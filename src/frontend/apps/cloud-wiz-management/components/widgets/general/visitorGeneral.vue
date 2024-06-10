<template>
  <div class="col-xxl-5 col-xl-3 col-md-12 box-col-12">
    <div class="card visitor-card">
      <div class="card-header card-no-border pb-0">
        <div class="header-top">
          <h5 class="m-0">Visitors<span class="f-14 font-primary f-w-500 ms-1">
              <svg class="svg-fill me-1">
                <use href="@/assets/svg/icon-sprite.svg#user-visitor"></use>
              </svg>(+2.8)</span></h5>
          <div class="card-header-right-icon">
            <div class="dropdown icon-dropdown">
              <button class="btn dropdown-toggle" id="visitorButton" type="button" data-bs-toggle="dropdown"
                aria-expanded="false"><i class="icon-more-alt"></i></button>
              <div class="dropdown-menu dropdown-menu-end" aria-labelledby="visitorButton"><a class="dropdown-item"
                  href="#">Today</a><a class="dropdown-item" href="#">Tomorrow</a><a class="dropdown-item"
                  href="#">Yesterday</a></div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body pt-3">
        <div class="visitors-container">
          <apexchart height="285" type="bar" :options="ecomDashboard.options4" :series="ecomDashboard.series4">
          </apexchart>
        </div>
      </div>
    </div>
  </div>
  <div class="col-xl-3 col-sm-6">
    <div class="card social-widget">
      <div class="card-body">
        <div class="d-flex align-items-center justify-content-between">
          <div class="d-flex align-items-center gap-2">
            <div class="social-icons"><img src="/images/dashboard-5/social/1.png" alt="facebook icon"></div>
            <span>Facebook</span>
          </div><span class="font-success f-12 d-xxl-block d-xl-none">+22.9%</span>
        </div>
        <div class="social-content">
          <div>
            <h5 class="mb-1">12,098</h5><span class="f-light">Followers</span>
          </div>
          <div class="social-chart">
            <apexchart height="96.4" type="radialBar" :options="socialDashboard.options" :series="socialDashboard.series">
            </apexchart>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { socialDashboard } from '@/data/comon'
import { ecomDashboard } from '@/data/comon'

export default {
  data() {
    return {
      socialDashboard: socialDashboard,
      ecomDashboard: ecomDashboard
    }
  }
}
</script>