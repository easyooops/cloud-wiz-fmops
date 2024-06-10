<template>
  <!-- browser uses widget chart Start-->
  <div class="col-sm-12 box-col-12">
    <div class="donut-chart-widget">
      <div class="card">
        <div class="card-header">
          <h5>Stock Market</h5>
        </div>
        <div class="card-body">
          <apexchart height="500" type="candlestick" :options="candleChart9.options" :series="candleChart9.series">
          </apexchart>
        </div>
      </div>
    </div>
  </div>
  <!-- browser uses widget chart Endss-->
  <!-- status widget Start-->
  <div class="col-xl-5 col-lg-12 box-col-12">
    <div class="card">
      <div class="card-header">
        <h5>Finance</h5>
      </div>
      <div class="card-body">
        <div class="chart-container column-container">
          <apexchart height="350" type="bar" :options="chart7.options" :series="chart7.series"></apexchart>
        </div>
      </div>
    </div>
  </div>
  <div class="col-xl-7 col-lg-12 box-col-6">
    <div class="card">
      <div class="card-header">
        <h5>Order Status </h5>
      </div>
      <div class="card-body">
        <div class="chart-container">
          <apexchart height="350" type="line" :options="chart8.options" :series="chart8.series"></apexchart>
        </div>
      </div>
    </div>
  </div>
  <!-- status widget Ends-->
</template>
<script>
import {
  chart
} from '@/data/comon'
export default {
  data() {
    return {
      chart7: chart.chart7,
      chart8: chart.chart8,
      candleChart9: chart.candleChart9
    }
  }
}
</script>