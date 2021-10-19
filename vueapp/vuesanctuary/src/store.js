import { createStore } from 'vuex'
import { getAPI } from './axios-api'



export default createStore({
    state() {
        return {
            accessToken: null,
            refreshToken: null,
        }
    },
    mutations: {
        updateStorage (state, { access, refresh }){
            state.accessToken = access
            state.refreshToken = refresh
        },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    getters: {
        loggedIn (state) {
            return state.accessToken != null
        }
    },
    actions: {
        userLogout (context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin (context, userCredentials) {
            return new Promise((resolve, reject) => {
                getAPI.post('/api-token/', {
                    username: userCredentials.username,
                    password: userCredentials.password
                })
                .then(response => {
                    context.commit('updateStorage', {
                        access: response.data.access, refresh: response.data.refresh
                    })
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
            })
        }
    }
})

