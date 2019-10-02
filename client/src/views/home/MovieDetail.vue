<template>
  <el-container>
    <my-header />
    <b-container>
      <div class="movie-detail">
        <b-row>
          <b-col cols="8">
            <b-embed type="iframe" aspect="4by3" :src="videoLink" allowfullscreen></b-embed>
          </b-col>
          <b-col cols="4">
            <b-list-group>
              <b-list-group-item>
                <b-button variant="outline-info" @click="handelMovieCollect(movie.id)">
                  <i class="el-icon-star-off">收藏</i>
                </b-button>
              </b-list-group-item>
              <b-list-group-item>片名:{{movie.title}}</b-list-group-item>
              <!-- <b-list-group-item>标签</b-list-group-item> -->
              <b-list-group-item>片长: {{movie.length}}分钟</b-list-group-item>
              <b-list-group-item>上映地区: {{movie.area}}</b-list-group-item>
              <b-list-group-item>上映时间: {{movie.releaseTime}}</b-list-group-item>
              <b-list-group-item>播放量:</b-list-group-item>
              <b-list-group-item>评论量:</b-list-group-item>
              <b-list-group-item>影片简介: {{movie.info.substring(0, 120) + "..."}}</b-list-group-item>
            </b-list-group>
          </b-col>
        </b-row>
      </div>
      <div class="movie-comment">
        <div class="comment-input">
          发表评论
          <b-form-textarea
            id="textarea"
            v-model="comment"
            placeholder="吐槽一下. . ."
            rows="3"
            max-rows="6"
          ></b-form-textarea>
          <b-button block variant="primary" @click="handelSubmitComment(movie.id)">提交评论</b-button>
        </div>
        <div class="comment-list">
          <ul class="commentList" v-for="(comment, index) in commentList" :key="index">
            <li class="item cl">
              <!-- <a href="user.html">
                <i class="avatar size-L radius">
                  <img
                    alt="50x50"
                    src="holder.js/50x50"
                    class="img-circle"
                    style="border:1px solid #abcdef;"
                  />
                </i>
              </a>-->
              <el-row :gutter="24">
                <el-col :span="2">
                  <b-img
                    rounded="circle"
                    alt="Circle image"
                    style="width: 75px;height: 75px"
                    :src="comment.commentor.avatar"
                  ></b-img>
                </el-col>
                <el-col :span="22">
                  <div class="comment-main">
                    <header class="comment-header">
                      <div class="comment-meta">
                        <a class="comment-author">{{comment.commentor.name}}</a>
                        评论于{{comment.addtime}}
                      </div>
                    </header>
                    <div class="comment-body">
                      <p>{{comment.content}}</p>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>
        </div>
      </div>
    </b-container>
    <el-footer>Footer</el-footer>
  </el-container>
</template>

<script>
import MyHeader from "@/components/Header.vue";
import MFooter from "@/components/Footer.vue";
export default {
  components: {
    MyHeader,
    MFooter
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated;
    }
  },
  data() {
    return {
      movieId: "",

      title: "送我上青云",
      videoLink: "",
      comment: "",
      movie: {},

      // 电影评论列表
      commentList: []
    };
  },
  methods: {
    handelSubmitComment(movieId) {
      if (this.isAuthenticated) {
        this.$axios
          .post("movie/" + movieId + "/comment/list", {
            content: this.comment
          })
          .then(res => {
            if (res.status == 200 && res.data.code == 0) {
              this.$message.success("评论发表成功");
              this.getMovieCommentList(this.movieId);
            }
          })
          .catch(err => {
            console.error(err);
          });
      } else {
        this.$message.warning("请登录后再评论");
      }
    },
    getMovie(movieId) {
      this.$axios
        .get("movie/" + movieId)
        .then(res => {
          let movie = res.data.data;
          this.movie = {
            id: movie.id,
            title: movie.title,
            length: movie.length,
            area: movie.area,
            releaseTime: movie.releaseTime,
            info: movie.info
          };
          this.videoLink = res.data.data.videoLink;
        })
        .catch(err => {});
    },
    getMovieCommentList(movieId) {
      this.$axios
        .get("movie/" + movieId + "/comment/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            this.commentList = [];
            res.data.data.forEach(comment => {
              this.commentList.push({
                id: comment.id,
                content: comment.content,
                commentor: comment.commentUser,
                addtime: comment.addtime
              });
            });
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    handelMovieCollect(movieId) {
      console.log("收藏" + this.movie.id);
      this.$axios
        .post("movie/" + movieId + "/collect")
        .then(res => {
          this.$message({
            type: "success",
            message: "电影收藏成功"
          });
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  created() {
    this.movieId = this.$route.params.movieId;
    this.getMovie(this.movieId);
    this.getMovieCommentList(this.movieId);
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

.movie-comment {
  margin-top: 30px;
  margin-left: 10px;
}

.item {
  list-style: none outside none;
  margin-bottom: 6px;
  margin-right: 6px;
}

.btn {
  margin-left: 0px;
  padding-left: 20px;
  padding-right: 20px;
}

li {
  display: list-item;
  text-align: -webkit-match-parent;
}

/*comments*/
.commentList {
  padding-left: 6px;
}

.comment-main {
  position: relative;
  /* margin-left: 64px; */
  text-align: left;
  border: 1px solid #dedede;
  border-radius: 2px;
  box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.1);
}

.comment-main:before,
.comment-main:after {
  position: absolute;
  top: 11px;
  left: -16px;
  right: 100%;
  width: 0;
  height: 0;
  display: block;
  content: " ";
  border-color: transparent;
  border-style: solid solid outset;
  pointer-events: none;
}

.comment-main:before {
  border-right-color: #dedede;
  border-width: 8px;
}

.comment-main:after {
  border-width: 7px;
  border-right-color: #f8f8f8;
  margin-top: 1px;
  margin-left: 2px;
}

.comment-header {
  padding: 10px 15px;
  background: #f8f8f8;
  border-bottom: 1px solid #eee;
}

.comment-title {
  margin: 0 0 8px 0;
  font-size: 1.6rem;
  line-height: 1.2;
}

.comment-meta {
  font-size: 13px;
  color: #999;
  line-height: 1.2;
}

.comment-meta a {
  color: #999;
}

.comment-author {
  font-weight: 700;
  color: #999;
}

.comment-body {
  padding: 15px;
  overflow: hidden;
}

.comment-body > :last-child {
  margin-bottom: 0;
}

.commentList .comment-flip .avatar {
  float: right;
}

.comment-flip .comment-main {
  margin-left: 0;
  margin-right: 64px;
}

.comment-flip .comment-main:before {
  border-left-color: #dedede;
  border-right-color: transparent;
}

.comment-flip .comment-main:before,
.comment-flip .comment-main:after {
  left: 100%;
  position: absolute;
  right: -16px;
}

.comment-flip .comment-main:after {
  border-left-color: #f8f8f8;
  border-right-color: transparent;
  margin-left: auto;
  margin-right: 2px;
}

/*comments*/
</style>