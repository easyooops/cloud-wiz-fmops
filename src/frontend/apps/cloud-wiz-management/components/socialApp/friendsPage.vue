<template>
  <div class="row">
    <div class="col-xl-4 col-sm-6 col-xxl-3 col-ed-4 box-col-4" v-for="(item, index) in users" :key="index">
      <div class="card social-profile">
        <div class="card-body">
          <div class="social-img-wrap">
            <div class="social-img"><img :src="getImgUrl(item.avatar)" alt="profile"></div>
            <div class="edit-icon">
              <svg>
                <use href="@/assets/svg/icon-sprite.svg#profile-check"></use>
              </svg>
            </div>
          </div>
          <div class="social-details">
            <h5 class="mb-1"><a href="social-app.html">{{ item.name }}</a></h5><span class="f-light">{{ item.email
            }}</span>
            <ul class="card-social">
              <li><a href="https://www.facebook.com/" target="_blank"><i class="fa fa-facebook"></i></a></li>
              <li><a href="https://accounts.google.com/" target="_blank"><i class="fa fa-google-plus"></i></a></li>
              <li><a href="https://twitter.com/" target="_blank"><i class="fa fa-twitter"></i></a></li>
              <li><a href="https://www.instagram.com/" target="_blank"><i class="fa fa-instagram"></i></a></li>
              <li><a href="https://rss.app/" target="_blank"><i class="fa fa-rss"></i></a></li>
            </ul>
            <ul class="social-follow">
              <li>
                <h5 class="mb-0">{{ item.totalPost }}</h5><span class="f-light">Posts</span>
              </li>
              <li>
                <h5 class="mb-0">{{ item.follower }}</h5><span class="f-light">Followers</span>
              </li>
              <li>
                <h5 class="mb-0">{{ item.following }}</h5><span class="f-light">Following</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import { data } from "@/data/users/user.json"
export default {
  name: 'userCards',
  data() {
    return {
      users: data
    }
  },
  methods: {
    getImgUrl(path) {
      return '/images/' + path
    }
  }

}
</script>