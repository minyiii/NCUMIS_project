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
      <!-- <b-button v-b-modal.modal-1 class="mt-4" variant="outline-danger">Start Convert</b-button> -->

      <b-modal
        id="modal-1"
        title="Before Convert"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <template>
          <div class="w-100">
            <h5>Preview & Edit</h5>
            <textarea rows="10" v-model="text" class="form-control mb-3"></textarea>
          </div>
        </template>

        <template>
          <div class="w-100">
            <h5>Select</h5>
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

          <!-- <b-row>
            <b-col cols="4" class="mt-1">H4</b-col>
            <b-col>
              <b-form-select class="mb-1" v-model="H4" :options="variants"></b-form-select>
            </b-col>
          </b-row>-->

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
        <b-button block variant="outline-danger" class="mt-3 w-100" @click="TextValue">Convert</b-button>
      </b-modal>
      <app-reader @load="text = $event"></app-reader>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VNBar from "@/components/Navbar-Top-New/index.vue";
import UploadFile from "@/components/UploadFile/index.vue";

export default {
  name: "Convert",
  // data: () => ({ text: "" }),
  data() {
    return {
      text: "",
      file: null,
      correct: false,
      show: false,
      variants: ["Yes", "No"],
      // true false
      H2: "Yes",
      H3: "Yes",
      Paragraph: "Yes",
      Summary: "Yes",
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
    appReader: UploadFile,
  },
  created() {
    // 幫我去拿這個api的位置，然後回來的response;
    this.$axios.get("http://localhost:8081/#/convert").then((res) => {
      console.log(res);
    });
  },
  methods: {
    TextValue() {
      // this.$axios
      //   .post("http://localhost:8081/#/convert", {
      //     H2: this.H2,
      //     H3: this.H3,
      //     Paragraph: this.Paragraph,
      //     Summary: this.Summary,
      //   })
      //   .then((res) => {
      //     console.log(res);
      //   })
      //   .catch((error) => {
      //     consoli.log(error);
      //   });

      console.log(this.text);
      console.log(this.H2);
      console.log(this.H3);
      console.log(this.Summary);
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
@media screen and (max-width: 600px) {
  .convert {
    height: 120vh;
  }
  .target-container .box {
    width: 80vw;
  }
}
@media screen and (max-width: 400px) {
  .convert {
    height: 150vh;
  }
  .target-container .box {
    width: 60vw;
  }
}
</style>