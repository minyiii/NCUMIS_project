<template>
  <div class="convert">
    <VNBar />
    <div class="target-container">
      <h1 class="mb-3">Convert</h1>
      <div class="box">
        <i class="far fa-file-code fa-6x mt-4 mb-5"></i>
        <h3>Upload</h3>
        <h4>Beware the file has to be ".md" file!</h4>
      </div>
    </div>
    <form class="pt-3 text-center">
      <div class="d-flex justify-content-center pb-3">
        <b-form-file
          style="width:40%;"
          type="file"
          v-model="file"
          @change="getFile($event)"
          ref="file-input"
          accept=".md"
        ></b-form-file>
        <b-button
          @click="clearFiles"
          class="ml-2"
          style="width:100px; height: 35px; margin-top: 2px;"
        >Reset</b-button>
      </div>
      <!-- 如果小於某寬度的話就顯示 -->
      <!-- <p class="mt-3">
        Selected file :
        <b>{{ file ? file.name : '' }}</b>
      </p>-->
      <b-button
        v-if="correct"
        v-b-modal.m1
        class="mb-4"
        variant="outline-danger"
        @click="checkFiles"
      >Start Convert</b-button>
      <b-button
        v-else
        disabled
        v-b-modal.m1
        class="mb-4"
        variant="outline-danger"
        @click="checkFiles"
      >Start Convert</b-button>
      <b-modal
        id="m1"
        title="Select"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <template>
          <div class="w-100">
            <p variant="danger">Choose the node levels you would like to show on the MindMap!</p>
          </div>
        </template>
        <b-container fluid>
          <b-row class="mb-1 text-center">
            <b-col cols="4"></b-col>
            <b-col>Node Level</b-col>
          </b-row>

          <b-row class="mb-1">
            <b-col cols="4" class="mt-1">H2</b-col>
            <b-col>
              <b-form-select v-model="H2" :options="variants"></b-form-select>
            </b-col>
          </b-row>

          <b-row class="mb-1">
            <b-col cols="4" class="mt-1">H3</b-col>
            <b-col>
              <b-form-select v-model="H3" :options="variants"></b-form-select>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="4" class="mt-1">Paragraph</b-col>
            <b-col>
              <b-form-select class="mb-1" v-model="Paragraph" :options="variants"></b-form-select>
            </b-col>
          </b-row>

          <b-row>
            <b-col cols="4" class="mt-1">Summary</b-col>
            <b-col>
              <b-form-select class="mb-1" v-model="Summary" :options="variants"></b-form-select>
            </b-col>
          </b-row>
        </b-container>

        <template v-slot:modal-footer>
          <div class="w-100">
            <b-button style="display:none;"></b-button>
          </div>
        </template>
        <b-button
          block
          variant="outline-danger"
          class="mt-3 w-100"
          @click="submitForm($event)"
        >Convert</b-button>
      </b-modal>
      {{ checkStatus }}
    </form>
  </div>
</template>

<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
export default {
  name: "convert",
  data() {
    return {
      file: null,
      checkStatus: "",
      correct: false,
      variants: ["yes", "no"],
      // true false
      H2: "yes",
      H3: "yes",
      Paragraph: "yes",
      Summary: "yes",
      headerBgVariant: "dark",
      headerTextVariant: "light",
      bodyBgVariant: "light",
      bodyTextVariant: "dark",
      footerBgVariant: "light",
      footerTextVariant: "danger",
    };
  },
  components: {
    VNBar,
  },
  methods: {
    getFile(event) {
      (this.file = event.target.files[0]), console.log(this.file);
      return (this.$data.correct = true);
    },
    clearFiles() {
      this.$refs["file-input"].reset();
      return (this.$data.correct = false);
    },
    submitForm(event) {
      // event.preventDefault();
      let formData = new FormData();
      formData.append("file", this.file);
      let config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      // 创建一个空的axios 对象
      const instance = this.$axios.create({
        withCredentials: true, // 如果发送请求的时候需要带上token 验证之类的也可以写在这个对象里
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log(this.H2);

      instance
        .post("http://127.0.0.1:8000/fileUpload/upload/", formData)
        .then((res) => {
          if (res.data.code === 200) {
            alert(res.data.msg);
            this.checkStatus = res.data;
          } else if (res.data.code === 2) {
            alert(res.data.msg);
          } else {
            alert(res.data.msg);
          }
        });

      this.$axios
        .post("http://127.0.0.1:8000/mindmap/convert/", {
          H2: this.H2,
          H3: this.H3,
          Paragraph: this.Paragraph,
          Summary: this.Summary,
        })
        .then((res) => {
          this.$router.push("/mindmap");
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    checkFiles() {
      let input = this.$refs["file-input"].$el.innerText;
      if (
        (input.substring(input.lastIndexOf(".")).toLowerCase() != ".md") &
        (input.toLowerCase() != "no file chosen")
      ) {
        alert('The file has to be ".md" file!');
        return (this.$data.correct = false);
      }
    },
  },
};
</script>

<style scoped>
.convert {
  width: 100%;
  height: 110vh;
  margin-top: 30px;
  overflow: hidden;
  text-align: center;
}
.target-container {
  padding-top: 50px;
}
.target-container .box {
  width: 45vw;
  padding: 20px;
  margin: auto;
  border: 5px dashed #707070;
  border-radius: 5rem;
  background: #ffffff;
}
.target-container .box h4 {
  color: rgb(230, 86, 86);
}
.target-container textarea {
  margin: auto;
  width: 30vw;
  margin-bottom: 30px;
  height: 50px;
}
</style>