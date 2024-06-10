<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
              <div class="card">
                <div class="card-header">
                  <h5>Pie Chart <span class="digits">2</span></h5>
                </div>
                <div class="card-body p-0 chart-block">
                  <GChart
                    class="chart-overflow" 
                    id="pie-chart1"
                    type="PieChart"
                    :data="pie_chart.chartData_1"
                    :options="pie_chart.options_1"
                  />
                </div>
              </div>
            </div>
             <div class="col-sm-12 col-xl-6 box-col-6">
              <div class="card">
                <div class="card-header">
                  <h5>Pie Chart <span class="digits">3</span></h5>
                </div>
                <div class="card-body p-0 chart-block">
                   <GChart
                    class="chart-overflow" 
                    id="pie-chart2"
                    type="PieChart"
                    :data="pie_chart.chartData_1"
                    :options="pie_chart.options_2"
                  />
                </div>
              </div>
            </div>
            
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#7366FF';
var secondary = localStorage.getItem('secondary_color') || '#FF3364';

import { GChart } from "vue-google-charts";
export default {
  components:{
      GChart 
  },
  data(){
      return{
            chartsLib: null, 
             pie_chart: {
                   chartData_1: [
          ['Task', 'Hours per Day'],
          ['Work',     5],
          ['Eat',      10],
          ['Commute',  15],
          ['Watch TV', 20],
          ['Sleep',    25]
        ],
          chartData_2: [
          ['Task', 'Hours per Day'],
          ['Work',     2],
          ['Eat',      2],
          ['Commute',  11],
          ['Watch TV', 2],
          ['Sleep',    7]
        ],
         options_1: { 
          title: 'My Daily Activities',
          width:'100%',
          height: 300,
           colors: [primary, primary, "#54BA4A", "#16C7F9", "#FFAA05"]
        },
         options_2: { 
          title: 'My Daily Activities',
          is3D: true,
          width:'100%',
          height: 300,
         colors: [secondary, primary, "#16C7F9", "#FFAA05", "#54BA4A"]
        },
         
             }
      }
  }
}
</script>