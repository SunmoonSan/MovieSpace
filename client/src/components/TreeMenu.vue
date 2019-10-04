<template>
  <el-menu default-active="2" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose">
    <router-link :to="{name:'admin'}">
      <el-menu-item index="1">
        <i class="el-icon-menu"></i>
        <span slot="title">首页</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'movie-list'}">
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">电影管理</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'tag-list'}">
      <el-menu-item index="2">
        <i class="el-icon-menu"></i>
        <span slot="title">标签管理</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'preview-list'}">
      <el-menu-item index="3">
        <i class="el-icon-menu"></i>
        <span slot="title">预告管理</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'auth-list'}">
      <el-menu-item index="3">
        <i class="el-icon-menu"></i>
        <span slot="title">权限管理</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'role-list'}">
      <el-menu-item index="3">
        <i class="el-icon-menu"></i>
        <span slot="title">角色管理</span>
      </el-menu-item>
    </router-link>
    <router-link :to="{name:'admin-list'}">
      <el-menu-item index="3">
        <i class="el-icon-menu"></i>
        <span slot="title">管理员管理</span>
      </el-menu-item>
    </router-link>
  </el-menu>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<style scoped>
@import "../assets/fontAwesome/css/fontawesome-all.min.css";
@import "../assets/css/lib/themify-icons.css";
@import "../assets/css/lib/mmc-chat.css";
@import "../assets/css/lib/sidebar.css";
</style>
</style>