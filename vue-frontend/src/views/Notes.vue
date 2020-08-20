<template>
  <div class="notes">
    <VNBar />
  </div>
</template>

<script>
import VNBar from "@/components/Navbar-Top-New/index.vue";
export default {
  name: "notes",
  components: {
    VNBar,
  },
};
</script>

<style scoped>
.notes {
  width: 100%;
  height: 95vh;
  padding-top: 100px;
}
</style>