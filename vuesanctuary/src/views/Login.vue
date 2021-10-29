<template>
  <div class="row">
    <div class="col-sm-6">
      <img :src="SiteImages.image" class="w-100" alt="Waterfall" />
    </div>
    <div class="col-sm-6">
      <div class="row h-50 d-flex justify-content-center align-items-center">
        <div class="row mb-3">
          <h1 class="text-center my-3">Welcome to Sanctuary</h1>
        </div>
        <h4 v-if="incorrectAuth">
          The username or password you entered was incorrect.
        </h4>
        <form v-on:submit.prevent="login()">
          <div class="row mb-3">
            <div class="col-sm-10">
              <input
                type="text"
                name="username"
                class="form-control"
                id="user"
                v-model="username"
                placeholder="Username"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-sm-10">
              <input
                type="password"
                name="password"
                class="form-control"
                id="pass"
                v-model="password"
                placeholder="Password"
              />
            </div>
          </div>
          <div class="col-sm-10 d-grid mb-3">
            <input type="submit" class="btn btn-primary btn-lg" value="Login" />
          </div>
        </form>
        <div class="row h-50 d-flex justify-content-center align-items-center">
          <div class="row mb-3">
            <div class="col-sm-10 d-grid mb-3">
              <router-link
                :to="{ name: 'register' }"
                class="btn btn-outline-secondary btn-lg"
                >Register</router-link
              >
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { getAPI } from "../axios-api";

export default {
  name: "login",
  data() {
    return {
      username: "",
      password: "",
      incorrect: false,
    };
  },
  computed: mapState(["SiteImages"]),
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          this.$router.push({ name: "posts" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrect = true;
        });
    },
    GetImages() {
      getAPI
        .get("/images/")
        .then((response) => (this.$store.state.SiteImages = response.data[0]));
    },
  },
  created() {
    this.GetImages();
  },
};
</script>