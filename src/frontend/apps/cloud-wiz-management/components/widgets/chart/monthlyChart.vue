<template>
  <!-- Monthly Sale chart widget Start-->
  <div class="xl-50 col-xl-5 col-lg-12 box-col-6">
    <div class="small-chart-widget chart-widgets-small">
      <div class="card">
        <div class="card-header">
          <h5>Monthly Sales</h5>
          <div class="card-header-right">
            <ul class="list-unstyled card-option">
              <li><i class="fa fa-spin fa-cog"></i></li>
              <li><i class="view-html fa fa-code"></i></li>
              <li><i class="icofont icofont-maximize full-card"></i></li>
              <li><i class="icofont icofont-minus minimize-card"></i></li>
              <li><i class="icofont icofont-refresh reload-card"></i></li>
              <li><i class="icofont icofont-error close-card"></i></li>
            </ul>
          </div>
        </div>
        <div class="card-body">
          <div class="chart-container">
            <div class="row">
              <div class="col-12">
                <apexchart height="320" type="radar" :options="chart14.options" :series="chart14.series"></apexchart>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
  <!-- Monthly Sale chart widget Ends-->
  <!-- Uses chart widget Start-->
  <div class="xl-50 col-xl-7 col-lg-12 box-col-12">
    <div class="small-chart-widget chart-widgets-small">
      <div class="card">
        <div class="card-header">
          <h5>Uses</h5>
          <div class="card-header-right">
            <ul class="list-unstyled card-option">
              <li><i class="fa fa-spin fa-cog"></i></li>
              <li><i class="view-html fa fa-code"></i></li>
              <li><i class="icofont icofont-maximize full-card"></i></li>
              <li><i class="icofont icofont-minus minimize-card"></i></li>
              <li><i class="icofont icofont-refresh reload-card"></i></li>
              <li><i class="icofont icofont-error close-card"></i></li>
            </ul>
          </div>
        </div>
        <div class="card-body">
          <div class="chart-container">
            <div class="row">
              <div class="col-12">
                <apexchart height="320" type="bubble" :options="chart15.options" :series="chart15.series"></apexchart>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
  <!-- Uses chart widget Ends-->
</template>
<script>
import {
  chart
} from '@/data/comon'
export default {
  data() {
    return {
      chart14: chart.chart14,
      chart15: chart.chart15,
    }
  }
}
</script>