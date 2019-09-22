<template>
  <div class="preview-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form :model="authForm" :rules="rules" ref="authForm" label-width="100px">
        <el-form-item label="权限名称" prop="name">
          <el-input v-model="authForm.name"></el-input>
        </el-form-item>
        <el-form-item label="权限路由" prop="url">
          <el-input v-model="authForm.url"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog.show = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit('authForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import * as qiniu from "qiniu-js";
export default {
  props: {
    dialog: Object,
    authForm: Object
  },
  data() {
    return {
      rules: {
        tiele: [
          { required: true, message: "请输入标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          if (this.dialog.option == "edit") {
            this.$axios
              .put("admin/auth/" + this.authForm.id, {
                name: this.authForm.name,
                url: this.authForm.url
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "权限编辑成功",
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
            // 添加权限
            this.$axios
              .post("admin/auth/list", {
                name: this.authForm.name,
                url: this.authForm.url
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
