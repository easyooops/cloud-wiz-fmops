<template>
  <div class="col-xxl-8 col-xl-5 col-md-6 box-col-6">
    <div class="row">
      <div class="col-xl-12">
        <div class="card growth-wrap">
          <div class="card-header card-no-border pb-0">
            <div class="header-top">
              <h5>Daily Expense</h5>
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
              <apexchart height="150" type="line" :options="apexDashboard.options7" :series="apexDashboard.series6">
              </apexchart>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { apexDashboard } from '~/data/comon'
export default {
  data() { return { apexDashboard: apexDashboard, } }
}
</script>