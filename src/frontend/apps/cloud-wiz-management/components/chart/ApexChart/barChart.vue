<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
    <div class="card">
      <div class="card-header">
        <h3>Bar chart</h3>
      </div>
      <div class="card-body">
                    <div id="basic-bar">
                        <apexchart
            type="bar"
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
var primary = localStorage.getItem('primary_color') || '#24695c';
export default {
    data(){
        return{
          series: [
            {
              data: [400, 430, 448, 470, 540, 580, 690, 1100, 1200, 1380],
            },
          ],
          chartOptions: { 
              chart: {
        height: 350,
        type: 'bar',
        toolbar:{
          show: false
        }
    },
    plotOptions: {
        bar: {
            horizontal: true,
        }
    },
    dataLabels: {
        enabled: false
    },
    
    xaxis: {
        categories: ['South Korea', 'Canada', 'United Kingdom', 'Netherlands', 'Italy', 'France', 'Japan', 'United States', 'China', 'Germany'],
    },
    colors:[primary]
}
          }
        }
    }

</script>