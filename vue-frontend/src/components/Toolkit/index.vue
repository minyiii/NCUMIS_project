<script>
/* eslint-disable */
export default {
  name: "toolkit",
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
          if (mind) {
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
      if (selected_node) {
        return selected_node.id;
      } else {
        return null;
      }
    },
  },
};
</script>
<template src="./template.html"></template>
<style src="./style.css" scoped></style>