<template>
  <b-navbar toggleable="lg" type="dark" class="custom-navbar">
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav class="navbar-nav">
        <b-nav-item :to="{ path: '/' }" exact>홈</b-nav-item>
        <b-nav-item :to="{ path: '/movies' }" exact>전체영화목록</b-nav-item>
        <b-nav-item :to="{ path: '/ranking' }" exact>추천 랭킹</b-nav-item>
        <b-nav-item :to="{ path: '/community' }" exact>자유게시판</b-nav-item>
        <b-nav-item :to="{ path: '/profile/' + username }" v-if="username" exact
          >나의 프로필</b-nav-item
        >
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      userData: "",
    };
  },
  computed: {
    userId() {
      return this.$store.state.userId;
    },
    username() {
      return this.$store.state.username;
    },
  },
};
</script>

<style scoped>
.custom-navbar {
  padding: 10px;
  background-color: rgb(83, 131, 234);
}

.navbar-nav {
  display: flex;
  align-items: center;
}

.nav-item {
  margin-right: 20px;
}

.nav-link {
  color: rgb(80, 76, 76);
  font-size: 25px;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

li.active {
  font-weight: bold;
  color: #fff;
}
</style>
