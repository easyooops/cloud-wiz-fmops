<template>
  <div class="col-sm-12 col-xl-6 box-col-12">
    <div class="card">
      <div class="card-header">
        <h3>
          3d Bubble Chart </h3>
      </div>
      <div class="card-body">
        <div id="chart-bubble">
          <apexchart height="350" type="bubble" :options="chartOptions" :series="series"></apexchart>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

var primary = localStorage.getItem('primary_color') || '#24695c';
var secondary = localStorage.getItem('secondary_color') || '#ba895d';
export default {
  data() {
    return {
      series: [
        {
          name: 'Product1',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, { min: 10, max: 60, }),
        },
        {
          name: 'Product2',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, { min: 10, max: 60, }),
        },
        {
          name: 'Product3',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10, max: 60,
          }),
        },
        {
          name: 'Product4',
          data: this.generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
            min: 10,
            max: 60,
          }),
        },
      ],
      chartOptions: {
        chart: {
          height: 350,
          type: 'bubble',
          toolbar: {
            show: false
          }
        },
        dataLabels: {
          enabled: false
        },

        fill: {
          type: 'gradient',
        },
        title: {
          text: '3D Bubble Chart'
        },
        xaxis: {
          tickAmount: 12,
          type: 'datetime',

          labels: {
            rotate: 0,
          }
        },
        yaxis: {
          max: 70
        },
        theme: {
          palette: 'palette2'
        },
        colors: [primary, secondary, '#222222', '#717171']
      }
    }
  },
  methods: {
    generateData(baseval, count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var y =
          Math.floor(Math.random() * (yrange.max - yrange.min + 1)) +
          yrange.min;
        var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;
        series.push([baseval, y, z]);
        baseval += 86400000;
        i++;
      }
      return series;
    },
  },
}
</script>