<template>
  <div class="col-sm-12 col-xl-12 box-col-12">
    <div class="card">
      <div class="card-header">
        <h3>Candlestick Chart</h3>
      </div>
      <div class="card-body">
        <div id="candlestick">
          <apexchart type="candlestick" height="350" :series="series" :options="chartOptions"></apexchart>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#24695c';
var secondary = localStorage.getItem('secondary_color') || '#ba895d';
import { chartData } from "@/data/chart-data"
export default {
  data() {
    return {
      series: [{
        data: chartData
      }],
      chartOptions: {
        chart: {
          height: 350,
          type: 'candlestick',
          toolbar: {
            show: false
          }
        },
        plotOptions: {
          candlestick: {
            colors: {
              upward: primary,
              downward: secondary
            }
          }
        },
        title: {
          text: 'CandleStick Chart',
          align: 'left'
        },
        xaxis: {
          type: 'datetime'
        },
        yaxis: {
          tooltip: {
            enabled: true
          }
        },
        colors: ['#000000']
      }
    }
  },

}
</script>