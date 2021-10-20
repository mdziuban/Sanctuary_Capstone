<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Welcome, {{ this.$store.state.username.username }}</a>
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
        <ul class="navbar-nav">
            <li class="nav-item" v-if="accessToken!=null">
              <router-link :to = "{ name: 'logout' }" class="btn btn-success">Logout</router-link>
            </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: "Navbar",
  computed: mapState(['accessToken'])
}
</script>