<template>
<body>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Unity WebGL Player | Farm Kit</title>
    <link rel="shortcut icon" href="../../../public/TemplateData/favicon.ico">
    <link rel="stylesheet" href="../static/unity/TemplateData/style.css">
  </head>
  <nav class="navbar navbar-expand-lg navbar-light bg-gradient" style="background-color: #404c24">
    <div class="container-fluid">
      <router-link :to="{ name:'posts' }" class="navbar-brand text-light">Welcome, {{ this.$store.state.username.username }}</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav" v-if="accessToken!=null">
            <li class="nav-item" >
              <router-link :to = "{ name: 'logout' }" class="btn btn-outline-dark text-light">Logout</router-link>
            </li>
            <li class="nav-item">
              <a href="http://127.0.0.1:8000/playgame/" class="btn btn-outline-dark text-light mx-3">Play Game</a>
            </li>
        </ul>
      </div>
    </div>
  </nav>
</body>
</template>

<script>
import { mapState } from 'vuex'
import { getAPI } from "../axios-api";

export default {
  name: "Navbar",
  computed: mapState(['accessToken']),
  methods: {
    playGame() {
      getAPI.get('/playgame/', {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
    }
  }
}
</script>