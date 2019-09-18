<template>
  <div>
    <tree-menu />
    <admin-header />
    <admin-chat />
    <el-button :plain="true" v-show="false">成功</el-button>
    <div class="content-wrap">
      <div class="main">
        <div class="container-fluid">
          <div class="row">
            <div class="col-lg-8 p-0">
              <div class="page-header">
                <div class="page-title">
                  <h1>Dashboard 1</h1>
                </div>
              </div>
            </div>
            <div class="col-lg-4 p-0">
              <div class="page-header">
                <div class="page-title">
                  <ol class="breadcrumb text-right">
                    <li>
                      <a href="#">Dashboard</a>
                    </li>
                    <li class="active">Basic Form</li>
                  </ol>
                </div>
              </div>
            </div>
          </div>
          <div class="main-content">
            <el-form
              :model="ruleForm"
              :rules="rules"
              ref="ruleForm"
              label-width="100px"
              class="demo-ruleForm"
            >
              <el-form-item label="电影标签" prop="name">
                <el-input v-model="ruleForm.name"></el-input>
              </el-form-item>

              <el-form-item>
                <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
                <el-button @click="resetForm('ruleForm')">重置</el-button>
              </el-form-item>
            </el-form>
          </div>
          <!-- /# main content -->
          More Templates
          <a href="http://www.cssmoban.com/" target="_blank" title="模板之家">模板之家</a> - Collect from
          <a href="http://www.cssmoban.com/" title="网页模板" target="_blank">网页模板</a>
        </div>
        <!-- /# container-fluid -->
      </div>
      <!-- /# main -->
    </div>
    <!-- /# content wrap -->
  </div>
</template>

<script>
import AdminHeader from "@/components/AdminHeader.vue";
import TreeMenu from "@/components/TreeMenu.vue";
import AdminChat from "@/components/AdminChat.vue";

export default {
  components: {
    AdminHeader,
    TreeMenu,
    AdminChat
  },
  data() {
    return {
      ruleForm: {
        name: ""
      },
      rules: {
        name: [
          { required: true, message: "请输入电影标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      let self = this;
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.axios
            .post("http://127.0.0.1:5000/admin/tag/list", {
              name: this.ruleForm.name
            })
            .then(function(res) {
              console.log(res.data);
              if (res.data.code == 0) {
                self.$message.success("添加成功!");
              } else {
                self.$message.error("添加失败, " + res.data.msg);
                console.error(res.data);
              }
            })
            .catch(function(error) {
              console.error(error);
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    }
  }
};
</script>

<style scoped>
@import "../../assets/fontAwesome/css/fontawesome-all.min.css";
@import "../../assets/css/lib/themify-icons.css";
@import "../../assets/css/lib/mmc-chat.css";
@import "../../assets/css/lib/sidebar.css";
@import "../../assets/css/lib/nixon.css";
@import "../../assets/css/style.css";
</style>