<template>
  <div class="col-sm-12 box-col-12">
             <div class="card">
               <div class="card-header">
                 <h5>Bar-chart2</h5>
               </div>
               <div class="card-body chart-block">
                 <div id="bar-chart2">
                      <GChart
                   class="chart-overflow" 
                   id="bar-chart2"
                   type="BarChart"
                   :data="bar_chart.chartData_1"
                   :options="bar_chart.options_1"
                 />
                 </div>
               </div>
             </div>
           </div>
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#FFAA05';
var secondary = localStorage.getItem('secondary_color') || '#54BA4A';

import { GChart } from "vue-google-charts";
export default {
 components:{
     GChart 
 },
 data(){
     return{
           chartsLib: null, 
            bar_chart: {
       chartData_1: [  
         ['Element', 'Density', { role: 'style' } ],
         ['Copper', 10, primary],
         ['Silver', 12, secondary],
         ['Gold', 14, '#FF3364'],
         ['Platinum', 16, 'color: #7366FF']
       ],
       options_1:  {
         title: 'Density of Precious Metals, in g/cm^3',
         width:'100%',
         height: 400,
         bar: { groupWidth: '95%' },
         legend: { position: 'none' },
       }
     },
     }
 }
}
</script>