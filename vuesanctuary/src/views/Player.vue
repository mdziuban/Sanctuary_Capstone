<template>
  <div v-if="dataLoaded" class="bg-dark text-light Min100">
    <Navbar></Navbar>
    <div class="container">
      <h1 class="p-3 my-1">{{ dataLoad.username }}</h1>
      <div class="row">
        <div class="col-6">
          <form v-on:submit.prevent="UpdateProfile">
            <div class="form-group">
              <label>Username</label>
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control my-1"
                :placeholder="dataLoad.username"
              />
            </div>
            <div class="form-group">
              <label>Email</label>
              <input
                type="email"
                name="email"
                id="email"
                v-model="email"
                class="form-control my-1"
                :placeholder="dataLoad.email"
              />
            </div>
            <div class="form-group">
              <label>First Name</label>
              <input
                type="text"
                name="first_name"
                id="first_name"
                v-model="first_name"
                class="form-control my-1"
                :placeholder="dataLoad.first_name"
              />
            </div>
            <div class="form-group">
              <label>Last Name</label>
              <input
                type="text"
                name="last_name"
                id="last_name"
                v-model="last_name"
                class="form-control my-1"
                :placeholder="dataLoad.last_name"
              />
            </div>
            <div class="form-group">
              <button
                type="submit"
                class="btn btn-lg bg-dark bg-gradient text-light my-1"
              >
                Update
              </button>
            </div>
          </form>
        </div>
        <div class="col-6">
          <form v-on:submit.prevent="UpdateBio">
            <div class="form-group">
              <label class="my-1">Bio</label>
              <textarea
                name="bio"
                rows="4"
                id="bio"
                v-model="bio"
                class="form-control my-1"
                :placeholder="dataLoad.player.bio"
              ></textarea>
            </div>
            <div class="form-group">
              <button
                type="submit"
                class="btn btn-lg btn-dark bg-gradient my-1"
              >
                Update Bio
              </button>
            </div>
          </form>
        </div>
      </div>
      <div class="row">
        <h2 class="my-3">Profile Picture</h2>
        <img
          :src="dataLoad.player.profilePic"
          class="img-thumbnail col-6"
          alt="Profil Pic"
        />
        <div class="col-6">
          <input type="file" @change="OnFileSelected" />
          <button
            @click="UploadImage"
            class="btn btn-lg btn-dark bg-gradient my-2 "
          >
            Change Profile Picture
          </button>
          <div class="align-items-end justify-content-center d-flex h-50">
          <router-link :to="{ name:'posts' }" class="btn btn-lg btn-dark bg-gradient my-2">Return to Posts</router-link>
        </div>
        </div>
      </div>
    </div>
  <footer></footer>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { mapState } from "vuex";
import { getAPI } from "../axios-api";
export default {
  components: { Navbar },
  data() {
    return {
      dataLoad: {},
      username: null,
      email: null,
      first_name: null,
      last_name: null,
      bio: null,
      selectedImage: null,
      dataLoaded: false,
    };
  },
  computed: mapState(["UserData"]),
  methods: {
    getUser() {
      getAPI
        .get("/player/", {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
          params: { username:  this.$store.state.username.username},
        })
        .then((response) => {
          this.dataLoad = response.data[0];
          this.dataLoaded = true;
          this.valdiateData();
        });
    },
    OnFileSelected(event) {
      this.selectedImage = event.target.files[0];
    },
    UploadImage() {
      let bodyParameters = new FormData();
      bodyParameters.append(
        "profilePic",
        this.selectedImage,
        this.selectedImage.name
      );
      getAPI
        .patch("/update/" + this.dataLoad.id, bodyParameters, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then(() => this.$router.go())
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    UpdateBio() {
      console.log(this.first_name)
      let bodyParameters = new FormData();
      bodyParameters.append("bio", this.bio);
      getAPI
        .patch("/update/" + this.dataLoad.id, bodyParameters, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then(() => this.$router.go())
    },
    UpdateProfile() {
      let bodyParameters = new FormData();
      bodyParameters.append("first_name", this.first_name);
      bodyParameters.append("last_name", this.last_name);
      bodyParameters.append("email", this.email);
      bodyParameters.append("username", this.username);
      getAPI
        .patch("/player/" + this.dataLoad.id, bodyParameters, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then(() => this.$router.go())
    },
    valdiateData() {
      this.username= this.dataLoad.username
      this.email= this.dataLoad.email
      this.first_name = this.dataLoad.first_name
      this.last_name = this.dataLoad.last_name
      this.bio = this.dataLoad.player.bio
    }
  },
  created() {
    this.getUser();
  },
};
</script>

<style>
.Min100 {
  min-height: 100vh;
}

</style>