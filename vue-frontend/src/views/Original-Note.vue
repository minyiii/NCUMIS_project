<template>
  <!-- 沒有工具欄的 MD EDITOR -->
  <div class="notes" id="editor">
    <VNBar />
    <div class="container">
      <div class="row mt-4">
        <div class="col-md-6">
          <h4>Markdown</h4>
          <textarea class="info" :value="markdown" @input="update"></textarea>
          <!-- <textarea class="info" cols="30" rows="10" v-model="markdown" debounce="300"></textarea> -->
        </div>
        <div class="col-md-6">
          <h4>Preview</h4>
          <div class="info preview" v-html="compiledMarkdown"></div>
        </div>
      </div>
    </div>
    <!-- <textarea v-model="input" debounce="300"></textarea> -->
    <!-- <div v-html="input | marked"></div> -->
  </div>
</template>

<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
import _ from "lodash";
import marked from "marked";

export default {
  name: "notes",
  components: {
    VNBar,
  },
  data() {
    return {
      markdown: "",
    };
  },
  computed: {
    compiledMarkdown: function () {
      return marked(this.markdown, { sanitize: true });
    },
  },
  methods: {
    update: _.debounce(function (e) {
      this.markdown = e.target.value;
    }, 300),
  },
};
</script>

<style scoped>
.notes {
  margin: 0;
  width: 100%;
  height: 95vh;
  padding-top: 100px;
  color: #333;
}
.info {
  height: 400px;
  width: 100%;
  background-color: #f6f6f6;
}
textarea {
  border: none;
  border-right: 1px solid #ccc;
  resize: none;
  outline: none;
  background-color: #f6f6f6;
  font-size: 14px;
  padding: 20px;
}
.preview {
  text-align: left;
  padding: 10px;
}
code {
  color: #f66;
}
</style>