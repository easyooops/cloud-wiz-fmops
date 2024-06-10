<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
    <div class="card">
      <div class="card-header"> 
        <h3>Basic Area Chart </h3>
      </div>
      <div class="card-body">
                    <div id="basic-apex">
                        <apexchart
                    type="area"
                    height="350"
                    ref="chart"
                    :options="chartOptions"
                    :series="series"
                  ></apexchart>
                    </div>
                  </div>
                </div>
              </div>
</template>
<script>
import chart from "@/data/chart.json";
var primary = localStorage.getItem('primary_color') || '#24695c';
export default {
    data(){
        return{
             series: [
        {
          name: "STOCK ABC",
          data: chart.monthDataSeries1.prices,
        },
      ],
       chartOptions: {
     chart: {
        height: 350,
        type: 'area',
        zoom: {
            enabled: false
        },
        toolbar:{
          show: false
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'straight'
    },
    title: {
        text: 'Fundamental Analysis of Stocks',
        align: 'left'
    },
    subtitle: {
        text: 'Price Movements',
        align: 'left'
    },
    labels: chart.monthDataSeries1.dates,
    xaxis: {
        type: 'datetime',
    },
    yaxis: {
        opposite: true
    },
    legend: {
        horizontalAlign: 'left'
    },
    colors:[primary]
        }
        }
    },
     mounted() {
    this.series[0].data = chart.monthDataSeries1.prices;
  },
}
</script>