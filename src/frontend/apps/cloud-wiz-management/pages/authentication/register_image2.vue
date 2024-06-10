<template>
  <div>
    <div class="container-fluid p-0">
      <div class="row m-0">
        <div class="col-xl-7 b-center bg-size p-0" :style="{ backgroundImage: 'url(' + '/images/login/1.jpg' + ')' }"
          style="background-size: cover; background-position: center center; display: block;">
          <img class="bg-img-cover bg-center" src="/images/login/1.jpg" alt="looginpage" style="display: none;" />
        </div>
        <div class="col-xl-5 p-0">
          <div class="login-card">
            <div>
              <div>
                <a class="logo">
                  <img class="img-fluid" src="/images/logo/logo.png" alt="looginpage" />
                </a>
              </div>
              <div class="login-main ">
                <form class="theme-form">
                  <h4>Create your account</h4>
                  <p>Enter your personal details to create account</p>
                  <div class="form-group">
                    <label class="col-form-label pt-0">Your Name</label>
                    <div class="row g-2">
                      <div class="col-6">
                        <input class="form-control" type="text" required="" placeholder="First name" />
                      </div>
                      <div class="col-6">
                        <input class="form-control" type="text" required="" placeholder="Last name" />
                      </div>
                    </div>
                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Email Address</label>
                    <input class="form-control" type="email" required="" placeholder="Test@gmail.com" />
                  </div>
                  <div class="form-group">
                    <label class="col-form-label">Password</label>
                    <div class="form-input position-relative">

                      <input class="form-control" :type="active ? 'password' : 'text'" name="login[password]" required=""
                        placeholder="*********" />
                      <div class="show-hide"><span :class="active ? 'show' : 'hide'" @click.prevent="show"> </span></div>
                    </div>
                  </div>
                  <div class="form-group mb-0">
                    <div class="checkbox p-0">
                      <input id="checkbox1" type="checkbox" />
                      <label class="text-muted" for="checkbox1">Agree with<a class="ms-2" href="#">Privacy
                          Policy</a></label>
                    </div>
                    <button class="btn btn-primary btn-block w-100">
                      Create Account
                    </button>
                  </div>
                  <h6 class="text-muted mt-4 or">Or signup with</h6>
                  <div class="social mt-4">
                    <div class="social mt-4">
                      <div class="btn-showcase"><a class="btn btn-light" href="https://www.linkedin.com/login"
                          target="_blank"><vue-feather class="txt-linkedin" type="linkedin"></vue-feather>LinkedIn </a><a
                          class="btn btn-light" href="https://twitter.com/login?lang=en" target="_blank"><vue-feather
                            class="txt-twitter" type="twitter"></vue-feather>twitter</a><a class="btn btn-light"
                          href="https://www.facebook.com/" target="_blank"><vue-feather class="txt-fb"
                            type="facebook"></vue-feather>facebook</a></div>
                    </div>
                  </div>
                  <p class="mt-4 mb-0">
                    Already have an account?
                    <router-link class="ms-2" to="/auth/login">
                      Login
                    </router-link>
                  </p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
definePageMeta({
  layout: 'custom'
})
export default {
  data() {
    return {
      active: true
    }
  },
  methods: {
    show() {
      this.active = !this.active
    }
  }
}
</script>