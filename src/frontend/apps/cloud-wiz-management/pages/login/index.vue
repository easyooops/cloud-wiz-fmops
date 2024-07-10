<template>
  <div>
    <div class="container-fluid">
      <div class="row ">
        <div class="col-12 p-0">
          <div class="login-card">
            <div>
              <div class="login-main">
                <form class="theme-form">
                  <h4>Sign in to account</h4>
                  <div class="mt-4">
                    <div class="social mt-4" id="googleButton"></div>
                  </div>
                </form>
                <div>
                  <a class="logo">
                    <img class="img-fluid" src="/images/wiz/logo-pink.png" alt="looginpage" width="300" />
                  </a>
                </div>                   
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from '@/store/auth';
import { mapState, mapActions } from 'pinia';
import { useRouter } from 'vue-router';

definePageMeta({
  layout: 'custom'
})

export default {
  name: 'login',
  data() {
    const router = useRouter();
  },
  methods: {
    ...mapActions(useAuthStore, ['loginWithGoogle']),
    async login() {
      if (this.user.name.value.trim() === '') {
        this.user.name.errormsg = 'Please enter your name.';
        return;
      }

      try {
        await this.loginWithGoogle({ name: this.user.name.value });
      } catch (error) {
        console.error('Login failed:', error);
      } finally {
      }
    },
    googleInitialize() {
      google.accounts.id.initialize({
        client_id: import.meta.env.VITE_GOOGLE_CLIENT_ID,
        callback: this.handleCallback,
        context: 'use',
      })
      google.accounts.id.renderButton(
        document.getElementById('googleButton'),
        {
          type: 'standard',         // Button type: standard, icon
          theme:'filled_blue',      // Theme: outline, filled_blue, filled_black
          size: 'large',            // Button size: large, medium, small
          text: 'signin_with',      // Button text: signin_with, signup_with, continue_with, signIn
          shape: 'rectangular',     // Button shape: rectangular, pill, circle, square
          logo_alignment: 'center',
          width: 50,
        }
      )
    },
    async handleCallback(response){
      if (response && response.credential) {
        const token = response.credential
        const base64Payload = token.split('.')[1]
        const payload = atob(base64Payload);
        const result = JSON.parse(payload);

        await this.loginWithGoogle(token)

        this.$router.push('/');
        
      } else {
        console.error('No credential found in response');
      } 
    }    
  },
  mounted() {
    this.googleInitialize()
  }
};
</script>