<template>
  <div id="editor">
    <VNBar />
    <mavon-editor
      ref="md"
      :subfield="subfield"
      :toolbarsFlag="toolbarsFlag"
      :editable="editable"
      :language="d_language"
      @change="change"
      @save="saveone"
      :ishljs="true"
      class="item-editor"
      v-model="help1"
      :autofocus="autofocus"
      :shortCut="true"
      :externalLink="external_link"
      @subfield-toggle="$subfieldtoggle"
      @preview-toggle="$previewtoggle"
      :imageFilter="image_filter"
      :boxShadow="true"
      :scrollStyle="true"
      :transition="true"
      style="height: 100%; z-index: 0"
    ></mavon-editor>
  </div>
</template>

<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
// Local Registration
// import { mavonEditor } from "mavon-editor";
// import "mavon-editor/dist/css/index.css";
export default {
  name: "editor",
  components: {
    VNBar,
  },
  data() {
    return {
      d_language: "zh-TW",
      help1: "",
      help2: "",
      d_words: {},
      screen_phone: false,
      toolbars: {
        underline: true, // 下划线
        strikethrough: true, // 中划线
        alignCenter: true, // 中划线
        undo: true,
        save: true,
        fullscreen: true, // 全屏编辑
        navigation: true,
        preview: true,
        subfield: false,
      },
      autofocus: true,
      subfield: true,
      editable: true,
      toolbarsFlag: true,
      img_file: {},
      external_link: {
        markdown_css: function () {
          return "/markdown/github-markdown.min.css";
        },
        hljs_js: function () {
          return "/highlightjs/highlight.min.js";
        },
        hljs_css: function (css) {
          return "/highlightjs/styles/" + css + ".min.css";
        },
        hljs_lang: function (lang) {
          return "/highlightjs/languages/" + lang + ".min.js";
        },
        katex_css: function () {
          return "/katex/katex.min.css";
        },
        katex_js: function () {
          return "/katex/katex.min.js";
        },
      },
      toolbar_settings: {
        undo: true, // 上一步
        redo: true, // 下一步
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        code: true, // code
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true, // 预览
        /* 1.4.2 */
        navigation: true, // 导航目录
      },
      image_filter: function ($files) {
        console.log("image_filter files:", $files);
        // console.log('here for you', $files);
        return true;
      },
      imageClick: function (file) {
        console.log(file);
      },
      imgName: "",
    };
  },
  toolbars: {
    bold: true, // 粗体
    italic: true, // 斜体
    header: true, // 标题
    underline: true, // 下划线
    strikethrough: true, // 中划线
    mark: true, // 标记
    superscript: true, // 上角标
    subscript: true, // 下角标
    quote: true, // 引用
    ol: true, // 有序列表
    ul: true, // 无序列表
    link: true, // 链接
    imagelink: true, // 图片链接
    code: true, // code
    table: true, // 表格
    fullscreen: true, // 全屏编辑
    readmodel: true, // 沉浸式阅读
    htmlcode: true, // 展示html源码
    help: true, // 帮助
    /* 1.3.5 */
    undo: true, // 上一步
    redo: true, // 下一步
    trash: true, // 清空
    save: true, // 保存（触发events中的save事件）
    /* 1.4.2 */
    navigation: true, // 导航目录
    /* 2.1.8 */
    alignleft: true, // 左对齐
    aligncenter: true, // 居中
    alignright: true, // 右对齐
    /* 2.2.1 */
    subfield: true, // 单双栏模式
    preview: true, // 预览
  },
  created() {
    var $vm = this;
    this.sizeToStatus();
    window.addEventListener("resize", function () {
      // 媒介查询
      $vm.sizeToStatus();
    });
  },
  //   mounted() {
  //     var md = this.$refs.md;
  //     var toolbar_left = md.$refs.toolbar_left;
  //   },
  methods: {
    sizeToStatus() {
      if (window.matchMedia("(min-width:768px)").matches) {
        // > 768
        this.screen_phone = false;
      } else {
        // <  768
        this.screen_phone = true;
      }
    },
    saveone(val, render) {
      //   alert("save one");
      //   console.log(val);
      alert(val);
    },
    savetwo(val, render) {
      alert("save two");
    },
    change(val, render) {
      console.log(val);
    },
    $subfieldtoggle(flag, value) {
      console.log("sufield toggle" + flag);
    },
    $previewtoggle(flag, value) {
      console.log("preview toggle" + flag);
    },
    imgdelete() {
      var md = this.$refs.md;
      var toolbar_left = md.$refs.toolbar_left;
      toolbar_left.$imgDelByFilename(this.imgName);
    },
  },
};
</script>

<style>
#editor {
  margin: auto;
  padding-top: 60px;
  padding-bottom: 60px;
  width: 80%;
  height: 600px;
}
</style>
