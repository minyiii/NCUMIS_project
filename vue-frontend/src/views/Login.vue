<template>
  <div>
    <VBar />
    <div class="login">
      <div class="box p-4">
        <h2>Login</h2>
        <form action>
          <div class="form-group">
            <label for="account">Account :</label>
            <input type="text" name="account" id="account" class="form-control" />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input type="password" name="password" id="password" class="form-control" />
          </div>
          <input type="submit" value="Submit" class="btn btn-dark" />
        </form>
        <p>
          No account yet?
          <router-link :to="{name:'Register'}">Register Now!</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VBar from "@/components/Navbar-Top-After/index.vue";
// import InputComponent from '@/components/InputComponent/index.vue'

export default {
  name: "Login",
  // data(){
  //   return{
  //     title:"Hello"
  //   }
  // },
  components: {
    VBar,
    // InputComponent
  },
};
</script>

<style scoped>
.login {
  width: 100%;
  height: 92vh;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 50%;
  height: 400px;
  position: relative;
  top: 100px;
}
.box .btn {
  width: 100%;
  margin-top: 10px;
  margin-bottom: 15px;
  background: #fa5959;
  border: none;
  transition: 0.2s;
}
.box .btn:hover {
  background: #d01414;
}
.box p {
  text-align: center;
}
h2 {
  text-align: left;
}
.form-group {
  margin-top: 30px;
  margin-bottom: 30px;
  text-align: left;
}
</style>