<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <el-main>
          <el-table :data="tableData">
            <el-table-column type="index" :span="6"></el-table-column>
            <el-table-column label="登录IP" align="center" :span="6">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.ip }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="登录用户名" align="left" :span="6">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.admin.name }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="登录时间" :span="6">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span>{{ scope.row.addtime }}</span>
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
export default {
  components: {
    AdminHeader,
    TreeMenu
  },
  data() {
    return {
      tableData: []
    };
  },
  methods: {
    getLogList() {
      // 获取表格数据
      this.$axios
        .get("admin/log/admin")
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
    this.getLogList();
  }
};
</script>

<style scoped>
.btnRight {
  float: right;
}
</style>