<template>
  <div class="tag-form">
    <el-button :plain="true" v-show="false">成功</el-button>
    <el-dialog :title="dialog.title" :visible.sync="dialog.show">
      <el-form
        :model="tagForm"
        :rules="rules"
        ref="tagForm"
        label-width="100px"
        class="demo-tagForm"
      >
        <el-form-item label="标签名称" prop="name">
          <el-input v-model="tagForm.name"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialog.show = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit('tagForm')">提 交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    dialog: Object,
    tagForm: Object
  },
  data() {
    return {
      rules: {
        name: [
          { required: true, message: "请输入标签名称", trigger: "blur" },
          { min: 2, max: 4, message: "长度在 2 到 4 个字符", trigger: "blur" }
        ]
      }
    };
  },
  methods: {
    onSubmit(formname) {
      console.log("提交");
      console.log(this.$refs["form"]);
      this.$refs[formname].validate(valid => {
        if (valid) {
          console.log(this.tagForm);
          if (this.dialog.option == "edit") {
            this.$axios
              .put("admin/tag/" + this.tagForm.id, {
                name: this.tagForm.name
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "标签编辑成功",
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
              .post("admin/tag/list", {
                name: this.tagForm.name
              })
              .then(res => {
                if (res.status == 200 && res.data.code == 0) {
                  this.dialog.show = false;
                  this.$message({
                    message: "标签添加成功",
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
          let url =
            "admin/tag/" +
            (this.dialog.option == "edit" ? this.tagForm.id : "list");
          console.log(url);
        }
      });
    }
  }
};
</script>
