<template>
  <div class="home">
    <VBar />
    <Content />
  </div>
</template>

<script>
// @ is an alias to /src
import VBar from "@/components/Navbar-Top/index.vue";
import Content from "@/components/Content/index.vue";

export default {
  name: "Home",
  components: {
    Content,
    VBar,
  },
};
</script>
