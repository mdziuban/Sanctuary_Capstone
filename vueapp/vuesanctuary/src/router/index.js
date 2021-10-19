import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import Posts from '../views/Posts'
import Login from '../views/Login'
import Logout from '../views/Logout'

const routes = [
  {
    path: '/',
    name: 'posts',
    component: Posts,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login/',
    name: 'login',
    component: Login
  },
  {
    path: '/logout/',
    name: 'logout',
    component: Logout,
    meta: {
      requiresLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router

