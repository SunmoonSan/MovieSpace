<template>
  <div class="preview-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form :model="previewForm" :rules="rules" ref="previewForm" label-width="100px">
        <el-form-item label="预告名称" prop="title">
          <el-input v-model="previewForm.title"></el-input>
        </el-form-item>
        <div class="preview-logo">
          <p class="preview-title">
            <i class="el-icon-upload"></i>预告海报
          </p>
          <el-upload
            class="avatar-uploader"
            action="http://up-z2.qiniup.com"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
            :data="postData"
          >
            <img v-if="previewForm.imageUrl" :src="previewForm.imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </div>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog.show = false">取 消</el-button>
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
    previewForm: Object
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
        token:
          "ux4DxWb-TJNjReQH6Nms_fPADLkBh4P4dIfg3dgY:IxJ_wlxqMwFszApNNpTnqBtBWbE=:eyJzY29wZSI6Im1vdmllc3BhY2UwMDEiLCJkZWFkbGluZSI6MTU2OTAzMTM0M30="
      }
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          if (this.dialog.option == "edit") {
            this.$axios
              .put("admin/preview/" + this.previewForm.id, {
                title: this.previewForm.title,
                logoLink: this.previewForm.imageUrl
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "预告编辑成功",
                    type: "success"
                  });
                  this.$emit("update");
                } else {
                  console.log("编辑失败");
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
            this.$axios
              .post("admin/preview/list", {
                title: this.previewForm.title,
                logoLink: this.imageUrl
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "预告添加成功",
                    type: "success"
                  });
                  this.$emit("update");
                } else {
                  console.log("添加失败");
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
    handleAvatarSuccess(res, file) {
      console.log(res);
      // this.imageUrl = URL.createObjectURL(file.raw);
      this.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
      this.previewForm.imageUrl = "http://py32746gy.bkt.clouddn.com/" + res.key;
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
      // return isJPG && isLt2M;
      return isLt2M;
    }
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
