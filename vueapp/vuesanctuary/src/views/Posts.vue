<template>
  <div class="posts">
    <Navbar></Navbar>
    <h1 class="text-center">The Sanctuary</h1>
    <article class="container" id="app">
      <div class="row">
        <div class="col-4">
          <div style="position: fixed" class="col-3 border border-dark">
            <!-- <img src='{% static "sanctuary\waterfall.JPG"  %}' class="img-thumbnail "> -->
            <!-- <h2 class="text-center">{{ userData.username }}</h2> -->
            <h2 class="text-center">{{ userData.user }}</h2>
          </div>
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
              <li v-for="post in posts" :key="post.id" class="list-group-item">
                <h3>{{ post.username }}</h3>
                <p>{{ post.created }}</p>
                <p>{{ post.text_content }}</p>
                <!-- <img v-if="post.img_content" :src="'api/'+post.img_content"> -->
                <p>{{ post.hashtags }}</p>
                <input
                  v-model="replyPost.text_content"
                  type="text"
                  placeholder="Reply"
                />
                <!-- <input v-model="replyPost.img_content" type="image"> -->
                <button
                  @click="replyToPost(post.id)"
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
                <div v-show="post.id === postReplyShow" class="card card-body">
                  <div v-for="reply in replies" :key="reply.id">
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
import { mapState } from 'vuex'

export default {
  name: "Posts",
  data() {
    return {
      // posts: [],
      replies: [],
      postReplyShow: "",
      newPost: {},
      userData: {},
      replyPost: {},
      isHidden: false,
    };
  },
  components: {
    Navbar,
  },
  computed: mapState(['posts']),
  methods: {
    loadFeed() {
      getAPI.get("/post/", {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then(response => {
            console.log('Post API has recieved data')
            this.$store.state.posts = response.data
        })
    },
    postFeed() {
      let [hashWords, content] = this.splitByHashtag(this.newPost.text_content);
      fetch("/post/", {
        method: "POST",
        body: JSON.stringify({
          user: "1",
          text_content: content,
          //img_content: this.newPost.img_content,
          hashtags: hashWords.join(" "),
        }),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      });
    },
    replyToPost(post) {
      fetch("/replyadd/", {
        method: "POST",
        body: JSON.stringify({
          user: "2",
          text_content: this.replyPost.text_content,
          post_id: post,
        }),
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      });
    },
    loadReplies(post) {
      (this.postReplyShow = post),
        getAPI
          .get("/reply/", {
            params: {
              post_id: post,
            },
          })
          .then((response) => (this.replies = response.data))
          .then((response) => console.log(response));
    },
    getUser() {
      getAPI
        .get("/player/", {
        headers: {
          Authorization: `Bearer ${this.$store.state.accessToken}`
        }
      })
        .then((response) => (this.userData = response.data))
        .then((response) => console.log(response))
    },
    splitByHashtag(stringToSplit) {
      let hashWords = stringToSplit.match(/#(\w+)/g);
      let content = stringToSplit.split("#")[0];
      return [hashWords, content];
    },
  },
  created() {
    this.loadFeed(), this.getUser();
  },
};
</script>