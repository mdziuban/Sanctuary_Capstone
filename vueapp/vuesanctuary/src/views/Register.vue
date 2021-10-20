<template>
  <div>
  <div class="container text-dark">
    <div class="row justify-content-md-center">
      <div class="col-md-5 p-3 login justify-content-md-center">
        <h1 class="h3 mb-3 font-weight-normal text-center">Welcome to Sanctuary, Register to Continue.</h1>

        <p v-if="noMatch">Passwords did not match.</p>
        <form v-on:submit.prevent="register">
          <div class="form-group">
            <input type="text" name="username" id="user" v-model="username" class="form-control" placeholder="Username">
          </div>
          <div class="form-group">
            <input type="password" name="password1" id="pass1" v-model="password1" class="form-control" placeholder="Password">
          </div>
          <div class="form-group">
            <input type="password" name="password2" id="pass2" v-model="password2" class="form-control" placeholder="Password Again">
          </div>
          <div class="form-group">
            <input type="email" name="email" id="email" v-model="email" class="form-control" placeholder="Email">
          </div>
          <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
        </form>
        
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { getAPI } from '../axios-api'
export default {
    name: 'register',
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            email: '',
            noMatch: false
        }
    },
    methods: {
        checkIfMatch(){
            if (this.password1 === this.password2 && this.password1 != ""){
                console.log('passwords matched')
                return true
            }
            else {
                console.log('no match for passwords')
                return false
            }
        },
        register() {
            const bodyParameters = {
                username: this.username,
                password: this.password1,
                email: this.email
            }
            getAPI.post('/register/', bodyParameters)
            .then(() => this.$router.push({name: 'login'}))
        }
    }
}
</script>