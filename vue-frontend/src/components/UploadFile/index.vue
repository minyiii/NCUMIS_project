<script>
// import Modal from '@/components/Modal.vue';
export default {
  name: "upload",
  data() {
    return {
      file: null,
      correct: false,
    };
  },
  methods: {
    loadTextFromFile(ev) {
      const file = ev.target.files[0];
      const reader = new FileReader();
      reader.onload = (e) => this.$emit("load", e.target.result);
      reader.readAsText(file);

      return (this.$data.correct = true);
    },
    clearFiles() {
      this.$refs["file-input"].reset();
      return (this.$data.correct = false);
    },
    submitFiles() {
      let input = this.$refs["file-input"].$el.innerText;
      if (
        (input.substring(input.lastIndexOf(".")).toLowerCase() != ".md") &
        (input.toLowerCase() != "no file chosen")
      ) {
        alert('The file has to be ".md" file!');
        return (this.$data.correct = false);
      }
      // if (input.toLowerCase() === "no file chosen") {
      //   alert("Please Upload Your File First!");
      // } else if (
      //   (input.substring(input.lastIndexOf(".")).toLowerCase() != ".md") &
      //   (input.toLowerCase() != "no file chosen")
      // ) {
      //   alert('The file has to be ".md" file!');
      // } else {
      //   // console.log(this.file);
      //   // console.log(this.text);
      //   // alert(this.H2);
      // }
    },
  },
};
</script>
<template src="./template.html"></template>
<style src="./style.css" scoped></style>
