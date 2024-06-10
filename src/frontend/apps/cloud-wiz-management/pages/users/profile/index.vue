<template>
  <Breadcrumbs title="User Profile" main="User" />

  <div class="container-fluid ">
    <div class="user-profile">
      <div class="row">
        <indexProfile />
      </div>
    </div>
  </div>
</template>

<script>
import indexProfile from '@/components/users/profile/indexProfile.vue';

export default {
  name: 'userProfile',
  components: {
    indexProfile
  },

}
</script>
