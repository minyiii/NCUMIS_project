<template>
  <div class="settings">
    <VNBar />
    <div class="row box p-4">
      <div class="col-12 col-md-6">
        <h2>Settings</h2>
        <form action>
          <div class="form-group">
            <label for="name">Name :</label>
            <input type="text" id="name" class="form-control" />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input type="password" id="password" class="form-control" />
          </div>
          <input type="submit" value="儲存" class="btn btn-dark w-100" />
        </form>
      </div>
      <div class="col-12 col-md-6 text-center">
        <div id="imgzone">
          <img v-bind:src="photo" class="img-thumbnail" />
        </div>
        <div class="btn-group">
          <!-- <input type="reset" value="Reset Image" class="btn btn-dark"> -->
          <input type="submit" value="Upload Image" class="btn btn-dark" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VNBar from "@/components/Navbar-Top-New/index.vue";

export default {
  name: "Settings",
  components: {
    VNBar,
  },
  data() {
    return {
      photo: "https://picsum.photos/300/300",
    };
  },
};
</script>

<style scoped>
.settings {
  width: 90vw;
  height: 90vh;
  margin: auto;
  align-items: center;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 70%;
  height: 80%;
  position: relative;
  margin-top: 100px;
  text-align: left;
  /* top: 100px; */
}
.box .btn {
  margin-top: 10px;
  margin-bottom: 15px;
  background: #fa5959;
  border: 2px solid #ffffff;
  transition: 0.2s;
}
.box .btn:hover {
  background: #d01414;
}
.box p {
  text-align: center;
}
.btn-group {
  width: 60%;
}
</style>