<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-button :plain="true" v-show="false">成功</el-button>
        <preview-dialog :dialog="dialog" :previewForm="previewForm" />
        <el-main>
          <el-form :inline="true" ref="add_data" class>
            <el-form-item class="btnRight">
              <el-button type="primary" size="small" icon="view" @click="handleAdd()">添加</el-button>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="预告名称" width="180" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.title }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="创建日期" width="240">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.addtime }}</span>
              </template>
            </el-table-column>

            <el-table-column label="图片链接" width="240" align="center">
              <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.url }}</span>
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
        title: ""
      },
      previewForm: {}
    };
  },
  methods: {
    handleAdd() {
      this.dialog.show = true;
      this.dialog.title = "添加预告";
    },
    handleEdit(index, row) {
      this.dialog = {
        show: true,
        title: "编辑预告"
      };
      this.previewForm = {
        title: row.title
      };
    },
    handleDelete(index, row) {
      this.$axios
        .delete("admin/preview/" + row.id)
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            console.log("删除成功");
          }
        })
        .catch(err => {});
    },
    getPreviewList() {
      // 获取表格数据
      this.$axios
        .get("admin/preview/list")
        .then(res => {
          console.log(res);
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
</style>