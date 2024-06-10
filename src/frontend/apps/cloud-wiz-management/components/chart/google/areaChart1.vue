<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
             <div class="card">
               <div class="card-header">
                 <h5>Area Chart <span class="digits">1</span></h5>
               </div>
               <div class="card-body p-0 chart-block">
                      <GChart
                   class="chart-overflow" 
                   id="area-chart1"
                   type="AreaChart"
                   :data="area_chart.chartData_1"
                   :options="area_chart.options_1"
                 />
               </div>
             </div>
           </div>
            <div class="col-sm-12 col-xl-6 box-col-6">
             <div class="card">
               <div class="card-header">
                 <h5>Area Chart <span class="digits">2</span></h5>
               </div>
               <div class="card-body p-0 chart-block">
                <GChart
                   class="chart-overflow" 
                   id="area-chart2"
                   type="AreaChart"
                   :data="area_chart.chartData_2"
                   :options="area_chart.options_2"
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
          area_chart: {
       chartData_1: [  
          ['Year', 'Sales', 'Expenses'],
     ['2013',  1000,      400],
     ['2014',  1170,      460],
     ['2015',  660,       1120],
     ['2016',  1030,      540]

       ],
       chartData_2: [  
         ['Year', 'Cars', 'Trucks' , 'Drones' , 'Segways'],
         ['2013',  100, 400, 2000, 400],
         ['2014',  500, 700, 530, 800],
         ['2015',  2000, 1000, 620, 120],
         ['2016',  120, 201, 2501, 540]
       ],
        options_1: {
         
     title: 'Company Performance',
     hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
     vAxis: {minValue: 0},
     width:'100%',
     height: 400,
     colors: [primary, secondary]
  
       },
        options_2: {
         title: 'Company Performance',
         hAxis: { title: 'Year',  titleTextStyle: { color: '#333' } },
         vAxis: { minValue: 0 },
         width:'100%',
         height: 400,
         colors: [ primary , secondary , "#51bb25", "#f8d62b"]
       }
          },
          
     }
 }
}
</script>