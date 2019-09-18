<template>
  <el-row class="tac">
    <el-col :span="6">
      <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <router-link to="/home">
          <el-menu-item index="1">
            <i class="el-icon-menu"></i>
            <span slot="title">首页</span>
          </el-menu-item>
        </router-link>
        <router-link to="/tag/list">
          <el-menu-item index="2">
            <i class="el-icon-menu"></i>
            <span slot="title">标签管理</span>
          </el-menu-item>
        </router-link>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>标签管理</span>
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项1</el-menu-item>
          </el-submenu>
        </el-submenu>

        <el-menu-item index="3" disabled>
          <i class="el-icon-document"></i>
          <span slot="title">导航三</span>
        </el-menu-item>
        <el-menu-item index="4">
          <i class="el-icon-setting"></i>
          <span slot="title">导航四</span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
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