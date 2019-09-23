<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-button :plain="true" v-show="false">成功</el-button>
        <admin-dialog :dialog="dialog" :adminForm="adminForm" @update="getAdminList" />
        <el-main>
          <el-form :inline="true" ref="add_data" class>
            <el-form-item class="btnRight">
              <el-button type="primary" size="small" icon="view" @click="handleAdd">添加</el-button>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="管理员姓名" width="240" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.name }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="所属角色" width="240" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium" type="success">{{ scope.row.role.name }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="创建日期" width="180">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span>{{ scope.row.addtime }}</span>
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
import AdminDialog from "@/components/AdminDialog.vue";
export default {
  components: {
    AdminHeader,
    TreeMenu,
    AdminDialog
  },
  data() {
    return {
      tableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit"
      },
      adminForm: {}
    };
  },
  methods: {
    handleAdd() {
      this.dialog = {
        show: true,
        title: "添加管理员"
      };
    },
    handleEdit(index, row) {
      this.$notify({
        title: "警告",
        message: "不支持修改管理员",
        type: "warning"
      });
    },
    handleDelete(index, row) {
      this.$notify({
        title: "警告",
        message: "不支持删除管理员",
        type: "warning"
      });
    },
    getAdminList() {
      // 获取表格数据
      this.$axios
        .get("admin/admin/list")
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
    this.getAdminList();
  }
};
</script>

<style scoped>
.btnRight {
  float: right;
}
</style>