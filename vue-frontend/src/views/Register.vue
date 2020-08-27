<template>
  <div>
    <VBar />
    <div class="login">
      <div class="box p-4">
        <router-link to="/convert">Convert</router-link>
        <h2>Register</h2>
        <form action>
          <div class="form-group">
            <label for="account">Account :</label>
            <input type="text" name="account" id="account" class="form-control" />
          </div>
          <div class="form-group">
            <label for="date">Birthday :</label>
            <input type="date" name="date" id="date" class="form-control" />
          </div>
          <div class="form-group">
            <label for="email">E-mail :</label>
            <input type="email" name="email" id="email" class="form-control" />
          </div>
          <div class="form-group">
            <label for="password">Password :</label>
            <input type="password" name="password" id="password" class="form-control" />
          </div>
          <div class="form-group">
            <label for="pwd-confirm">Confirm Password :</label>
            <input type="password" id="pwd-confirm" class="form-control" />
          </div>
          <div class="btn-group d-flex">
            <input type="reset" value="Reset" class="btn btn-dark" />
            <input type="submit" value="Submit" class="btn btn-dark" />
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import VBar from "@/components/Navbar-Top-After/index.vue";

export default {
  name: "Register",
  components: {
    VBar,
  },
};
</script>

<style scoped>
.login {
  width: 100%;
  height: 140vh;
}
.box {
  margin: auto;
  background: white;
  border: 1px solid #e2dada;
  width: 50%;
  height: 680px;
  position: relative;
  top: 100px;
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
h2 {
  text-align: left;
}
.form-group {
  margin-top: 30px;
  margin-bottom: 30px;
  text-align: left;
}
</style>
