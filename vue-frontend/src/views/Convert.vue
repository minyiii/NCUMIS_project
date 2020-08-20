<template>
  <div class="convert">
    <VNBar />
    <div class="target-container">
      <h1 class="mb-3">Convert</h1>
      <div class="box">
        <i class="far fa-file-code fa-6x mt-4 mb-5"></i>
        <h3>Preview</h3>
        <textarea rows="10" v-model="text" class="form-control"></textarea>
        <!-- @click="TextValue" -->
        <h3>Upload</h3>
        <h4>Beware the file has to be ".md" file!</h4>
      </div>
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
  data: () => ({ text: "" }),
  components: {
    VNBar,
    appReader: UploadFile,
    // props: true,
  },
  // methods: {
  //   TextValue() {
  //     // const getString = (value) => (value || this.text).toString();
  //     // String(this.text);
  //     // var symbol = Symbol(this.text);
  //     // String(symbol);
  //     // const s = String(this.text);
  //     // let s = this.text + "";
  //     // let y = [];
  //     alert(typeof this.text);
  //   },
  // },
};
</script>

<style scoped>
.convert {
  width: 100%;
  height: 140vh;
  margin-top: 30px;
  overflow: hidden;
}
.target-container {
  padding-top: 50px;
  /* background: rgb(255, 255, 255); */
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