<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-main>Main</el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
// import "@/assets/js/lib/jquery.min.js";
// import sidebar from '@/assets/js/lib/sidebar.js';
// import "@/assets/js/lib/sidebar.js";
import TreeMenu from "@/components/TreeMenu.vue";
import AdminHedaer from "@/components/AdminHeader.vue";
export default {
  components: {
    TreeMenu,
    AdminHedaer
  },
  data() {
    return {
      // sidebar
    };
  }
};
</script>

<style lang="css">
@import "../../assets/fontAwesome/css/fontawesome-all.min.css";
@import "../../assets/css/lib/themify-icons.css";
@import "../../assets/css/lib/mmc-chat.css";
@import "../../assets/css/lib/sidebar.css";
/* @import "../../assets/css/lib/bootstrap.min.css"; */
@import "../../assets/css/lib/nixon.css";
@import "../../assets/lib/lobipanel/css/lobipanel.min.css";
@import "../../assets/css/style.css";
.admin-home {
  height: 1682px;
  width: 1428px;
}
</style>
