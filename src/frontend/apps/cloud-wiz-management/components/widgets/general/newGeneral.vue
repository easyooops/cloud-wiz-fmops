<template>
  <div class="col-xxl-5 col-xl-8 box-col-12">
    <div class="row g-sm-3 height-equal-2 widget-charts">
      <div class="col-sm-6">
        <div class="card small-widget mb-sm-0">
          <div class="card-body primary"> <span class="f-light">New Orders</span>
            <div class="d-flex align-items-end gap-1">
              <h4>2,435</h4><span class="font-primary f-12 f-w-500"><i class="icon-arrow-up"></i><span>+50%</span></span>
            </div>
            <div class="bg-gradient">
              <svg class="stroke-icon svg-fill">
                <use href="@/assets/svg/icon-sprite.svg#new-order"></use>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card small-widget mb-sm-0">
          <div class="card-body warning"><span class="f-light">New Customers</span>
            <div class="d-flex align-items-end gap-1">
              <h4>2,908</h4><span class="font-warning f-12 f-w-500"><i class="icon-arrow-up"></i><span>+20%</span></span>
            </div>
            <div class="bg-gradient">
              <svg class="stroke-icon svg-fill">
                <use href="@/assets/svg/icon-sprite.svg#customers"></use>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card small-widget mb-sm-0">
          <div class="card-body secondary"><span class="f-light">Average Sale</span>
            <div class="d-flex align-items-end gap-1">
              <h4>$389k</h4><span class="font-secondary f-12 f-w-500"><i
                  class="icon-arrow-down"></i><span>-10%</span></span>
            </div>
            <div class="bg-gradient">
              <svg class="stroke-icon svg-fill">
                <use href="@/assets/svg/icon-sprite.svg#sale"></use>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card small-widget mb-sm-0">
          <div class="card-body success"><span class="f-light">Gross Profit</span>
            <div class="d-flex align-items-end gap-1">
              <h4>$3,908</h4><span class="font-success f-12 f-w-500"><i class="icon-arrow-up"></i><span>+80%</span></span>
            </div>
            <div class="bg-gradient">
              <svg class="stroke-icon svg-fill">
                <use href="@/assets/svg/icon-sprite.svg#profit"></use>
              </svg>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card widget-1 widget-with-chart mb-xl-0">
          <div class="card-body">
            <div>
              <h4 class="mb-1">1,80k</h4><span class="f-light">Orders</span>
            </div>
            <div class="order-chart">
              <apexchart height="125" type="bar" :options="apexDashboard.options" :series="apexDashboard.series">
              </apexchart>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6">
        <div class="card widget-1 widget-with-chart mb-xl-0">
          <div class="card-body">
            <div>
              <h4 class="mb-1">6,90k</h4><span class="f-light">Profit</span>
            </div>
            <div class="profit-chart">
              <apexchart height="125" type="line" :options="apexDashboard.options2" :series="apexDashboard.series2">
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

  data() {
    return {
      apexDashboard: apexDashboard,
    };
  },

};
</script>
