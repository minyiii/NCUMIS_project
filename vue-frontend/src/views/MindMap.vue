<template>
  <div id="mindmapview">
    <VNBar />
    <b-container>
      <h3>MindMap</h3>
      <b-row class="pt-3 pb-3" align-h="start">
        <b-col cols="12" sm="6" md="4" class="pb-3" v-for="(item,index) in file" :key="item.name">
          <b-button
            class="content"
            variant="light"
            :to="{path: '/mmedit/' + index}"
            style="z-index:0;"
          >
            <h5>{{item.name}}</h5>
            <p>{{item.describe}}</p>
          </b-button>
          <div class="d-flex justify-content-center">
            <b-button class="ml-2 mr-2 mt-2 btn-edit" size="sm" v-b-modal="modalId(index)">Edit</b-button>
            <b-modal :id="'modal' + index" title="Edit Your Description" centered>
              <b-form-textarea
                id="textarea-plaintext"
                :value="item.describe"
                v-model="item.describe"
              ></b-form-textarea>
              <template v-slot:modal-footer>
                <b-button size="sm" variant="info" @click="save(index)">Save</b-button>
              </template>
            </b-modal>
            <b-button class="ml-2 mr-2 mt-2 btn-edit" size="sm" v-b-modal="modalId2(index)">Delete</b-button>
            <b-modal :id="'modal' + index + index" size="sm" hide-header centered>
              <h5>Are you sure?</h5>
              <template v-slot:modal-footer="{ cancel }">
                <b-button variant="danger" size="sm" @click="removeItem(index)">Yes</b-button>
                <b-button variant="secondary" size="sm" @click="cancel">No</b-button>
              </template>
            </b-modal>
          </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
export default {
  name: "mindmapview",
  components: {
    VNBar,
  },
  data() {
    return {
      file: [
        // {
        //   name: "Example.md",
        //   describe: "you are a nerd !!!",
        // },
        // {
        //   name: "Example2.md",
        //   describe: "aa",
        // },
        // {
        //   name: "Example3.md",
        //   describe: "sada",
        // },
        // {
        //   name: "Example4.md",
        //   describe: "424",
        // },
        // {
        //   name: "Example5.md",
        //   describe: "235",
        // },
        // {
        //   name: "Example6.md",
        //   describe: "adad",
        // },
      ],
    };
  },
  mounted() {
    this.$axios.get("http://localhost:3000/test").then((res) => {
      this.file = res.data;
    });
  },
  methods: {
    modalId(i) {
      return "modal" + i;
    },
    modalId2(i) {
      return "modal" + i + i;
    },
    save(index) {
      // alert(this.file[this.file.indexOf(item)].describe);
      let target = this.file[index];
      this.$axios
        .patch("http://localhost:3000/test" + "/" + target.id, {
          describe: target.describe,
        })
        .then((res) => {
          console.log(res.data);
          this.$router.go("/mindmap");
        });
    },
    removeItem: function (index) {
      // this.file.splice(this.file.indexOf(item), 1);
      // console.log(index);
      let target = this.file[index];
      this.$axios
        .delete("http://localhost:3000/test" + "/" + target.id)
        .then((res) => {
          console.log(res);
          this.file.splice(index, 1);
        });
    },
  },
  computed: {},
};
</script>
<style scoped>
#mindmapview {
  margin: auto;
  padding-top: 100px;
  padding-bottom: 150px;
  width: 80%;
  /* height: 600px; */
}
.btn-edit {
  width: 30%;
}
.content {
  width: 250px;
  height: 200px;
  padding: 50px;
  padding-top: 70px;
  overflow: hidden;
}
.content p {
  width: 150px;
  height: 55px;
  text-align: left;
  margin-bottom: 20px;
  font-size: smaller;
  word-wrap: break-word;
  padding-top: 15px;
  padding-left: 15px;
  padding-right: 15px;
  color: rgb(97, 97, 97);
  overflow: hidden;
}
@media screen and (max-width: 1024px) {
  #mindmapview {
    height: 100vh;
  }
  .content {
    width: 200px;
    height: 160px;
    padding: 30px;
    padding-top: 45px;
  }
  .btn-edit {
    width: 100px;
  }
}
@media screen and (max-width: 760px) {
  #mindmapview {
    height: auto;
  }
  .btn-edit {
    width: 80px;
  }
}
</style>