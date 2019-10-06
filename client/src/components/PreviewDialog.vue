<template>
  <div class="preview-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form :model="previewData" :rules="rules" ref="previewForm" label-width="100px">
        <el-form-item label="预告名称" prop="title">
          <el-input v-model="previewData.title"></el-input>
        </el-form-item>
        <el-form-item label="预告海报">
          <el-upload
            class="upload-video"
            action="http://up-z2.qiniup.com"
            :show-file-list="false"
            :on-success="handleImageSuccess"
            :before-upload="beforeImageUpload"
            :data="postData"
          >
            <img v-if="previewData.imageUrl" :src="previewData.imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            <!-- <img v-else :src="previewForm.imageUrl" class="avatar" /> -->
          </el-upload>
        </el-form-item>

        <!-- <div class="preview-logo">
          <p class="preview-title">
            <i class="el-icon-upload"></i>预告海报
          </p>
          <el-upload
            class="avatar-uploader"
            action="http://up-z2.qiniup.com"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
            :data="postData"
          >
            <img v-if="previewData.imageUrl" :src="previewData.imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </div>-->
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="onCancel">取 消</el-button>
        <el-button type="primary" @click="onSubmit('previewForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import * as qiniu from "qiniu-js";
export default {
  props: {
    dialog: Object,
    previewData: Object
  },
  data() {
    return {
      rules: {
        tiele: [
          { required: true, message: "请输入标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      },
      postData: {
        token: ""
      }
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          let data = {
            title: this.previewData.title,
            logoLink: this.previewData.imageUrl
          };
          if (this.dialog.option == "edit") {
            this.$axios
              .put("admin/preview/" + this.previewData.id, data)
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "预告编辑成功",
                    type: "success"
                  });
                  this.$emit("update");
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
          } else {
            // 添加预告
            this.$axios
              .post("admin/preview/list", data)
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "预告添加成功",
                    type: "success"
                  });
                  this.$emit("update");
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
        }
      });
    },
    onCancel() {
      this.imageUrl = "";
      this.dialog.show = false;
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
    handleImageSuccess(res, file) {
      this.previewData.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
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
      return isLt2M;
    }
  },
  created() {
    this.getQiniuToken();
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
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.preview-title {
  font-size: 150%;
}
</style>
