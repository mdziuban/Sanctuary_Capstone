<template>
  <div class="posts">
    <Navbar></Navbar>
    <h1 class="text-center">The Sanctuary</h1>
    <article class="container" id="app">
      <div class="row">
        <div class="col-4">
          <router-link :to="{ name: 'playerDetails' }">

          <div style="position: fixed" class="col-3 border border-dark">
            <img :src="AdditionalData.profilePic" class="img-thumbnail" alt="Profil Pic">
            <h2 class="text-center">{{ this.$store.state.username.username }}</h2>
          </div>
          </router-link>
        </div>
        <div class="col-8 border border-dark">
          <div class="row">
            <input
              v-model="newPost.text_content"
              type="text"
              placeholder="New Post Content"
            />
            <!-- <input v-model="newPost.img_content" type='text' placeholder="New Img Content"> -->
            <button @click="postFeed()" class="btn btn-success">submit</button>
            <ul class="list-group">
              <li
                v-for="post in PostData"
                :key="post.id"
                class="list-group-item"
              >
                <h3>{{ post.username }}</h3>
                <p>{{ post.created }}</p>
                <p>{{ post.text_content }}</p>
                <!-- <img v-if="post.img_content" :src="'api/'+post.img_content"> -->
                <p>{{ post.hashtags }}</p>
                <input
                  v-model="post.content"
                  type="text"
                  placeholder="Reply"
                />
                <!-- <input v-model="replyPost.img_content" type="image"> -->
                <button
                  @click="replyToPost(post)"
                  class="btn btn-success mx-3"
                >
                  Reply
                </button>
                <p>
                  <button
                    class="btn btn-primary"
                    type="button"
                    @click="loadReplies(post.id)"
                  >
                    Show Replies
                  </button>
                </p>
                <div v-show="post.id === postReplyShow" class="card card-body reply">
                  <div v-for="reply in ReplyData" :key="reply.id">
                    <div class="card card-body">
                      <h4>{{ reply.username }}</h4>
                      <p>{{ reply.reply_created }}</p>
                      <p>{{ reply.text_content }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </article>
  </div>
</template>

<script>
import { getAPI } from "../axios-api";
import Navbar from "../components/Navbar.vue";
import { mapState } from "vuex";

export default {
  name: "Posts",
  data() {
    return {
      replies: [],
      postReplyShow: "",
      newPost: {},
      userData: {},
      replyPost: {},
      isHidden: false,
      replyContent: ''
    };
  },
  components: {
    Navbar,
  },
  computed: mapState(["PostData", "ReplyData", "UserData", "AdditionalData"]),
  methods: {
    loadFeed() {
      getAPI
        .get("/post/", {
          headers: {
            Authorization: `Bearer ${this.$store.state.accessToken}`,
          },
        })
        .then((response) => {
          this.$store.state.PostData = response.data;
        }).catch(err => 
        (console.log(err)));
    },
    postFeed() {
      let [hashWords, content] = this.splitByHashtag(this.newPost.text_content);
      const bodyParameters = {
        user: this.$store.state.UserData.id,
        text_content: content,
        //img_content: this.newPost.img_content,
        hashtags: hashWords,
      };
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        }
      };
      getAPI.post("/post/", bodyParameters, config)
      .then(() => this.loadFeed())
      .then(this.newPost.text_content = '');
    },
    replyToPost(post) {
      const bodyParameters = {
        user: this.$store.state.UserData.id,
        text_content: post.content,
        post_id: post.id,
      };
      const config = {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        }
      };
      getAPI.post("/replyadd/", bodyParameters, config)
      .then(() => this.loadReplies(post.id))
      .then(() => post.content = '')
    },
    loadReplies(post) {
      (this.postReplyShow = post),
        getAPI
          .get("/reply/", {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
            params: { post_id: post },
          })
          .then((response) => {
            this.$store.state.ReplyData = response.data;
          })
          // .then(console.log(this.$store.state.ReplyData));
    },
    getUser() {
      getAPI
        .get("/player/", {
            headers: {
              Authorization: `Bearer ${this.$store.state.accessToken}`,
            },
            params: { username: this.$store.state.username.username },
          })
        .then((response) => {
          // console.log(response.data[0])
          this.$store.state.UserData = response.data[0];
        }).then(this.getAdditionalUserData())
    },
    getAdditionalUserData() {
      getAPI.get("/player/" + this.$store.state.UserData.id, {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`,
        },
      }).then((response) => {console.log(response) 
      this.$store.state.AdditionalData = response.data[0]})
    },
    splitByHashtag(stringToSplit) {
      let hashWords = stringToSplit.match(/#(\w+)/g);
      if (hashWords) {
        hashWords = hashWords.join(" ");
      } else {
        hashWords = "";
      }
      let content = stringToSplit.split("#")[0];
      return [hashWords, content];
    },
  },
  created() {
    this.loadFeed(), this.getAdditionalUserData();
  },
};
</script>

<style>
.reply > div > div {
  background: lightblue;
}
</style>