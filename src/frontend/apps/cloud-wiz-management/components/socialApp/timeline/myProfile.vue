<template>
  <div class="row">
    <div class="col-xl-3 xl-40 col-lg-12 col-md-5 box-col-4">
      <div class="default-according style-1 faq-accordion " id="accordionoc4">

        <div class="card">
          <div class="card-header" id="headingOne">
            <h2 class="mb-0">
              <button class="btn btn-link btn-block text-start" data-bs-target="#collapseicon" aria-expanded="true"
                aria-controls="collapseicon" v-on:click="toogle = !toogle">My Profile</button>
            </h2>
          </div>
          <div class="collapse" id="collapseicon" aria-labelledby="collapseicon" data-parent="#accordion"
            :class="{ show: toogle }">
            <div class="card-body socialprofile filter-cards-view">
              <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" src="/images/user/1.jpg" alt="">
                <div class="media-body">
                  <h6 class="font-primary f-w-600">My Page</h6><span class="d-block"><span><i class="fa fa-comments-o">
                      </i><span class="px-2">Messages<span
                          class="badge rounded-pill badge-light ms-1">9</span></span></span></span><span
                    class="d-block"><span><i class="fa fa-bell-o"> </i><span class="px-2">Notification<span
                          class="badge rounded-pill badge-light ms-1">9</span></span></span></span>
                </div>
              </div>
              <div class="social-btngroup d-flex">
                <button class="btn btn-primary text-center " type="button">Likes</button>
                <button class="btn btn-primary-light text-center ms-2" type="button">View</button>
              </div>
              <div class="likes-profile text-center">
                <h5 class="f-w-600 mb-1"><i class="fa fa-heart font-danger"></i> 884</h5>
              </div>
              <h6 class="text-center">35 New Likes This Week</h6>
              <div class="customers text-center social-group">
                <ul>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/3.jpg" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Johny Waston"></li>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/5.jpg" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Andew Jon"></li>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/1.jpg" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Comeren Diaz"></li>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/2.png" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Bucky Barnes"></li>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/8.jpg" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Jason Borne"></li>
                  <li class="d-inline-block"><img class="img-30 rounded-circle" src="/images/user/11.png" alt=""
                      data-container="body" data-bs-toggle="popover" data-placement="top" title=""
                      data-original-title="Comeren Diaz"></li>
                </ul>
              </div><img class="img-fluid mt-5" alt="" src="/images/social-app/timeline-3.png">
            </div>
          </div>
        </div>


        <SocialAppAboutMutualFriends />
        <SocialAppTimelineActivityFeed />

      </div>
    </div>
    <SocialAppTimelinePostView />
    <SocialAppTimelineProfileIntro />
  </div>
</template>
<script>
export default {
  data() {
    return {
      toogle: true,
    }
  }
}
</script>