<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-button :plain="true" v-show="false">成功</el-button>
        <tag-dialog :dialog="dialog" :tagData="tagData" @update="getTagList" />
        <el-main>
          <el-form :inline="true" ref="add_data" class>
            <el-form-item class="btnRight">
              <el-button type="primary" size="small" icon="view" @click="handleAdd()">添加</el-button>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="标签名称" width="180" align="center">
              <template slot-scope="scope">
                <el-popover trigger="hover" placement="top">
                  <p>姓名: {{ scope.row.name }}</p>
                  <div slot="reference" class="name-wrapper">
                    <el-tag size="medium">{{ scope.row.name }}</el-tag>
                  </div>
                </el-popover>
              </template>
            </el-table-column>

            <el-table-column label="创建日期" width="240">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.addtime }}</span>
              </template>
            </el-table-column>

            <el-table-column label="操作">
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
          <div class="pagination">
            <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page.sync="pagination.page_index"
              :page-sizes="pagination.page_sizes"
              :page-size="pagination.page_size"
              :layout="pagination.layout"
              :total="pagination.total"
            ></el-pagination>
          </div>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import AdminHeader from "@/components/AdminHeader.vue";
import TreeMenu from "@/components/TreeMenu.vue";
import TagDialog from "@/components/TagDialog";
export default {
  components: {
    AdminHeader,
    TreeMenu,
    TagDialog
  },
  data() {
    return {
      pagination: {
        page_index: 2,
        total: 100,
        page_size: 5,
        page_sizes: [5, 10, 15, 20],
        layout: "total, sizes, prev, pager, next, jumper"
      },
      tableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit"
      },
      tagData: {}
    };
  },
  methods: {
    handleAdd() {
      this.dialog.show = true;
      this.dialog.title = "添加";
      this.dialog.option = "add";
      this.tagData = {
        name: ""
      };
    },
    handleEdit(index, row) {
      this.dialog.show = true;
      this.dialog.title = "编辑";
      this.dialog.option = "edit";
      this.tagData = {
        id: row.id,
        name: row.name
      };
    },
    handleDelete(index, row) {
      this.$axios
        .delete("admin/tag/" + row.id)
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.getTagList();
            this.$message({
              message: "标签删除成功",
              type: "success"
            });
          } else {
            console.error(res.data.msg);
            this.$message({
              message: "标签删除失败",
              type: "error"
            });
          }
        })
        .catch(res => {});
    },

    handleSizeChange(page_size) {
      console.log(page_size);
    },
    handleCurrentChange(page) {
      console.log("size" + page);
    },
    getTagList() {
      // 获取表格数据
      this.$axios
        .get("admin/tag/list")
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
    this.getTagList();
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