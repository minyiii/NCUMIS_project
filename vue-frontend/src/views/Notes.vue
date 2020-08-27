<template>
  <div id="notes">
    <VNBar />
    <b-container>
      <h3>Notes</h3>
      <b-row class="pt-3 pb-3" align-h="start">
        <b-col cols="4" class="pb-3" v-for="item in file" :key="item.name">
          <b-button class="content" variant="light">
            {{item.name}}
            <p>{{item.describe}}</p>
          </b-button>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
export default {
  name: "notes",
  components: {
    VNBar,
  },
  data() {
    return {
      file: [
        {
          name: "Example.md",
          describe: "you are a nerd",
        },
        {
          name: "Example2.md",
          describe: "aa",
        },
        {
          name: "Example3.md",
          describe: "s",
        },
        {
          name: "Example4.md",
          describe: "s",
        },
        {
          name: "Example5.md",
          describe: "s",
        },
        {
          name: "Example6.md",
          describe: "s",
        },
      ],
    };
  },
  computed: {},
};
</script>
<style scoped>
#notes {
  margin: auto;
  padding-top: 100px;
  padding-bottom: 150px;
  width: 80%;
  /* height: 600px; */
}
.content {
  width: 250px;
  height: 250px;
  overflow: hidden;
}
.content p {
  width: 220px;
  text-align: left;
  margin-bottom: 0px;
  font-size: smaller;
  word-wrap: break-word;
  padding-top: 20px;
  padding-left: 20px;
  padding-right: 20px;
  /* background-color: red; */
  color: rgb(97, 97, 97);
  overflow: hidden;
}
</style>