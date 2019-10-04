<template>
  <el-container>
    <my-header />
    <b-container>
      <div class="movie-detail">
        <b-row>
          <b-col cols="4">
            <b-list-group>
              <b-list-group-item>
                <router-link :to="{name: 'profile'}">会员中心</router-link>
              </b-list-group-item>
              <b-list-group-item>
                <router-link :to="{name: 'password-modify'}">修改密码</router-link>
              </b-list-group-item>
              <b-list-group-item>评论记录</b-list-group-item>
              <b-list-group-item>登录日志</b-list-group-item>
              <b-list-group-item variant="info">
                <router-link :to="{name: 'movie-collections'}">电影收藏</router-link>
              </b-list-group-item>
            </b-list-group>
          </b-col>

          <b-col cols="8">
            <div class="profile-form">
              <el-table :data="tableData" style="width: 100%">
                <el-table-column prop="date" label="海报" width="120">
                  <template slot-scope="scope">
                    <router-link :to="{name: 'movie-detail', params:{movieId:scope.row.id}}">
                      <b-img
                        thumbnail
                        fluid
                        :src="scope.row.imageLink"
                        alt="Logo"
                        style="width: 100px;height: 100px"
                      />
                    </router-link>
                  </template>
                </el-table-column>
                <el-table-column prop="name" label="名称" width="160">
                  <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                      <router-link :to="{name: 'movie-detail', params:{movieId:scope.row.id}}">
                        <el-tag size="medium">{{ scope.row.title }}</el-tag>
                      </router-link>
                    </div>
                  </template>
                </el-table-column>
                <el-table-column prop="address" label="简介">
                  <template slot-scope="scope">
                    <div slot="reference" class="name-wrapper">
                      <p>{{ scope.row.info.substring(0, 80) + "..." }}</p>
                    </div>
                  </template>
                </el-table-column>

                <el-table-column label="创建日期" width="180">
                  <template slot-scope="scope">
                    <i class="el-icon-time"></i>
                    <span style="margin-left: 10px">{{ scope.row.addtime }}</span>
                  </template>
                </el-table-column>
              </el-table>
            </div>
          </b-col>
        </b-row>
      </div>
    </b-container>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import MyHeader from "@/components/Header.vue";
import MFooter from "@/components/Footer.vue";
export default {
  props: {
    movieId: String
  },
  components: {
    MyHeader,
    MFooter
  },
  data() {
    return {
      tableData: [],
      imageUrl: "",
      postData: {
        token: ""
      }
    };
  },
  methods: {
    getMovieCollections() {
      this.$axios
        .get("profile/moviecols")
        .then(res => {
          console.log(res);
          if (res.status == 200 && res.data.code == 0) {
            this.tableData = res.data.data;
          }
        })
        .catch(err => {});
    }
  },
  created() {
    this.getMovieCollections();
  }
};
</script>

<style>
.el-header,
.el-footer {
  text-align: center;
  line-height: 60px;
}

.movie-detail {
  margin-top: 20px;
}

.profile-form {
  text-align: right;
}
.avatar {
  margin-right: 80%;
}
.btn {
  margin-left: 20px;
  padding-left: 20px;
  padding-right: 20px;
}
</style>