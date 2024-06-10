<template>
  <div class="col-sm-12 box-col-12">
             <div class="card">
               <div class="card-header">
                 <h5>Combo Chart</h5>
               </div>
               <div class="card-body chart-block">
                  <GChart
                   class="chart-overflow" 
                   id="combo-chart"
                   type="ComboChart"
                   :data="combo_chart.chartData_1"
                   :options="combo_chart.options_1"
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
           combo_chart: {
       chartData_1: [  
         ['Month', 'Bolivia', 'Ecuador', 'Madagascar', 'Papua New Guinea', 'Rwanda', 'Average'],
         ['2004/05',  165,      938,         522,             998,           450,      614.6],
         ['2005/06',  135,      1120,        599,             1268,          288,      682],
         ['2006/07',  157,      1167,        587,             807,           397,      623],
         ['2007/08',  139,      1110,        615,             968,           215,      609.4],
         ['2008/09',  136,      691,         629,             1026,          366,      569.6]
       ],
       options_1:  {
         title : 'Monthly Coffee Production by Country',
         vAxis: { title: 'Cups' },
         hAxis: { title: 'Month' },
         seriesType: 'bars',
         series: { 5: { type: 'line' } },
         height: 500,
         fullWidth: true,
         colors: [primary, secondary, "#54BA4A", "#16C7F9", "#FFAA05"]
       }
     },
     }
 }
}
</script>