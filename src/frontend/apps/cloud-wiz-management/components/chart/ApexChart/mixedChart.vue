<template>
    <div class="col-sm-12 col-xl-12 box-col-12">
        <div class="card">
            <div class="card-header">
                <h3>Mixed Chart</h3>
            </div>
            <div class="card-body">
                <div id="mixedchart">
                    <apexchart height="350" type="line" :options="chartOptions" :series="series"></apexchart>
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
            series: [{
                name: 'Column',
                type: 'column',
                data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30]
            }, {
                name: 'Area',
                type: 'area',
                data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43]
            }, {
                name: 'Line',
                type: 'line',
                data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39]
            }],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'line',
                    stacked: false,
                    toolbar: {
                        show: false
                    }
                },
                stroke: {
                    width: [0, 2, 5],
                    curve: 'smooth'
                },
                plotOptions: {
                    bar: {
                        columnWidth: '50%'
                    }
                },

                fill: {
                    opacity: [0.85, 0.25, 1],
                    gradient: {
                        inverseColors: false,
                        shade: 'light',
                        type: "vertical",
                        opacityFrom: 0.85,
                        opacityTo: 0.55,
                        stops: [0, 100, 100, 100]
                    }
                },
                labels: ['01/01/2003', '02/01/2003', '03/01/2003', '04/01/2003', '05/01/2003', '06/01/2003', '07/01/2003', '08/01/2003', '09/01/2003', '10/01/2003', '11/01/2003'],
                markers: {
                    size: 0
                },
                xaxis: {
                    type: 'datetime'
                },
                yaxis: {
                    min: 0
                },
                tooltip: {
                    shared: true,
                    intersect: false,
                    y: {
                        formatter: function (y) {
                            if (typeof y !== "undefined") {
                                return y.toFixed(0) + " views";
                            }
                            return y;

                        }
                    }
                },
                legend: {
                    labels: {
                        useSeriesColors: true
                    },
                },
                colors: [primary, secondary, '#222222']
            }
        }
    }
}
</script>