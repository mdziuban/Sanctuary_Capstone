<template>
  <div class="container">
      <h1>{{ UserData.username }}</h1>  

    <form v-on:submit.prevent="UpdateProfile">
          <div class="form-group">
            <label>Username</label>
            <input type="text" name="username" id="user" v-model="username" class="form-control" :placeholder="UserData.username">
          </div>
          <div class="form-group">
              <label>Email</label>
            <input type="email" name="email" id="email" v-model="email" class="form-control" :placeholder="UserData.email">
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
          <button type="submit" class="btn btn-lg btn-primary btn-block">Update</button>
          </div>
        </form>


        <form v-on:submit.prevent="UpdateBio">
          <div class="form-group">
              <label>Bio</label>
            <input type="text" name="bio" id="bio" v-model="bio" class="form-control" :placeholder="UserData.player.bio">
          </div>
          <div class="form-group">
          <button type="submit" class="btn btn-lg btn-primary btn-block">Update Bio</button>
          </div>
        </form>

              <label>Profile Picture</label>
              <img :src="UserData.player.profilePic" class="img-thumbnail" alt="Profil Pic">
            <input type="file" @change='OnFileSelected'>
            <button @click="UploadImage" class="btn btn-success">Change Profile Picture</button>
    </div>
</template>

<script>
import { mapState } from "vuex";
import { getAPI } from '../axios-api'
export default {
  data() {
    return {
        username: this.$store.state.UserData.username,
        email: this.$store.state.UserData.email,
        first_name: this.$store.state.UserData.first_name,
        last_name: this.$store.state.UserData.last_name,
        bio: this.$store.state.UserData.player.bio,
        selectedImage: null,
    };
  },
  computed: mapState(["UserData", "AdditionalData"]),
  methods: {
    getUser() {
      getAPI.get("/player/", {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).then((response) => this.additionalData = response.data[0])
    },
    OnFileSelected(event) {
      this.selectedImage = event.target.files[0]
    },
    UploadImage(){
      let bodyParameters = new FormData()
      bodyParameters.append('profilePic', this.selectedImage, this.selectedImage.name)
      getAPI.patch("/update/" + this.$store.state.UserData.id, bodyParameters, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).catch(error => { console.log(error.response.data) })
    },
    UpdateBio(){
      let bodyParameters = new FormData()
      bodyParameters.append('bio', this.bio)
      getAPI.patch("/update/" + this.$store.state.UserData.id, bodyParameters, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).then(() => 
          this.$router.push({ name: 'posts' }))
    },
    UpdateProfile(){
      let bodyParameters = new FormData()
      bodyParameters.append('first_name', this.first_name)
      bodyParameters.append('last_name', this.last_name)
      bodyParameters.append('email', this.email)
      bodyParameters.append('username', this.username)
      getAPI.patch("/player/" + this.$store.state.UserData.id, bodyParameters, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).then(() => 
          this.$router.push({ name: 'posts' }))
    }
  },
  created() {
      this.getUser()
  }
};
</script>