<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
             <div class="card">
               <div class="card-header">
                 <h5>Pie Chart <span class="digits">4</span></h5>
               </div>
               <div class="card-body p-0 chart-block">
                  <GChart
                   class="chart-overflow" 
                   id="pie-chart4"
                   type="PieChart"
                   :data="pie_chart.chartData_4"
                   :options="pie_chart.options_4"
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
                  chartData_4: [
         ['Task', 'Hours per Day'],
         ['Work',     5],
         ['Eat',      10],
         ['Commute',  15],
         ['Watch TV', 20],
         ['Sleep',    25]
       ],
        
        options_4: { 
         title: 'My Daily Activities',
        pieHole: 0.4,
         width:'100%',
         height: 300,
        colors: [secondary, primary, "#54BA4A", "#FFAA05", "#16C7F9"]
       },
        
            }
     }
 }
}
</script>