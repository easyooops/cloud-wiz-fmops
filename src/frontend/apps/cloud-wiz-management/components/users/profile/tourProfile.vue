<template>
  <div class="col-sm-12">
    <div class="card hovercard text-center">
      <div class="cardheader" style="    background-size: cover; background-position: 10%; height: 470px;"
        :style="{ backgroundImage: 'url(' + ('/images/other-images/bg-profile.png') + ')' }"></div>
      <div class="user-image">
        <div class="avatar"><img id="profile-tour" alt="" src="/images/user/7.jpg" data-intro="This is Profile image">
        </div>
        <div class="icon-wrapper"><i id="update-profile-tour" class="icofont icofont-pencil-alt-5"
            data-intro="Change Profile image here"></i></div>
      </div>
      <div class="info">
        <div class="row" data-intro="This is the your details" id="info-bar-tour">
          <div class="col-sm-6 col-lg-4 order-sm-1 order-xl-0">
            <div class="row">
              <div class="col-md-6">
                <div class="ttl-info text-start">
                  <h6><i class="fa fa-envelope"></i>   Email</h6><span>Marekjecno@yahoo.com</span>
                </div>
              </div>
              <div class="col-md-6">
                <div class="ttl-info text-start ttl-sm-mb-0">
                  <h6><i class="fa fa-calendar"></i>   BOD</h6><span>02 January 1988</span>
                </div>
              </div>
            </div>
          </div>
          <div class="col-sm-12 col-lg-4 order-sm-0 order-xl-1">
            <div class="user-designation">
              <div class="title"><a target="_blank" href="">Mark jecno</a></div>
              <div class="desc mt-2">designer</div>
            </div>
          </div>
          <div class="col-sm-6 col-lg-4 order-sm-2 order-xl-2">
            <div class="row">
              <div class="col-md-6">
                <div class="ttl-info text-start ttl-xs-mt">
                  <h6><i class="fa fa-phone"></i>   Contact Us</h6><span>India +91 123-456-7890</span>
                </div>
              </div>
              <div class="col-md-6">
                <div class="ttl-info text-start ttl-sm-mb-0">
                  <h6><i class="fa fa-location-arrow"></i>   Location</h6><span>B69 Near Schoool Demo Home</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <hr>
        <div class="social-media" data-intro="This is your Social details" id="social-bar-tour">
          <ul class="list-inline">
            <li class="list-inline-item"><a href="https://www.facebook.com/" target="_blank"><i
                  class="fa fa-facebook"></i></a></li>
            <li class="list-inline-item"><a href="https://accounts.google.com/" target="_blank"><i
                  class="fa fa-google-plus"></i></a></li>
            <li class="list-inline-item"><a href="https://twitter.com/" target="_blank"><i class="fa fa-twitter"></i></a>
            </li>
            <li class="list-inline-item"><a href="https://www.instagram.com/" target="_blank"><i
                  class="fa fa-instagram"></i></a></li>
            <li class="list-inline-item"><a href="https://rss.app/" target="_blank"><i class="fa fa-rss"></i></a></li>
          </ul>
        </div>
        <div class="follow">
          <div class="row">
            <div class="col-6 border-right">
              <div class="follow-num counter">
                <number class="bold counter" ref="number1" :from="0" :to="25869" :duration="5" :delay="0"
                  easing="Power1.easeOut" />
              </div><span>Follower</span>
            </div>
            <div class="col-6">
              <div class="follow-num counter">
                <number class="bold counter" ref="number1" :from="0" :to="659887" :duration="5" :delay="0"
                  easing="Power1.easeOut" />
              </div><span>Following</span>
            </div>
          </div>
      </div>
    </div>

  </div>
</div></template>
<script>
export default {
}
</script>