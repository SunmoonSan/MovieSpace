<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-button :plain="true" v-show="false">成功</el-button>
        <preview-dialog :dialog="dialog" :previewData="previewData" @update="getPreviewList" />
        <el-main>
          <el-form :inline="true" ref="add_data" class>
            <el-form-item class="btnRight">
              <el-button type="primary" size="small" icon="view" @click="handleAdd()">添加</el-button>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="预告名称" width="160" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.title }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="创建日期" width="180">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.addtime }}</span>
              </template>
            </el-table-column>

            <!-- <el-table-column label="海报链接" width="500" align="center">
              <template slot-scope="scope">
                <span style="margin-left: 10px">
                  <a v-bind:href="scope.row.url">{{ scope.row.title }}</a>
                </span>
              </template>
            </el-table-column>-->

            <el-table-column label="海报" width="160" height="120" align="center">
              <template slot-scope="scope">
                <el-image
                  style="width: 120px; height: 120px"
                  :src="scope.row.url"
                >{{ scope.row.url }}</el-image>
              </template>
            </el-table-column>

            <el-table-column label="操作" align="center">
              <template slot-scope="scope">
                <el-button
                  size="small"
                  type="warning"
                  @click="handleEdit(scope.$index, scope.row)"
                >编辑</el-button>
                <el-button
                  size="small"
                  type="danger"
                  @click="handleDelete(scope.$index, scope.row)"
                >删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import AdminHeader from "@/components/AdminHeader.vue";
import TreeMenu from "@/components/TreeMenu.vue";
import PreviewDialog from "@/components/PreviewDialog.vue";
export default {
  components: {
    AdminHeader,
    TreeMenu,
    PreviewDialog
  },
  data() {
    return {
      tableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit",
        hidden: false
      },
      previewData: {}
    };
  },
  methods: {
    handleAdd() {
      this.dialog.show = true;
      this.dialog.title = "添加预告";
      this.dialog.option = "add";
      this.previewData = {
        title: "",
        imageUrl: ""
      };
    },
    handleEdit(index, row) {
      this.dialog = {
        show: true,
        title: "编辑预告",
        option: "edit"
      };
      this.previewData = {
        id: row.id,
        title: row.title,
        imageUrl: row.url
      };
    },
    handleDelete(index, row) {
      this.$axios
        .delete("admin/preview/" + row.id)
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.$message({
              message: "预告删除成功",
              type: "success"
            });
            this.$$emit("update");
          }
        })
        .catch(err => {});
    },
    getPreviewList() {
      // 获取表格数据
      this.$axios
        .get("admin/preview/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.tableData = res.data.data;
          } else {
            this.tableData = [];
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  created: function() {
    this.getPreviewList();
  }
};
</script>

<style scoped>
.btnRight {
  float: right;
}

.el-form-item {
  margin-bottom: 2px;
}

.el-main {
  line-height: 0px;
}
</style>