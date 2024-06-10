<template>
  <div class="col-xl-12 xl-50 box-col-6">
    <div class="card">
      <div class="card-header">
        <h5 class="mb-0">
          <button class="btn btn-link" data-bs-target="#collapseicon13" aria-expanded="true"
            aria-controls="collapseicon13" v-on:click="toogle = !toogle">Friends</button>
        </h5>
      </div>
      <div class="collapse " id="collapseicon13" data-bs-parent="#accordion" aria-labelledby="collapseicon13"
        :class="{ show: toogle }">
        <div class="card-body avatar-showcase filter-cards-view">
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/3.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/5.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/1.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/2.png" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/3.png" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/6.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/10.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/14.png" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/1.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/4.jpg" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/11.png" alt="#">
          </div>
          <div class="d-inline-block friend-pic"><img class="img-50 rounded-circle" src="/images/user/8.jpg" alt="#">
          </div>
        </div>
    </div>
  </div>
</div></template>
<script>
export default {
  data() {
    return {
      toogle: true
    }
  }
}
</script>