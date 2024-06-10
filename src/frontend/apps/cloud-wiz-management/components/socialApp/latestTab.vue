<template>
  <div class="col-xl-12 xl-50 box-col-6">
    <div class="card">
      <div class="card-header">
        <h5 class="mb-0">
          <button class="btn btn-link" data-bs-target="#collapseicon4" aria-expanded="true" aria-controls="collapseicon4"
            v-on:click="toogle = !toogle">Latest Photos</button>
        </h5>
      </div>
      <div class="collapse " id="collapseicon4" data-bs-parent="#accordion" aria-labelledby="collapseicon4"
        :class="{ show: toogle }">
        <div class="card-body photos filter-cards-view px-0">
          <ul class="text-center">
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-1.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-2.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-3.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-4.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-5.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-6.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-7.png"></div>
            </li>
            <li>
              <div class="latest-post"><img class="img-fluid" alt="" src="/images/social-app/post-8.png"></div>
            </li>
          </ul>
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