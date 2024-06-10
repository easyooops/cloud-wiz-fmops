<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
    <div class="card">
      <div class="card-header">
        <h5>Area Spaline Chart </h5>
      </div>
      <div class="card-body">
        <div id="area-spaline">
          <apexchart type="area" height="350" :options="options" :series="series"></apexchart>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { storeToRefs } from 'pinia';
import { useLayoutStore } from '~~/store/layout';
var { primaryColor: primaryRef, secondaryColor: secondaryRef } = storeToRefs(useLayoutStore())
var primary = primaryRef.value || '#24695c';
var secondary = '#ba895d';
export default {
  watch: {
    primaryRef: {
      handler() {
        this.primaryColor = primaryRef.value
      }, deep: true
    },
    secondaryRef: {
      handler() {
        this.secondaryColor = secondaryRef.value
      }
    }
  },
  data() {
    return {
      primaryColor: '#24695c',
      secondaryColor: '#ba895d',
      options: {
        chart: {
          height: 350,
          type: 'area',
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },


        xaxis: {
          type: 'datetime',
          categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"],
        },
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
        colors: [primary, secondary]
      },
      series: [{
        name: 'series1',
        data: [31, 40, 28, 51, 42, 109, 100]
      }, {
        name: 'series2',
        data: [11, 32, 45, 32, 34, 52, 41]
      }]


    };
  },
};
</script>