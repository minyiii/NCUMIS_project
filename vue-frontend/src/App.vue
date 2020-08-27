<template>
  <div id="app">
    <div class="nav"></div>
    <router-view />
    <div
      class="row bg-light d-flex justify-content-center align-items-center text-center pt-3 fixed-bottom"
      id="footer"
    >
      <p>Copyright &copy; 2020 KeyInMind</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
#app {
  outline: none;
  width: 100%;
  font-family: "Comfortaa", "Noto Serif TC", Avenir, Helvetica, Arial,
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #f3f1ee;
  transition: 0.2s;
}
</style>
