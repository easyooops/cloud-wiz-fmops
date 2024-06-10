<template>
  <div class="col-xl-3 xl-50 col-md-6 box-col-6">
    <div class="card features-faq product-box">
      <div class="faq-image product-img"><img class="img-fluid" src="/images/faq/3.jpg" alt="">
        <div class="product-hover">
          <ul>
            <li><i class="icon-link"></i></li>
            <li><i class="icon-import"></i></li>
          </ul>
        </div>
      </div>
      <div class="card-body">
        <h6>UI Design</h6>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum
          sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
      </div>
      <div class="card-footer"><span>Dec 15, 2022</span><span class="pull-right"><i class="fa fa-star font-primary"></i><i
            class="fa fa-star font-primary"></i><i class="fa fa-star font-primary"></i><i
            class="fa fa-star font-primary"></i><i class="fa fa-star font-primary"></i></span></div>
    </div>
  </div>
  <div class="col-xl-3 xl-50 col-md-6 box-col-6">
    <div class="card features-faq product-box">
      <div class="faq-image product-img"><img class="img-fluid" src="/images/faq/4.jpg" alt="">
        <div class="product-hover">
          <ul>
            <li><i class="icon-link"></i></li>
            <li><i class="icon-import"></i></li>
          </ul>
        </div>
      </div>
      <div class="card-body">
        <h6> UX Design</h6>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum
          sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.</p>
      </div>
      <div class="card-footer"><span>Dec 15, 2022</span><span class="pull-right"><i class="fa fa-star font-primary"></i><i
            class="fa fa-star font-primary"></i><i class="fa fa-star font-primary"></i><i
            class="fa fa-star font-primary"></i><i class="fa fa-star-half-o font-primary"></i></span></div>
    </div>
  </div>
</template>
<script>

import pxcard from '../Pxcard.vue'
export default {
  components: {
    'px-card': pxcard,
  }
}
</script>