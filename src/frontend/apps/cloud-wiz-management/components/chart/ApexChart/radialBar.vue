<template>
    <div class="col-sm-12 col-xl-6 box-col-6">
                <div class="card">
                  <div class="card-header">
                    <h3>Radial Bar Chart</h3>
                  </div>
                  <div class="card-body">
                    <div id="circlechart">
                        <apexchart
                  height="320"
                  type="radialBar"
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
var secondary = localStorage.getItem('secondary_color') || '#ba895d';
export default {
    data(){
        return{
            series: [44, 55, 67, 83],
            chartOptions:{
                 chart: {
        height: 350,
        type: 'radialBar',
    },
    plotOptions: {
        radialBar: {
            dataLabels: {
                name: {
                    fontSize: '22px',
                },
                value: {
                    fontSize: '16px',
                },
                total: {
                    show: true,
                    label: 'Total',
                    formatter: function () {
                        return 249
                    }
                }
            }
        }
    },
    
    labels: ['Apples', 'Oranges', 'Bananas', 'Berries'],
    colors:[primary , secondary , '#222222', '#717171']

            }
        }
    }
}
</script>