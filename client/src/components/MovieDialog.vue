<template>
  <div class="movie-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show" width="600px">
      <el-form :model="movieData" :rules="rules" ref="movieForm" label-width="100px">
        <el-form-item label="电影名称" prop="title">
          <el-col :span="20">
            <el-input v-model="movieData.title"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="海报">
          <el-upload
            class="upload-video"
            action="http://up-z2.qiniup.com"
            :show-file-list="false"
            :on-success="handleImageSuccess"
            :before-upload="beforeImageUpload"
            :data="postData"
          >
            <img v-if="movieData.imageUrl" :src="movieData.imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            <!-- <img v-else :src="previewForm.imageUrl" class="avatar" /> -->
          </el-upload>
        </el-form-item>

        <el-form-item label="影片">
          <el-upload
            class="upload-video"
            action="http://up-z2.qiniup.com"
            :on-success="handleVideoSuccess"
            :before-upload="beforeVideoUpload"
            :data="postData"
          >
            <i v-if="!movieData.videoUrl" class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
          <b-embed
            v-if="movieData.videoUrl"
            type="iframe"
            aspect="16by9"
            :src="movieData.videoUrl"
            allowfullscreen
          ></b-embed>
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-form-item>

        <el-form-item label="电影简介 :">
          <el-input type="textarea" :rows="5" placeholder="请输入内容" v-model="movieData.info"></el-input>
        </el-form-item>

        <el-form-item label="电影标签" prop="tag">
          <el-col :span="10">
            <el-select v-model="movieData.tag" placeholder="请选择电影标签">
              <el-option v-for="tag in tagList" :label="tag.label" :key="tag.id" :value="tag"></el-option>
            </el-select>
          </el-col>
        </el-form-item>

        <!-- <el-form-item label="电影星级">
          <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="textarea"></el-input>
        </el-form-item>-->

        <!-- <el-form-item label="电影星级" prop="region">
          <el-select v-model="ruleForm.region" placeholder="请选择活动区域">
            <el-option label="区域一" value="shanghai"></el-option>
            <el-option label="区域二" value="beijing"></el-option>
          </el-select>
        </el-form-item>-->

        <el-form-item label="电影时长" prop="length">
          <el-row>
            <el-col :span="10">
              <el-input v-model="movieData.length"></el-input>
            </el-col>
            <el-col :span="3">(分钟)</el-col>
          </el-row>
        </el-form-item>

        <el-form-item label="上映时间">
          <el-col :span="10">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="movieData.releaseDate"
              style="width: 100%;"
            ></el-date-picker>
          </el-col>
        </el-form-item>

        <el-form-item label="上映地区">
          <el-col :span="10">
            <el-input v-model="movieData.area"></el-input>
          </el-col>
        </el-form-item>
      </el-form>

      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog.show = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit('movieForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    dialog: Object,
    movieData: Object
  },
  data() {
    return {
      movieForm: {},
      tagList: [],

      title: "",

      rules: {},
      postData: {
        token: ""
      },
      videoUrl: ""
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          console.log(this.movieData);
          let data = {
            title: this.movieData.title,
            imageLink: this.movieData.imageUrl,
            videoLink: this.movieData.videoUrl,
            info: this.movieData.info,
            length: this.movieData.length,
            // tagId: this.movieData.tag.value,
            releaseDate: this.movieData.releaseDate,
            area: this.movieData.area
          };
          if (this.dialog.option == "add") {
            this.$axios
              .post("admin/movie/list", data)
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "电影添加成功",
                    type: "success"
                  });
                  this.$emit("update");
                }
              })
              .catch(err => {});
          } else {
            this.$axios
              .put("admin/movie/" + this.movieData.id, data)
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "电影修改成功",
                    type: "success"
                  });
                  this.$emit("update");
                }
              })
              .catch(err => {});
          }
        }
      });
    },
    getQiniuToken() {
      this.$axios
        .get("auth/qiniu")
        .then(res => {
          console.log(res);
          if (res.status == 200 && res.data.code == 0) {
            console.log("token", res.data.data["token"]);
            this.postData = {
              token: res.data.data["token"]
            };
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    handleImageSuccess(res, file) {
      // this.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
      this.movieData.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
    },
    beforeImageUpload(file) {
      // this.getQiniuToken();
      // const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 2;
      // if (!isJPG) {
      //   this.$message.error("上传头像图片只能是 JPG 格式!");
      // }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 2MB!");
      }
      // return isJPG && isLt2M;
      // this.imageUrl = "";
      return isLt2M;
    },
    handleVideoSuccess(res, file) {
      this.movieData.videoUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
    },
    beforeVideoUpload(file) {},
    getTagList() {
      this.$axios
        .get("admin/tag/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            let tags = res.data.data;
            for (let i = 0; i < tags.length; i++) {
              this.tagList.push({
                value: tags[i].id,
                label: tags[i].name
              });
            }
          } else {
            console.log(res);
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  created() {
    this.getTagList();
    this.getQiniuToken();
    this.title = this.movieData.title;
  }
};
</script>

<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 16px;
  color: #8c939d;
  width: 80px;
  height: 80px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 120px;
  height: 120px;
  display: block;
}
.el-icon-upload {
  font-size: 16px;
}
.movie-length {
  width: 100px;
}
.upload-video {
  width: 50%;
}
.el-upload-dragger {
  width: 200px;
}
</style>
