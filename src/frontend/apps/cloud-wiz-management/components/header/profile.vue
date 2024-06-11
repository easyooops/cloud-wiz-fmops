<template>
  <li class="profile-nav onhover-dropdown pe-0 py-0">
    <div class="media profile-media">
      <img class="b-r-10" src="/images/dashboard/profile.png" alt="" />
      <div class="media-body">
        <span>Suyeong Yoo</span>
        <p class="mb-0 font-roboto">
          Admin <i class="middle fa fa-angle-down"></i>
        </p>
      </div>
    </div>
    <ul class="profile-dropdown onhover-show-div">
      <li>
        <nuxt-link :to="'/users/profile'"><vue-feather type="user"></vue-feather><span>Account </span></nuxt-link>
      </li>
      <li>
        <nuxt-link :to="'/email/readMail'"><vue-feather type="mail"></vue-feather><span>Inbox</span></nuxt-link>
      </li>
      <li>
        <nuxt-link :to="'/task'"><vue-feather type="file-text"></vue-feather><span>Taskboard</span></nuxt-link>
      </li>
      <li>
        <nuxt-link :to="'/search'"><vue-feather type="settings"></vue-feather><span>Settings</span></nuxt-link>
      </li>
      <li>
        <a @click="logout"><vue-feather type="log-in"></vue-feather><span>Log out</span></a>
      </li>
    </ul>
  </li>
</template>

<script>


export default {
  name: 'Profile',
  methods: {
    logout: function () {

      this.$router.replace('/auth/login');

      useCookie('User').value = undefined
    }

  },
};
</script>
