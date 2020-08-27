<!-- 思维导图编辑器 -->
<template>
  <div class="mindmap">
    <VNBar />
    <div>
      <b-button v-b-toggle:my-collapse variant="outline-dark" class="tool">
        <div class="when-open">
          <b-icon icon="arrow-bar-left"></b-icon>
          <span>Close me</span>
        </div>
        <div class="when-closed">
          <span>Expand me</span>
          <b-icon icon="arrow-bar-right"></b-icon>
        </div>
      </b-button>
      <b-collapse id="my-collapse" class="toolbox">
        <b-button-group vertical size="sm" class="btn-group mt-3">
          <b-dropdown
            class="mt-2 mb-2"
            id="dropdown-dropright"
            dropright
            text="Theme"
            size="sm"
            squared
            variant="outline-secondary"
          >
            <b-dropdown-form style="height:30px;">
              <b-form-group>
                <select @change="set_theme" v-model="theme_value">
                  <option value>default</option>
                  <option value="primary">primary</option>
                  <option value="warning">warning</option>
                  <option value="danger">danger</option>
                  <option value="success">success</option>
                  <option value="info">info</option>
                  <option value="greensea" selected="selected">greensea</option>
                  <option value="nephrite">nephrite</option>
                  <option value="belizehole">belizehole</option>
                  <option value="wisteria">wisteria</option>
                  <option value="asphalt">asphalt</option>
                  <option value="orange">orange</option>
                  <option value="pumpkin">pumpkin</option>
                  <option value="pomegranate">pomegranate</option>
                  <option value="clouds">clouds</option>
                  <option value="asbestos">asbestos</option>
                </select>
              </b-form-group>
            </b-dropdown-form>
          </b-dropdown>
          <b-button squared variant="outline-secondary" @click="onMoveUp">Move to top</b-button>
          <b-button squared variant="outline-secondary" @click="onMoveDown">Move to bottom</b-button>
          <b-button squared variant="outline-secondary" @click="onRemoveNode">Delete Node</b-button>
          <b-button squared variant="outline-secondary" @click="addImageNode">Add Images</b-button>
          <b-button squared variant="outline-secondary" @click="addNode">Add Node</b-button>
          <b-button squared variant="outline-secondary" @click="saveLocalFile">Save as local file</b-button>
          <b-button squared variant="outline-secondary" @click="screenshot">Save as images</b-button>
          <b-button squared variant="outline-secondary" @click="zoomOut" ref="zoomOut">Zoom In</b-button>
          <b-button squared variant="outline-secondary" @click="zoomIn" ref="zoomIn">Zoom Out</b-button>
        </b-button-group>
      </b-collapse>
    </div>
    <div class="mind">
      <js-mind :values="mind" :options="options" ref="jsMind" height="500px"></js-mind>
    </div>
    <Toolkit />
  </div>
</template>

<script>
// @ is an alias to /src
import VNBar from "@/components/Navbar-Top-New/index.vue";
import Toolkit from "@/components/Toolkit/index.vue";

export default {
  name: "mindmap",
  components: {
    VNBar,
    Toolkit,
  },
  data() {
    return {
      theme_value: "",
      mind: {
        /* 元数据，定义思维导图的名称、作者、版本等信息 */
        meta: {
          name: "example",
          author: "906106844@qq.com",
          version: "0.2",
        },
        /* 数据格式声明 */
        format: "node_array",
        /* 数据内容 */
        data: [
          { id: "root", isroot: true, topic: "jsMind" },

          { id: "easy", parentid: "root", topic: "Easy", direction: "left" },
          { id: "easy1", parentid: "easy", topic: "Easy to show" },
          { id: "easy2", parentid: "easy", topic: "Easy to edit" },
          { id: "easy3", parentid: "easy", topic: "Easy to store" },
          { id: "easy4", parentid: "easy", topic: "Easy to embed" },

          {
            id: "open",
            parentid: "root",
            topic: "Open Source",
            expanded: false,
            direction: "right",
          },
          { id: "open1", parentid: "open", topic: "on GitHub" },
          { id: "open2", parentid: "open", topic: "BSD License" },

          {
            id: "powerful",
            parentid: "root",
            topic: "Powerful",
            direction: "right",
          },
          {
            id: "powerful1",
            parentid: "powerful",
            topic: "Base on Javascript",
          },
          { id: "powerful2", parentid: "powerful", topic: "Base on HTML5" },
          { id: "powerful3", parentid: "powerful", topic: "Depends on you" },
        ],
      },
      options: {
        // mode:'side'
      },
      shortCutVal: "",
      keyCode: "",
    };
  },
  mounted() {
    this.jm = this.$refs.jsMind.jm;
    this.jm.enable_edit();
  },
  methods: {
    addNode() {
      var selected_node = this.jm.get_selected_node(); // as parent of new node
      if (!selected_node) {
        alert("please select a node first.");
        return;
      }

      var nodeid = jsMind.util.uuid.newid();
      var topic = "new Node";
      var node = this.jm.add_node(selected_node, nodeid, topic);
    },
    onMoveUp() {
      var selected_id = this.jm.get_selected_node();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }
      this.jm.move_node(selected_id, "_first_");
    },
    onMoveDown() {
      var selected_id = this.jm.get_selected_node();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }

      this.jm.move_node(selected_id, "_last_");
    },
    onRemoveNode() {
      var selected_id = this.get_selected_nodeid();
      console.log(selected_id);
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }
      this.jm.remove_node(selected_id);
    },
    addImageNode() {
      var imageChooser = document.getElementById("image-chooser");
      const _this = this;
      imageChooser.addEventListener(
        "change",
        function (event) {
          // Read file here.
          var reader = new FileReader();
          reader.onloadend = function () {
            var selected_node = _this.jm.get_selected_node();
            var nodeid = jsMind.util.uuid.newid();
            var topic = undefined;
            var data = {
              "background-image": reader.result,
              width: "100",
              height: "100",
            };
            var node = _this.jm.add_node(selected_node, nodeid, topic, data);
          };

          var file = imageChooser.files[0];
          if (file) {
            reader.readAsDataURL(file);
          }
        },
        false
      );
      var selected_node = this.jm.get_selected_node(); // as parent of new node
      if (!selected_node) {
        alert("please select a node first.");
        return;
      }

      imageChooser.focus();
      imageChooser.click();
    },
    openLocalFile() {
      var file_input = this.$refs.input;
      var files = file_input.files;
      const _this = this;
      if (files.length > 0) {
        var file_data = files[0];
        jsMind.util.file.read(file_data, function (jsmind_data, jsmind_name) {
          var mind = jsMind.util.json.string2json(jsmind_data);
          if (!!mind) {
            _this.mind = mind;
            _this.jm.show(mind);
          } else {
            alert("can not open this file as mindmap");
          }
        });
      } else {
        alert("please choose a file first");
      }
    },
    saveLocalFile() {
      var mind_data = this.jm.get_data();
      var mind_name = mind_data.meta.name;
      var mind_str = jsMind.util.json.json2string(mind_data);
      jsMind.util.file.save(mind_str, "text/jsmind", mind_name + ".jm");
    },
    fontSize() {
      var selected_id = this.get_selected_nodeid();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }
      this.jm.set_node_font_style(selected_id, 28);
    },
    fontColor() {
      var selected_id = this.get_selected_nodeid();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }
      this.jm.set_node_color(selected_id, null, "#000");
    },
    bgColor() {
      var selected_id = this.get_selected_nodeid();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }

      this.jm.set_node_color(selected_id, "#eee", null);
    },
    bgImage() {
      var selected_id = this.get_selected_nodeid();
      if (!selected_id) {
        alert("please select a node first.");
        return;
      }
      this.jm.set_node_background_image(selected_id, "ant.png", 100, 100);
    },
    set_theme() {
      this.jm.set_theme(this.theme_value);
    },
    zoomOut() {
      if (this.jm.view.zoomOut()) {
        this.$refs.zoomOut.disabled = false;
      } else {
        this.$refs.zoomOut.disabled = true;
      }
    },
    zoomIn() {
      if (this.jm.view.zoomIn()) {
        this.$refs.zoomIn.disabled = false;
      } else {
        this.$refs.zoomIn.disabled = true;
      }
    },
    screenshot() {
      this.jm.screenshot.shootDownload();
    },
    // 获取选中标签的 ID
    get_selected_nodeid() {
      var selected_node = this.jm.get_selected_node();
      if (!!selected_node) {
        return selected_node.id;
      } else {
        return null;
      }
    },
    changeOption() {
      this.options = {
        mode: "side",
      };
    },
    // 只支持绑定单个按键
    shortcutSet(value) {
      if (value.key === "Backspace" || value.key === "Delete") {
        this.shortCutVal = this.shortCutVal.substring(
          0,
          this.shortCutVal.lastIndexOf("+")
        );
        this.keyCode = this.keyCode.substring(0, this.keyCode.lastIndexOf("+"));
        return;
      }
      if (this.shortCutVal) {
        this.shortCutVal += " + ";
        this.keyCode += "+";
      }
      this.shortCutVal += value.key;
      this.keyCode += value.keyCode;
      console.log("keyCode", this.keyCode);
      this.options = {
        shortcut: {
          mapping: {
            // 快捷键映射
            addchild: this.keyCode,
          },
        },
      };
    },
  },
};
</script>
<style scoped>
.mindmap {
  width: 100%;
  height: 95vh;
  padding-top: 100px;
}
.mind {
  /* padding-top: 100px; */
  z-index: 0;
}
.collapsed > .when-open,
.not-collapsed > .when-closed {
  display: none;
}
.tool {
  position: fixed;
  top: 75px;
  left: 30px;
  box-shadow: none !important;
  z-index: 1;
}
.toolbox {
  position: fixed;
  top: 100px;
  left: 30px;
  box-shadow: none !important;
  text-align: left;
  z-index: 3;
}
.toolbox button {
  width: 150px;
  margin-top: 10px;
  margin-bottom: 10px;
  box-shadow: none !important;
}
</style>