<template>
  <el-container>
    <my-header />
    <b-container>
      <div class="movie-detail">
        <b-row>
          <b-col cols="4">
            <b-list-group>
              <b-list-group-item variant="info">
                <router-link to="/profile">会员中心</router-link>
              </b-list-group-item>
              <b-list-group-item>
                <router-link to="/password/modify">修改密码</router-link>
              </b-list-group-item>
              <b-list-group-item>评论记录</b-list-group-item>
              <b-list-group-item>登录日志</b-list-group-item>
              <b-list-group-item>
                <router-link :to="{name: 'movie-collections'}">电影收藏</router-link>
              </b-list-group-item>
            </b-list-group>
          </b-col>

          <b-col cols="8">
            <div class="profile-form">
              <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group label-cols-sm="2" label="头像:">
                  <el-upload
                    class="avatar-uploader"
                    action="http://up-z2.qiniup.com"
                    :show-file-list="false"
                    :on-success="handleAvatarSuccess"
                    :before-upload="beforeAvatarUpload"
                    :data="postData"
                  >
                    <el-avatar
                      v-if="imageUrl"
                      :size="100"
                      shape="square"
                      class="avatar"
                      :src="imageUrl"
                    ></el-avatar>
                    <el-avatar
                      v-else
                      :size="100"
                      shape="square"
                      src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                    ></el-avatar>
                  </el-upload>
                </b-form-group>

                <b-form-group label-cols-sm="2" label="邮箱:">
                  <b-form-input v-model="form.email" type="email" required />
                </b-form-group>

                <b-form-group label-cols-sm="2" label="用户名:">
                  <b-form-input v-model="form.name" required />
                </b-form-group>

                <b-form-group label-cols-sm="2" label="手机号:">
                  <b-form-input v-model="form.phone" required />
                </b-form-group>

                <b-form-group label-cols-sm="2" label="个人简介:">
                  <b-form-textarea v-model="form.info" rows="3" max-rows="6" />
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
        .put("profile", {
          email: this.form.email,
          name: this.form.name,
          phone: this.form.phone,
          info: this.form.info,
          avatar: this.imageUrl
        })
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.$message({
              type: "success",
              message: "修改成功"
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
    },
    getProfile(userId) {
      this.$axios
        .get("profile")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            let user = res.data.data;
            this.form = {
              email: user.email,
              name: user.name,
              phone: user.phone,
              info: user.info,
              avatar: user.avatar
            };
            this.imageUrl = user.avatar;
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    getQiniuToken() {
      this.$axios
        .get("auth/qiniu")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.postData = {
              token: res.data.data["token"]
            };
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    handleAvatarSuccess(res, file) {
      this.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
    },
    beforeAvatarUpload(file) {
      // const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;

      // if (!isJPG) {
      //   this.$message.error("上传头像图片只能是 JPG 格式!");
      // }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      return isLt2M;
    }
  },
  created() {
    const userId = this.$store.state.user.id;
    this.getProfile(userId);
    this.getQiniuToken();
  }
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