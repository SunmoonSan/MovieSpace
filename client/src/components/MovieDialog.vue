<template>
  <div class="movie-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show" width="600px">
      <el-form :model="movieForm" :rules="rules" ref="movieForm" label-width="100px">
        <el-form-item label="电影名称" prop="title">
          <el-col :span="20">
            <el-input v-model="movieForm.title"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="电影封面 :">
          <el-row>
            <el-row>
              <el-col :span="12">
                <i class="el-icon-upload" />上传封面
                <el-upload
                  class="avatar-uploader"
                  action="http://up-z2.qiniup.com"
                  :show-file-list="false"
                  :on-success="handleImageSuccess"
                  :before-upload="beforeImageUpload"
                  :data="postData"
                >
                  <!-- 从Movie列表跳转到对话框 -->
                  <img v-if="dialog.option==='add'" :src="movieForm.imageUrl" class="avatar" />
                  <img v-else-if="dialog.option==='edit'" :src="movieForm.imageUrl" class="avatar" />
                  <i v-else class="el-icon-plus avatar-uploader-icon"></i>

                  <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                </el-upload>
              </el-col>
              <el-col :span="12"></el-col>
            </el-row>
            <el-row>
              <el-col :span="6">
                <i class="el-icon-upload" />上传影片
              </el-col>
              <el-col :span="12">
                <el-upload
                  class="upload-video"
                  drag
                  action="http://up-z2.qiniup.com"
                  :on-success="handleVideoSuccess"
                  :before-upload="beforeVideoUpload"
                  :data="postData"
                >
                  <i class="el-icon-upload"></i>
                  <div class="el-upload__text">
                    将文件拖到此处，或
                    <em>点击上传</em>
                    <div class="el-upload__tip" slot="tip">只能上传mp4文件，且不超过500kb</div>
                  </div>
                </el-upload>
                <div>
                  <b-embed type="iframe" aspect="16by9" :src="videoUrl" allowfullscreen></b-embed>
                </div>
              </el-col>
            </el-row>
          </el-row>
        </el-form-item>

        <el-form-item label="电影简介 :">
          <el-input type="textarea" :rows="2" placeholder="请输入内容" v-model="movieForm.info"></el-input>
        </el-form-item>

        <el-form-item label="电影标签" prop="tag">
          <el-col :span="10">
            <el-select v-model="movieForm.tag" placeholder="请选择电影标签">
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
              <el-input v-model="movieForm.length"></el-input>
            </el-col>
            <el-col :span="3">(分钟)</el-col>
          </el-row>
        </el-form-item>

        <el-form-item label="上映时间">
          <el-col :span="10">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="movieForm.releaseDate"
              style="width: 100%;"
            ></el-date-picker>
          </el-col>
        </el-form-item>

        <el-form-item label="上映地区">
          <el-col :span="10">
            <el-input v-model="movieForm.area"></el-input>
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
import * as qiniu from "qiniu-js";
export default {
  props: {
    dialog: Object,
    movieForm: {
      imageUrl: ""
    }
  },
  data() {
    return {
      tagList: [],
      ruleForm: {
        region: "",
        tag: "",
        length: "",
        info: ""
      },
      // movieForm: {},
      rules: {},
      postData: {
        token:
          "ux4DxWb-TJNjReQH6Nms_fPADLkBh4P4dIfg3dgY:7JaKYhAxqL7fO9cvAIO0U7qr9uY=:eyJzY29wZSI6Im1vdmllc3BhY2UwMDEiLCJkZWFkbGluZSI6MTU2OTEyMzE2M30="
      },
      imageUrl: "",
      videoUrl: ""
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        console.log(valid);
        if (valid) {
          console.log(this.ruleForm.tag);
          this.$axios
            .post("admin/movie/list", {
              title: this.movieForm.title,
              logoLink: this.imageUrl,
              videoLink: this.videoUrl,
              info: this.movieForm.info,
              length: this.movieForm.length,
              tagId: this.movieForm.tag.value,
              releaseDate: this.movieForm.releaseDate,
              area: this.movieForm.area
            })
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
        }
      });
    },
    handleImageSuccess(res, file) {
      this.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
      this.movieForm.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
      console.log(this.movieForm);
    },
    beforeImageUpload(file) {
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
      this.videoUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
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
  created: function() {
    this.getTagList();
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
