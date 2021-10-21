<template>
  <div class="container">
      <h1>{{ UserData.username }}</h1>
      <!-- <div>{{ UserData.id }}</div>
      <div>{{ UserData.username }}</div>
      <div>{{ UserData.first_name }}</div>
      <div>{{ UserData.last_name }}</div>
      <div>{{ UserData.email }}</div>
      <div>{{ additionalData.bio }}</div>
      <div>{{ additionalData.profilePic }}</div> -->
  

    <form v-on:submit.prevent="">
          <div class="form-group">
            <label>Username</label>
            <input type="text" name="username" id="user" v-model="username" class="form-control" :placeholder="UserData.username">
          </div>
          <div class="form-group">
              <label>Email</label>
            <input type="email" name="email" id="email" v-model="email" class="form-control" :placeholder="UserData.email">
          </div>
          <div class="form-group">
              <label>Bio</label>
            <input type="text" name="bio" id="bio" v-model="bio" class="form-control" :placeholder="additionalData.bio">
          </div>
          <div class="form-group">
              <label>First Name</label>
            <input type="text" name="first_name" id="first_name" v-model="first_name" class="form-control" :placeholder="UserData.first_name">
          </div>
          <div class="form-group">
              <label>Last Name</label>
            <input type="text" name="last_name" id="last_name" v-model="last_name" class="form-control" :placeholder="UserData.last_name">
          </div>
          <div class="form-group">
              <label>Profile Picture</label>
            <input type="text" name="profilePic" id="profilePic" v-model="profilePic" class="form-control" :placeholder="additionalData.profilePic">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Update</button>
        </form>
    </div>
</template>

<script>
import { mapState } from "vuex";
import { getAPI } from '../axios-api'
export default {
  data() {
    return {
        additionalData: {},
    };
  },
  computed: mapState(["UserData"]),
  methods: {
    getUser() {
      getAPI.get("/player/" + this.$store.state.UserData.id, {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).then((response) => this.additionalData = response.data[0])
    },
  },
  created() {
      this.getUser()
  }
};
</script>