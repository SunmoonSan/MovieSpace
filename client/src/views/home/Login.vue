<template>
  <el-container>
    <el-header>
      <MHeader />
    </el-header>
    <el-main>
      <el-button :plain="true" v-show="false">成功</el-button>
      <hr />
      <h1>登录</h1>
      <div class="login-form">
        <el-form
          :model="ruleForm"
          :rules="rules"
          ref="ruleForm"
          label-width="100px"
          class="ruleForm"
        >
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="ruleForm.email"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input v-model="ruleForm.password" type="password"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
            <el-button @click="resetForm('ruleForm')">重置</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>

    <el-footer style="height: 100%;">
      <m-footer />
    </el-footer>
  </el-container>
</template>

<script>
import MHeader from "@/components/Header.vue";
import MFooter from "@/components/Footer.vue";
export default {
  components: {
    MHeader,
    MFooter
  },
  data() {
    return {
      ruleForm: {
        email: ""
      },
      rules: {
        email: [
          {
            required: true,
            type: "email",
            message: "请输入邮箱",
            trigger: "blur"
          }
        ],
        password: [
          {
            required: true,
            type: "string",
            message: "请输入密码",
            trigger: "blur"
          }
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
            .post("http://127.0.0.1:5000/login", {
              email: this.ruleForm.email,
              password: this.ruleForm.password
            })
            .then(function(res) {
              if (res.data.code == 0) {
                // self.$message.success("登录成功!");
                location.href = "/";
              } else {
                self.$message({
                  type: "error",
                  message: "  登录失败, " + res.data.msg,
                  center: true
                });
                console.error(res.data);
              }
            })
            .catch(error => {
              console.error(error);
            });
        }
      });
    }
  }
};
</script>

<style>
.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  padding: 0px;
  text-align: center;
  height: 80px;
  line-height: 80px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  height: 600px;
}

body > .el-container {
  margin-bottom: 10px;
}

.login-form {
  width: 400px;
  margin: auto;
}
</style>
