<template>
  <el-container>
    <el-header>Header</el-header>
    <el-container>
      <el-aside width="200px">
        <tree-menu />
      </el-aside>
      <el-container>
        <movie-dialog :dialog="dialog" :movieData="movieData" @update="getMovieList" />
        <el-main>
          <el-button
            class="btnRight"
            type="primary"
            size="medium"
            icon="el-icon-plus"
            @click="handleAdd()"
          >添加</el-button>

          <el-table :data="tableData" style="width: 100%;">
            <el-table-column label="电影名称" width="160" align="center">
              <template slot-scope="scope">
                <div slot="reference" class="name-wrapper">
                  <el-tag size="medium">{{ scope.row.title }}</el-tag>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="电影时长" width="100">
              <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.length }}</span>分钟
              </template>
            </el-table-column>

            <el-table-column label="电影简介" width="160">
              <template slot-scope="scope">
                <div class="movie-info-tip" style="width:200px">
                  <el-tooltip effect="dark" :content="scope.row.info" placement="top">
                    <span style="margin-left: 10px">{{ scope.row.info.substring(0, 20) + "..." }}</span>
                  </el-tooltip>
                </div>
              </template>
            </el-table-column>

            <el-table-column label="上映地区" width="100">
              <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.area }}</span>
              </template>
            </el-table-column>

            <el-table-column label="创建日期" width="180">
              <template slot-scope="scope">
                <i class="el-icon-time"></i>
                <span style="margin-left: 10px">{{ scope.row.addtime }}</span>
              </template>
            </el-table-column>

            <el-table-column label="电影海报" width="160" height="120" align="center">
              <template slot-scope="scope">
                <el-image style="width: 120px; height: 120px" :src="scope.row.imageLink"></el-image>
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
import MovieDialog from "@/components/MovieDialog.vue";
export default {
  components: {
    AdminHeader,
    TreeMenu,
    MovieDialog
  },
  data() {
    return {
      tableData: [],
      dialog: {
        show: false,
        title: "",
        option: "edit"
      },
      movieData: {}
    };
  },
  methods: {
    handleAdd() {
      this.dialog.show = true;
      this.dialog.title = "添加电影";
      this.dialog.option = "add";
      this.movieData = {
        imageUrl: "",
        videoUrl: ""
      };
    },
    handleEdit(index, row) {
      this.dialog = {
        show: true,
        title: "编辑电影",
        option: "edit"
      };
      this.movieData = {
        id: row.id,
        title: row.title,
        info: row.info,
        releaseData: row.releaseData,
        length: row.length,
        area: row.area,
        imageUrl: row.imageLink,
        videoUrl: row.videoLink
      };
    },
    handleDelete(index, row) {
      this.$axios
        .delete("admin/movie/" + row.id)
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.$message({
              message: "电影删除成功",
              type: "success"
            });
            this.getMovieList();
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    getMovieList() {
      // 获取表格数据
      this.$axios
        .get("admin/movie/list")
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
    this.getMovieList();
  }
};
</script>

<style scoped>
.el-main {
  line-height: 0px;
}
.el-form-item {
  margin-bottom: 0px;
}
.btnRight {
  float: right;
  margin-bottom: 10px;
}
</style>