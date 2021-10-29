<template>
  <div class="bg-dark text-light bg-gradient vh-100">
    <div class="container">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">
            Welcome to Sanctuary, Register to Continue.
          </h1>

          <p v-if="noMatch" style="color: red;">Passwords did not match.</p>
          <form v-on:submit.prevent="register">
            <div class="form-group my-3">
              <label for="user">Username</label>
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control"
                placeholder="Username"
              />
            </div>
            <div class="form-group my-3">
              <label for="pass1">Password</label>
              <input
                type="password"
                name="password1"
                id="pass1"
                v-model="password1"
                class="form-control"
                placeholder="Password"
              />
            </div>
            <div class="form-group my-3">
              <label for="pass2">Password Again</label>
              <input
                type="password"
                name="password2"
                id="pass2"
                v-model="password2"
                class="form-control"
                placeholder="Password Again"
              />
            </div>
            <div class="form-group my-3">
              <label for="email">Email</label>
              <input
                type="email"
                name="email"
                id="email"
                v-model="email"
                class="form-control"
                placeholder="Email"
              />
            </div>
            <div class="form-group my-3">
              <label for="first_name">First Name</label>
              <input
                type="text"
                name="first_name"
                id="first_name"
                v-model="first_name"
                class="form-control"
                placeholder="First Name"
              />
            </div>
            <div class="form-group my-3">
              <label for="last_name">Last Name</label>
              <input
                type="text"
                name="last_name"
                id="last_name"
                v-model="last_name"
                class="form-control"
                placeholder="Last Name"
              />
            </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";
export default {
  name: "register",
  data() {
    return {
      username: "",
      password1: "",
      password2: "",
      email: "",
      last_name: "",
      first_name: "",
      noMatch: false,
    };
  },
  methods: {
    checkIfMatch() {
      if (this.password1 === this.password2 && this.password1 != "") {
        console.log("passwords matched");
        return
      } else {
        console.log("no match for passwords");
        this.noMatch = true;
        return false;
      }
    },
    register() {
      this.checkIfMatch();
      const bodyParameters = {
        username: this.username,
        password: this.password1,
        email: this.email,
        last_name: this.last_name,
        first_name: this.first_name,
      };
      getAPI
        .post("/register/", bodyParameters)
        .then(() => this.$router.push({ name: "login" }));
    },
  },
};
</script>