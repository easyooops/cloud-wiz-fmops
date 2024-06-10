<template>
  <div class="col-xxl-3 col-xl-4 col-md-6 box-col-6">
    <div class="row">
      <div class="col-sm-12">
        <div class="card course-box widget-course">
          <div class="card-body">
            <div class="course-widget">
              <div class="course-icon">
                <svg class="fill-icon">
                  <use href="@/assets/svg/icon-sprite.svg#course-1"></use>
                </svg>
              </div>
              <div>
                <h4 class="mb-0">100+</h4><span class="f-light">Completed Courses</span><a class="btn btn-light f-light"
                  href="learning-list-view.html">View course<span class="ms-2">
                    <svg class="fill-icon f-light">
                      <use href="@/assets/svg/icon-sprite.svg#arrowright"></use>
                    </svg></span></a>
              </div>
            </div>
          </div>
          <ul class="square-group">
            <li class="square-1 warning"></li>
            <li class="square-1 primary"></li>
            <li class="square-2 warning1"></li>
            <li class="square-3 danger"></li>
            <li class="square-4 light"></li>
            <li class="square-5 warning"></li>
            <li class="square-6 success"></li>
            <li class="square-7 success"></li>
          </ul>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card course-box widget-course">
          <div class="card-body">
            <div class="course-widget">
              <div class="course-icon warning">
                <svg class="fill-icon">
                  <use href="@/assets/svg/icon-sprite.svg#course-2"></use>
                </svg>
              </div>
              <div>
                <h4 class="mb-0">50+</h4><span class="f-light">In Progress Courses</span><a class="btn btn-light f-light"
                  href="learning-list-view.html">View course<span class="ms-2">
                    <svg class="fill-icon f-light">
                      <use href="@/assets/svg/icon-sprite.svg#arrowright"></use>
                    </svg></span></a>
              </div>
            </div>
          </div>
          <ul class="square-group">
            <li class="square-1 warning"></li>
            <li class="square-1 primary"></li>
            <li class="square-2 warning1"></li>
            <li class="square-3 danger"></li>
            <li class="square-4 light"></li>
            <li class="square-5 warning"></li>
            <li class="square-6 success"></li>
            <li class="square-7 success"></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="col-xxl-4 col-xl-5 col-md-6 box-col-6">
    <div class="row">
      <div class="col-xl-12">
        <div class="card">
          <div class="card-header card-no-border pb-0">
            <div class="header-top">
              <h5>Total Users</h5>
              <div class="dropdown icon-dropdown">
                <button class="btn dropdown-toggle" id="userdropdown" type="button" data-bs-toggle="dropdown"
                  aria-expanded="false"><i class="icon-more-alt"></i></button>
                <div class="dropdown-menu dropdown-menu-end" aria-labelledby="userdropdown"><a class="dropdown-item"
                    href="#">Weekly</a><a class="dropdown-item" href="#">Monthly</a><a class="dropdown-item"
                    href="#">Yearly</a></div>
              </div>
            </div>
          </div>
          <div class="card-body py-lg-3">
            <ul class="user-list">
              <li>
                <div class="user-icon primary">
                  <div class="user-box"><vue-feather class="font-primary" type="user-plus"></vue-feather></div>
                </div>
                <div>
                  <h5 class="mb-1">178,098</h5><span class="font-primary d-flex align-items-center"><i
                      class="icon-arrow-up icon-rotate me-1"> </i><span class="f-w-500">+30.89</span></span>
                </div>
              </li>
              <li>
                <div class="user-icon success">
                  <div class="user-box"><vue-feather class="font-success" type="user-minus"></vue-feather></div>
                </div>
                <div>
                  <h5 class="mb-1">178,098</h5><span class="font-danger d-flex align-items-center"><i
                      class="icon-arrow-down icon-rotate me-1"></i><span class="f-w-500">-08.89</span></span>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-xl-12">
        <div class="card growth-wrap">
          <div class="card-header card-no-border pb-0">
            <div class="header-top">
              <h5>Followers Growth</h5>
              <div class="dropdown icon-dropdown">
                <button class="btn dropdown-toggle" id="growthdropdown" type="button" data-bs-toggle="dropdown"
                  aria-expanded="false"><i class="icon-more-alt"></i></button>
                <div class="dropdown-menu dropdown-menu-end" aria-labelledby="growthdropdown"><a class="dropdown-item"
                    href="#">Weekly</a><a class="dropdown-item" href="#">Monthly</a><a class="dropdown-item"
                    href="#">Yearly</a></div>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="growth-wrapper">
              <apexchart height="150" type="line" :options="apexDashboard.options6" :series="apexDashboard.series6">
              </apexchart>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { apexDashboard } from '@/data/comon'
export default {
  data() { return { apexDashboard: apexDashboard, } }
}
</script>