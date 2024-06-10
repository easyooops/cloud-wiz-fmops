<template>
  <div class="col-xl-12 xl-50 box-col-6">
    <div class="card">
      <div class="card-header">
        <h5 class="mb-0">
          <button class="btn btn-link" data-bs-target="#collapseicon10" aria-expanded="true"
            aria-controls="collapseicon10" v-on:click="toogle = !toogle">Followings</button>
        </h5>
      </div>
      <div class="collapse " id="collapseicon10" aria-labelledby="collapseicon10" data-bs-parent="#accordion"
        :class="{ show: toogle }">
        <div class="card-body social-list filter-cards-view">
          <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" alt="" src="/images/user/3.png">
            <div class="media-body"><span class="d-block">Sarah Loren</span><a href="#">Add Friend</a></div>
          </div>
          <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" alt="" src="/images/user/2.png">
            <div class="media-body"><span class="d-block">Bucky Barnes</span><a href="#">Add Friend</a></div>
          </div>
          <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" alt="" src="/images/user/10.jpg">
            <div class="media-body"><span class="d-block">Comeren Diaz</span><a href="#">Add Friend</a></div>
          </div>
          <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" alt="" src="/images/user/3.jpg">
            <div class="media-body"><span class="d-block">Jason Borne</span><a href="#">Add Friend</a></div>
          </div>
          <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" alt="" src="/images/user/11.png">
            <div class="media-body"><span class="d-block">Andew Jon</span><a href="#">Add Friend</a></div>
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
      toogle: true
    }
  }
}
</script>