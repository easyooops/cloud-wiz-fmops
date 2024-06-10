<template>
  <div class="col-xl-3 xl-100 box-col-12">
    <div class="default-according style-1 faq-accordion job-accordion" id="accordionoc1">
      <div class="row">
        <div class="col-xl-12 xl-50 box-col-6">
          <div class="card">
            <div class="card-header">
              <h5 class="p-0">
                <button class="btn btn-link ps-0" data-bs-target="#collapseicon2" aria-expanded="true"
                  aria-controls="collapseicon2" v-on:click="toogle = !toogle">Profile Intro</button>
              </h5>
            </div>
            <div class="collapse " id="collapseicon2" aria-labelledby="collapseicon2" data-parent="#accordion"
              :class="{ show: toogle }">
              <div class="card-body filter-cards-view">
                <div class="filter-view-group"><span class="f-w-600">About Me :</span>
                  <p>
                    Hi, I’m elana, I’m 30 and I work as a
                    web Designer for the “Daydreams”
                    Agency in Pier 56.
                  </p>
                </div>
                <div class="filter-view-group"><span class="f-w-600">Favourite TV shows :</span>
                  <p>
                    Breaking Good, RedDevil, People of
                    Interest, The Running Dead,
                    Found, American Guy.
                  </p>
                </div>
                <div class="filter-view-group"><span class="f-w-600">Favourite Music Bands :</span>
                  <p>
                    Breaking Good, RedDevil, People of
                    Interest, The Running Dead,
                    Found, American Guy.
                  </p>
                </div>
                <div class="social-network theme-form"><span class="f-w-600">Social Networks</span>
                  <button class="btn social-btn btn-fb mb-2 text-center"><i
                      class="fa fa-facebook m-r-5"></i>Facebook</button>
                  <button class="btn social-btn btn-twitter mb-2 text-center"><i
                      class="fa fa-twitter m-r-5"></i>Twitter</button>
                  <button class="btn social-btn btn-google text-center"><i
                      class="fa fa-dribbble m-r-5"></i>Dribbble</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <SocialAppFollowersTab />
        <SocialAppFollowing />
        <SocialAppLatestTab />
        <SocialAppFriendsTab />

        <div class="col-xl-12 col-md-6 xl-50 box-col-6">
          <div class="card"><img class="img-fluid" src="/images/social-app/timeline-4.png" alt=""></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      toogle: true
    }
  }
}
</script>