<template>
  <div class="admin-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form :model="adminForm" :rules="rules" ref="adminForm" label-width="100px">
        <el-form-item label="管理员姓名" prop="name">
          <el-col :span="12">
            <el-input v-model="adminForm.name"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="密码" prop="password">
          <el-col :span="12">
            <el-input type="password" v-model="adminForm.password" autocomplete="off"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="确认密码" prop="checkPass">
          <el-col :span="12">
            <el-input type="password" v-model="adminForm.checkPwd" autocomplete="off"></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="所属角色" prop="tag">
          <el-col :span="12">
            <el-select
              v-model="adminForm.roleId"
              multiple
              filterable
              placeholder="请选择角色"
              style="width:287px;"
            >
              <el-option
                v-for="role in roleList"
                :key="role.value"
                :label="role.label"
                :value="role.value"
              ></el-option>
            </el-select>
          </el-col>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog.show = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit('adminForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    dialog: Object,
    adminForm: Object
  },
  data() {
    return {
      rules: {
        tiele: [
          { required: true, message: "请输入标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      },
      roleList: []
    };
  },
  methods: {
    onSubmit(formname) {
      this.$refs[formname].validate(valid => {
        if (valid) {
          console.log("....");
          // 添加管理员
          this.$axios
            .post("admin/admin/list", {
              name: this.adminForm.name,
              password: this.adminForm.password,
              roleId: this.adminForm.roleId
            })
            .then(res => {
              if (res.status == 200 && res.data.code == 0) {
                this.dialog.show = false;
                this.$message({
                  message: "管理员添加成功",
                  type: "success"
                });
                this.$emit("update");
              }
            })
            .catch(err => {
              console.error(err);
            });
        }
      });
    },
    getRoleList() {
      this.$axios
        .get("admin/role/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            let roleList = res.data.data;
            for (let i = 0; i < roleList.length; i++) {
              this.roleList.push({
                value: roleList[i].id,
                label: roleList[i].name
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
    this.getRoleList();
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
.admin-form {
  text-align: center;
}
</style>
