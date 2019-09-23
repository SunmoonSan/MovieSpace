<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-button :plain="true" v-show="false">成功</el-button>
        <role-dialog :dialog="dialog" :roleForm="roleForm" @update="getRoleList" />
        <el-main>
          <el-form :inline="true" ref="add_data" class>
            <el-form-item class="btnRight">
              <el-button type="primary" size="small" icon="view" @click="handleAdd()">添加</el-button>
            </el-form-item>
          </el-form>
          <el-table :data="tableData" style="width: 100%">
            <el-table-column label="角色名称" width="240" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.name }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <!-- <el-table-column label="权限列表" width="320">
              <template slot-scope="scope">
                <span>{{ scope.row.authList }}</span>
              </template>
            </el-table-column>-->

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
import RoleDialog from "@/components/RoleDialog.vue";
export default {
  components: {
    AdminHeader,
    TreeMenu,
    RoleDialog
  },
  data() {
    return {
      tableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit"
      },
      roleForm: {
        authList: []
      }
    };
  },
  methods: {
    handleAdd() {
      this.dialog.show = true;
      this.dialog.title = "添加角色";
      this.dialog.option = "add";
      this.roleForm = {};
    },
    handleEdit(index, row) {
      let authIds = [];
      let authList = this.tableData[index]["authList"];
      for (let i = 0; i < authList.length; i++) {
        authIds.push(Number(authList[i]));
      }
      this.roleForm = {
        id: row.id,
        name: row.name,
        authList: authIds
      };

      this.dialog = {
        show: true,
        title: "编辑角色",
        option: "edit"
      };
    },
    handleDelete(index, row) {
      this.$axios
        .delete("admin/auth/" + row.id)
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.$message({
              message: "权限删除成功",
              type: "success"
            });
            this.getAuthList();
            this.authForm = {};
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    getRoleList() {
      // 获取表格数据
      this.$axios
        .get("admin/role/list")
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
    this.getRoleList();
  }
};
</script>

<style scoped>
.btnRight {
  float: right;
}
</style>