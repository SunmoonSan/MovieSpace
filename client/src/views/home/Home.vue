<template>
  <b-container fluid class="bv-example-row">
    <b-row>
      <b-col>
        <home-header />
      </b-col>
    </b-row>

    <b-row>
      <b-col>
        <el-carousel :interval="4000" type="card" height="360px">
          <el-carousel-item v-for="url in urls" :key="url">
            <el-image :src="url"></el-image>
          </el-carousel-item>
        </el-carousel>
      </b-col>
    </b-row>

    <div class="movie-grid">
      <b-row v-for="(movies,index) of movieList" :key="index">
        <b-col v-for="movie in movies" :key="movie.id">
          <router-link :to="{name: 'movie-detail', params:{movieId:movie.id}}">
            <b-card
              no-body
              class="overflow-hidden"
              style="max-width: 300px; max-height: 200px;"
              :key="movie.id"
            >
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img :src="movie.imageLink" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body :title="movie.title">
                    <b-card-text>{{ movie.info.substring(0, 88) + "..." }}</b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </router-link>
        </b-col>
      </b-row>
    </div>

    <b-row></b-row>
  </b-container>
</template>

<script>
// @ is an alias to /src
import HomeHeader from "@/components/Header.vue";
import HomeFooter from "@/components/Footer.vue";

export default {
  components: {
    HomeHeader,
    HomeFooter
  },
  data() {
    return {
      urls: [],
      movieList: [],
      // 传递到MovieDetail
      show: false
    };
  },
  methods: {
    getPreviewList() {
      this.$axios
        .get("preview/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            res.data.data.forEach(preview => {
              this.urls.push(preview.url);
            });
          }
        })
        .catch(err => {
          console.error(err);
        });
    },
    getMovieList() {
      this.$axios
        .get("movie/list")
        .then(res => {
          if (res.status == 200 && res.data.code == 0) {
            let movies = [];
            res.data.data.forEach(element => {
              movies.push({
                id: element.id,
                title: element.title,
                imageLink: element.imageLink,
                videoLink: element.videoLink,
                info: element.info
              });
              if (movies.length == 4) {
                this.movieList.push(movies);
                movies = [];
              }
            });
            if (movies.length != 0) {
              this.movieList.push(movies);
            }
            console.log(this.movieList);
          }
        })
        .catch(err => {
          console.error(err);
        });
    }
  },

  created() {
    this.getPreviewList();
    this.getMovieList();
  }
};
</script>

<style>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}

/* 轮播图 */
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.movie-grid {
  padding-left: 50px;
  padding-right: 50px;
}

/* .movie-grid >>> .card {
  padding: 0px;
} */

.card-title {
  font-size: 1px;
  margin-bottom: 0px;
}
.card-text {
  font-size: 0.5px;
  text-align: left;
}

.card-body {
  padding-left: 6px;
  padding-right: 1px;
  margin-top: -30px;
}
.card-img {
  margin-top: -10px;
  margin-left: -20px;
}
p {
  margin-top: 5px;
}
</style>