<template>
  <div class="col-sm-4 col-xxl-2">
    <div class="currency-widget warning height-equal widget-currency">
      <div class="d-flex">
        <div class="currency-icon-widget">
          <svg>
            <use href="@/assets/svg/icon-sprite.svg#beta"></use>
          </svg>
        </div>
        <div>
          <h6>Bitcoin <span class="f-light">BTC</span></h6>
        </div>
      </div>
      <div class="card">
        <div class="card-body d-flex">
          <div class="currency-chart-wrap">
            <apexchart height="115" type="line" :options="cryptoDashboard?.options3" :series="cryptoDashboard?.series3">
            </apexchart>
          </div>
          <div class="bg-light-warning text-center">
            <h5 class="mb-sm-0">$21,43</h5><span class="f-12 f-w-500 font-warning"><i class="me-1"
                data-feather="trending-up"></i>+50%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-4 col-xxl-2">
    <div class="currency-widget primary height-equal widget-currency">
      <div class="d-flex">
        <div class="currency-icon-widget">
          <svg>
            <use href="@/assets/svg/icon-sprite.svg#eth"></use>
          </svg>
        </div>
        <div>
          <h6>Ethereum <span class="f-light">ETC</span></h6>
        </div>
      </div>
      <div class="card">
        <div class="card-body d-flex">
          <div class="currency-chart-wrap">
            <apexchart height="115" type="line" :options="cryptoDashboard?.options4" :series="cryptoDashboard?.series4">
            </apexchart>
          </div>
          <div class="bg-light-primary text-center">
            <h5 class="mb-0">$7,450</h5><span class="f-12 f-w-500 font-primary"><i class="me-1"
                data-feather="trending-up"> </i>+35%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-4 col-xxl-2">
    <div class="currency-widget success height-equal widget-currency">
      <div class="d-flex">
        <div class="currency-icon-widget">
          <svg>
            <use href="@/assets/svg/icon-sprite.svg#ltc"></use>
          </svg>
        </div>
        <div>
          <h6>Leave Travel <span class="f-light">LTC</span></h6>
        </div>
      </div>
      <div class="card">
        <div class="card-body d-flex">
          <div class="currency-chart-wrap">
            <apexchart height="115" type="line" :options="cryptoDashboard?.options5" :series="cryptoDashboard?.series5">
            </apexchart>
          </div>
          <div class="bg-light-success text-center">
            <h5 class="mb-0">$2,198</h5><span class="f-12 f-w-500 font-success"><i class="me-1"
                data-feather="trending-up"> </i>+73%</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { cryptoDashboard } from '@/data/comon'
export default {
  data() {
    return {
      cryptoDashboard: cryptoDashboard
    }
  },
}
</script>