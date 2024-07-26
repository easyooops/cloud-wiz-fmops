import { defineNuxtPlugin } from '#app'
import { loadGapiInsideDOM, loadAuth2 } from 'gapi-script'

export default defineNuxtPlugin((nuxtApp) => {
  const gAuthOptions = {
    clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
    scope: 'https://www.googleapis.com/auth/drive',
    redirect_uri: import.meta.env.VITE_GOOGLE_REDIRECT_URI,
    fetch_basic_profile: false
  }

  const initGoogle = async () => {
    await loadGapiInsideDOM()
    const auth2 = await loadAuth2(gapi, gAuthOptions.clientId, gAuthOptions.scope)
    return auth2
  }

  const googleAuth = {
    instance: null,
    async signIn() {
      if (!this.instance) {
        this.instance = await initGoogle()
      }
      return this.instance.signIn()
    },
    async getAuthCode() {
      if (!this.instance) {
        this.instance = await initGoogle()
      }
      console.log("== getAuthCode() ========================")
      console.log(this.instance)
      console.log("== getAuthCode() ========================")
      return new Promise((resolve, reject) => {
        this.instance.grantOfflineAccess({ prompt:'consent', response_type:'code' }).then(response => {
          resolve(response.code)
        }).catch(reject)
      })
    }
  }

  nuxtApp.provide('googleAuth', googleAuth)
})
