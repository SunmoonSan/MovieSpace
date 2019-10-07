<template>
  <el-container>
    <my-header />
    <el-main>
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
            <el-button @click="resetForm('ruleForm')">注册</el-button>
          </el-form-item>
        </el-form>
      </div>
    </el-main>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import MyHeader from "@/components/Header.vue";
import MFooter from "@/components/Footer.vue";
import jwt_decode from "jwt-decode";
export default {
  components: {
    MyHeader,
    MFooter
  },
  data() {
    return {
      ruleForm: {},
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
    submitForm(formname) {
      console.log(this);
      this.$refs[formname].validate(valid => {
        if (valid) {
          console.log(this);
          this.$axios
            .post("login", {
              email: this.ruleForm.email,
              password: this.ruleForm.password
            })
            .then(res => {
              if (res.status == 200 && res.data.code == 0) {
                this.$message({
                  message: "登录成功",
                  type: "success"
                });
                let token = res.data.data["token"];

                localStorage.setItem("eleToken", token);

                // token存储到vuex中
                const decoded = jwt_decode(token);
                // console.log(decoded);
                this.$store.dispatch(
                  "setAuthenticated",
                  !this.isEmpty(decoded)
                );
                this.$store.dispatch("setUser", decoded.data);

                this.$router.push("/");
              } else {
                this.$message({
                  message: res.data.msg,
                  type: "error"
                });
              }
            })
            .catch(err => {
              console.error(err);
            });
        }
      });
    },
    isEmpty(value) {
      return (
        value === undefined ||
        value === null ||
        (typeof value === "object" && Object.keys(value).length === 0) ||
        (typeof value === "string" && value.trim().length === 0)
      );
    }
  }
};
</script>

<style>
.el-header,
.el-footer {
  /* background-color: #b3c0d1; */
  /* color: #333; */
  text-align: center;
  line-height: 60px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
}

body > .el-container {
  margin-bottom: 40px;
}

.login-form {
  width: 600px;
  margin: 100px auto;
}
</style>