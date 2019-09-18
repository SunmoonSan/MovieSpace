<template>
  <el-container>
    <el-header>
      <MHeader />
    </el-header>
    <el-main>
      <el-button :plain="true" v-show="false">成功</el-button>
      <hr />
      <h1>注册</h1>

      <div class="register-form">
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

          <el-form-item label="确认密码" prop="confirmPwd">
            <el-input v-model="ruleForm.confirmPwd" type="password"></el-input>
          </el-form-item>

          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
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
        ],
        confirmPwd: [
          {
            required: true,
            type: "string",
            message: "请再次输入密码",
            trigger: "blur"
          },
          {
            validator: (rule, value, callback) => {
              if (value === "") {
                callback(new Error("请再次输入密码"));
              } else if (value !== this.ruleForm.password) {
                callback(new Error("两次密码输入不一致"));
              } else {
                callback();
              }
            },
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    submitForm(formName) {
      let self = this;
      console.log("this");
      console.log(this);
      this.$refs[formName].validate(valid => {
        console.log(valid);
        console.log(this.rules);
        if (valid) {
          this.axios
            .post("http://127.0.0.1:5000/register", {
              email: this.ruleForm.email,
              password: this.ruleForm.password
            })
            .then(function(res) {
              if (res.data.code == 0) {
                self.$message.success("注册成功!");
              } else {
                self.$message.error("注册失败, " + res.data.msg);
                console.error(res.data);
              }
            })
            .catch(function(error) {
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

.register-form {
  width: 400px;
  margin: auto;
}
</style>
