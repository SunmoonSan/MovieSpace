<template>
  <el-container>
    <my-header />
    <b-container>
      <div class="movie-detail">
        <b-row>
          <b-col cols="4">
            <b-list-group>
              <b-list-group-item>会员中心</b-list-group-item>
              <b-list-group-item>修改密码</b-list-group-item>
              <b-list-group-item>评论记录</b-list-group-item>
              <b-list-group-item>登录日志</b-list-group-item>
              <b-list-group-item>收藏电影</b-list-group-item>
            </b-list-group>
          </b-col>

          <b-col cols="8">
            <div class="profile-form">
              <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group label-cols-sm="2" label="旧密码:">
                  <b-form-input type="password" v-model="form.oldpwd" required />
                </b-form-group>

                <b-form-group label-cols-sm="2" label="新密码:">
                  <b-form-input type="password" v-model="form.newpwd" required />
                </b-form-group>

                <b-form-group>
                  <b-button type="submit" variant="primary" class="btn">保存</b-button>
                  <b-button type="reset" variant="danger" class="btn">重置</b-button>
                </b-form-group>
              </b-form>
            </div>
          </b-col>
        </b-row>
      </div>
    </b-container>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import MyHeader from "@/components/Header.vue";
import MFooter from "@/components/Footer.vue";
export default {
  props: {
    movieId: String
  },
  components: {
    MyHeader,
    MFooter
  },
  data() {
    return {
      form: {
        email: "",
        name: "",
        phone: "",
        info: ""
      },
      imageUrl: "",
      postData: {
        token: ""
      }
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      this.$axios
        .put("password/modify", {
          oldpwd: this.form.oldpwd,
          newpwd: this.form.newpwd
        })
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.$message({
              type: "success",
              message: "密码修改成功"
            });
          }
        })
        .catch(err => {
          console.log(err);
        });
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.name = "";
      this.form.food = null;
      this.form.checked = [];
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    }
  },
  created() {}
};
</script>

<style>
.el-header,
.el-footer {
  text-align: center;
  line-height: 60px;
}

.movie-detail {
  margin-top: 20px;
}

.profile-form {
  text-align: right;
}
.avatar {
  margin-right: 80%;
}
.btn {
  margin-left: 20px;
  padding-left: 20px;
  padding-right: 20px;
}
</style>