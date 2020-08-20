<template>
  <div class="settings">
    <VNBar />
    <div class="row box p-4">
      <div class="col-12 col-md-6 l-section">
        <h2>Settings</h2>
        <b-form @submit="onSubmit" @reset="onReset" v-if="show" class="mt-4">
          <b-form-group id="input-group-1" label="Name:" label-for="input-1">
            <b-form-input id="input-1" v-model="form.name" required placeholder="Enter name"></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Email:" label-for="input-2">
            <b-form-input id="input-2" type="email" v-model="form.email" required></b-form-input>
          </b-form-group>
          <b-row class="mt-3 p-3">
            <b-button type="submit" class="btn btn-dark w-50">Save</b-button>
            <b-button type="reset" class="btn btn-dark w-50">Cancel</b-button>
          </b-row>
        </b-form>
      </div>
      <div class="col-12 col-md-6 text-center r-section">
        <b-img v-bind:src="photo" v-bind="mainProps" />
        <!-- <b-button type="submit" class="btn btn-dark" @change="UploadImages">Upload Images</b-button> -->
        <!-- <input type="reset" value="Reset Image" class="btn btn-dark" /> -->
        <b-form-file
          v-model="file"
          ref="file-input"
          accept="image/jpeg, image/png"
          placeholder="Upload Images"
          drop-placeholder="Drop file here..."
          @change="UploadImages"
          class="mt-3"
          style="overflow: hidden; width:350px"
        ></b-form-file>
        <b-button @click="resetFiles" style="width:350px">Reset Images</b-button>
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
      file: null,
      photo:
        "https://pbs.twimg.com/media/Efx05jfUwAAodUy?format=jpg&name=large",
      mainProps: {
        width: "350px",
        height: "300px",
      },
      form: {
        name: "",
        email: "",
      },
      show: true,
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.name = "";
      this.form.email = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    UploadImages(e) {
      const image = e.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(image);
      reader.onload = (e) => {
        this.photo = e.target.result;
      };
    },
    resetFiles() {
      this.photo =
        "https://pbs.twimg.com/media/Efx05jfUwAAodUy?format=jpg&name=large";
      this.$refs["file-input"].reset();
    },
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
  width: 80%;
  height: 90%;
  position: relative;
  margin-top: 100px;
  text-align: left;
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