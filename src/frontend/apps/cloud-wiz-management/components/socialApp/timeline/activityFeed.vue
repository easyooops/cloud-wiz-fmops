<template>
  <div class="card">
    <div class="card-header">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block " data-bs-target="#collapseicon12" aria-expanded="true"
          aria-controls="collapseicon12" v-on:click="show = !show">Activity Feed</button>
      </h2>
    </div>
    <div class="collapse " id="collapseicon12" aria-labelledby="collapseicon12" data-parent="#accordion"
      :class="{ show: show }">
      <div class="card-body social-status filter-cards-view">
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/10.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href=""><span class="f-w-600 d-block">Andew
                  Jon</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">20 min
              Ago</span>
          </div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/3.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href=""><span class="f-w-600 d-block">Johny
                  Waston</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">1 hour
              Ago</span>
          </div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/5.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href=""><span class="f-w-600 d-block">Comeren
                  Diaz</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">1 days
              Ago</span>
          </div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/4.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href=""><span class="f-w-600 d-block">Sarah
                  Loren</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">2 days
              Ago</span>
          </div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/3.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href=""><span class="f-w-600 d-block">Johny
                  Waston</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">5 days
              Ago</span>
          </div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/5.jpg" alt="">
          <div class="media-body"><router-link to="/users/profile"><a href="user-profile.html"><span
                  class="f-w-600 d-block">Comeren Diaz</span></a></router-link>
            <p>Commented on Shaun Park's <a href="javascript:void(0)">Photo</a></p><span class="light-span">6 days
              Ago</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      show: true
    }
  }
}
</script>