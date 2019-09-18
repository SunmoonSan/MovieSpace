<template>
  <div class="m-header">
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <!--小屏幕导航按钮和logo-->
        <div class="navbar-header">
          <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a href="index.html" class="navbar-brand" style="height:40px;width:250px;">
            <!-- <img src="@/assets/base/images/logo.png" style="height:40px;weight:40px;" />微电影 -->
          </a>
        </div>
        <!--小屏幕导航按钮和logo-->
        <!--导航-->
        <div class="navbar-collapse collapse">
          <form class="navbar-form navbar-left" role="search" style="margin-top:18px;">
            <div class="form-group input-group">
              <input type="text" class="form-control" placeholder="请输入电影名！" />
              <span class="input-group-btn">
                <a class="btn btn-default" href="search.html">
                  <span class="glyphicon glyphicon-search"></span>&nbsp;搜索
                </a>
              </span>
            </div>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li>
              <a class="curlink" href="/">
                <span class="glyphicon glyphicon-film"></span>&nbsp;电影
              </a>
            </li>
            <li>
              <a class="curlink" href="/login">
                <span class="glyphicon glyphicon-log-in"></span>&nbsp;登录
              </a>
            </li>
            <li>
              <a class="curlink" href="/register">
                <span class="glyphicon glyphicon-plus"></span>&nbsp;注册
              </a>
            </li>
            <li>
              <a class="curlink" href="/logout">
                <span class="glyphicon glyphicon-log-out"></span>&nbsp;退出
              </a>
            </li>
            <li>
              <a class="curlink" href="/user">
                <span class="glyphicon glyphicon-user"></span>&nbsp;会员
              </a>
            </li>
          </ul>
        </div>
        <!--导航-->
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "Header"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->