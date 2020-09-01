<template>
  <form enctype="multipart/form-data">
    <div class="field" id="test">
      <label for="file" class="label">Upload File</label>
      <input type="file" id="file" ref="file" @change="handleFileUpload()" />
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </form>
</template>
<script>
export default {
  name: "test",
  data() {
    return {
      file: "",
    };
  },
  methods: {
    handleFileUpload() {
      //   const file = ev.target.files[0];
      //   const reader = new FileReader();
      //   reader.onload = (e) => this.$emit("load", e.target.result);
      //   reader.readAsText(file);
      this.file = this.$refs.file.files[0];
    },
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      this.$axios
        .post("http://localhost:3000/contents", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
    },
  },
};
</script>
<style scoped>
#test {
  height: 100vh;
}
</style>