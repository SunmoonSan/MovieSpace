<template>
  <div class="preview-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form :model="roleForm" :rules="rules" ref="roleForm" label-width="100px">
        <el-form-item label="角色名称" prop="name">
          <el-col :span="16">
            <el-input v-model="roleForm.name"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="权限列表" prop="tag">
          <el-col :span="16">
            <el-select
              v-model="roleForm.authList"
              multiple
              name="test"
              filterable
              placeholder="请选择权限"
              @change="change"
              :span="12"
            >
              <el-option
                v-for="auth in authList"
                :key="auth.value"
                :label="auth.label"
                :value="auth.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="onCancel()">取 消</el-button>
        <el-button type="primary" @click="onSubmit('roleForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    dialog: Object,
    roleForm: Object
  },
  data() {
    return {
      rules: {
        tiele: [
          { required: true, message: "请输入标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      },
      authList: []
    };
  },
  methods: {
    onCancel() {
      this.dialog.show = false;
      this.roleForm.authList = [];
    },
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          if (this.dialog.option == "edit") {
            this.$axios
              .put("admin/auth/" + this.roleForm.id, {
                name: this.roleForm.name,
                authList: this.roleForm.authList
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
            // 添加角色
            console.log("添加角色");
            this.$axios
              .post("admin/role/list", {
                name: this.roleForm.name,
                authList: this.roleForm.authList
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "角色添加成功",
                    type: "success"
                  });
                  this.$emit("update");
                }
              })
              .catch(err => {
                console.error(err);
              });
          }
        }
      });
    },
    change() {
      console.log(".......");
      console.log(this.roleForm.authList);
    },
    getAuthList() {
      this.$axios
        .get("admin/auth/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            let authList = res.data.data;
            for (let i = 0; i < authList.length; i++) {
              this.authList.push({
                value: authList[i].id,
                label: authList[i].name,
                disabled: true
              });
            }
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  created() {
    this.getAuthList();
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
