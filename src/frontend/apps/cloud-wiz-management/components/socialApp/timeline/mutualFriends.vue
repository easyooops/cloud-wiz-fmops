<template>
  <div class="card">
    <div class="card-header" id="headingTwo">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-start collapsed" data-bs-target="#collapseicon1" aria-expanded="true"
          aria-controls="collapseicon1" v-on:click="toogle = !toogle">Mutual Friends</button>
      </h2>
    </div>
    <div class="collapse " id="collapseicon1" data-parent="#accordion" aria-labelledby="collapseicon1"
      :class="{ show: toogle }">
      <div class="card-body social-status filter-cards-view">
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/2.png" alt="">
          <div class="social-status social-online"></div>
          <div class="media-body"><span class="f-w-600 d-block">Bucky Barnes</span><span
              class="d-block">winter@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/10.jpg" alt="">
          <div class="social-status social-busy"></div>
          <div class="media-body"><span class="f-w-600 d-block">Sarah Loren</span><span
              class="d-block">barnes@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/6.jpg" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Jason Borne</span><span
              class="d-block">jasonb@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/8.jpg" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Comeren Diaz</span><span
              class="d-block">comere@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/14.png" alt="">
          <div class="social-status social-online"></div>
          <div class="media-body"><span class="f-w-600 d-block">Andew Jon</span><span
              class="d-block">andrewj@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/4.jpg" alt="">
          <div class="social-status social-busy"></div>
          <div class="media-body"><span class="f-w-600 d-block">Johny Waston</span><span
              class="d-block">johny@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/3.png" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Johny William</span><span
              class="d-block">johnyw@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/2.png" alt="">
          <div class="social-status social-online"></div>
          <div class="media-body"><span class="f-w-600 d-block">Bucky Barnes</span><span
              class="d-block">winter@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/10.jpg" alt="">
          <div class="social-status social-busy"></div>
          <div class="media-body"><span class="f-w-600 d-block">Sarah Loren</span><span
              class="d-block">barnes@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/6.jpg" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Jason Borne</span><span
              class="d-block">jasonb@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/8.jpg" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Comeren Diaz</span><span
              class="d-block">comere@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/14.png" alt="">
          <div class="social-status social-online"></div>
          <div class="media-body"><span class="f-w-600 d-block">Andew Jon</span><span
              class="d-block">andrewj@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/4.jpg" alt="">
          <div class="social-status social-busy"></div>
          <div class="media-body"><span class="f-w-600 d-block">Johny Waston</span><span
              class="d-block">johny@gmail.com</span></div>
        </div>
        <div class="media"><img class="img-50 rounded-circle m-r-15" src="/images/user/3.png" alt="">
          <div class="social-status social-offline"></div>
          <div class="media-body"><span class="f-w-600 d-block">Johny William</span><span
              class="d-block">johnyw@gmail.com</span></div>
        </div>

      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      toogle: true,
      friends: [
        { image: "2.png", StatusClass: "social-online", name: "Bucky Barnes", email: "winter@gmail.com" },
        { image: "10.jpg", StatusClass: "social-busy", name: "Sarah Loren", email: "barnes@gmail.com" },
        { image: "6.jpg", StatusClass: "social-offline", name: "Jason Borne", email: "jasonb@gmail.com" },
        { image: "8.jpg", StatusClass: "social-offline", name: "Comeren Diaz", email: "comere@gmail.com" },
        { image: "14.png", StatusClass: "social-online", name: "Andew Jon", email: "andrewj@gmail.com" },
        { image: "4.jpg", StatusClass: "social-busy", name: "Johny Waston", email: "johny@gmail.com" },
        { image: "3.png", StatusClass: "social-offline", name: "Johny William", email: "johnyw@gmail.com" },
        { image: "2.png", StatusClass: "social-online", name: "Bucky Barnes", email: "winter@gmail.com" },
        { image: "10.jpg", StatusClass: "social-busy", name: "Sarah Loren", email: "barnes@gmail.com" },
        { image: "6.jpg", StatusClass: "social-offline", name: "Jason Borne", email: "jasonb@gmail.com" },
        { image: "8.jpg", StatusClass: "social-offline", name: "Comeren Diaz", email: "comere@gmail.com" },
        { image: "14.png", StatusClass: "social-online", name: "Andew Jon", email: "andrewj@gmail.com" },
        { image: "4.jpg", StatusClass: "social-busy", name: "Johny Waston", email: "johny@gmail.com" },
        { image: "3.png", StatusClass: "social-offline", name: "Johny William", email: "johnyw@gmail.com" },
      ]
    }
  },
}
</script>