<template>
  <div class="col-sm-12">
    <div class="card profile-header">
      <div class="profile-img-wrrap"></div>
      <div class="userpro-box">
        <div class="img-wrraper">
          <div class="avatar"><img class="img-fluid" alt="" src="/images/user/7.jpg"></div><a class="icon-wrapper"
            href="edit-profile.html"><i class="icofont icofont-pencil-alt-5"></i></a>
        </div>
        <div class="user-designation">
          <div class="title"><a target="_blank" href="">
              <h4>Emay Walter</h4>
              <h6>designer</h6>
            </a></div>
          <div class="social-media">
            <ul class="user-list-social">
              <li><a href="#"><i class="fa fa-facebook"></i></a></li>
              <li><a href="#"><i class="fa fa-google-plus"></i></a></li>
              <li><a href="#"><i class="fa fa-twitter"></i></a></li>
              <li><a href="#"><i class="fa fa-instagram"></i></a></li>
              <li><a href="#"><i class="fa fa-rss"></i></a></li>
            </ul>
          </div>
          <div class="follow">
            <ul class="follow-list">
              <li>
                <div class="follow-num">325</div><span>Follower</span>
              </li>
              <li>
                <div class="follow-num counter">450</div><span>Following</span>
              </li>
              <li>
                <div class="follow-num counter">500</div><span>Likes</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <socialTabs />
</template>
<script>
import socialTabs from "./socialTabs.vue"

export default {
  components: {
    socialTabs
  },
  data() {
    return {
      showtab: 'timeline',
    }
  },
  methods: {
    changetab(tab) {
      this.showtab = tab;
    }
  }
}
</script>