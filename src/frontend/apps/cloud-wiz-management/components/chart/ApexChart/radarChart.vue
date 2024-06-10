<template>
    <div class="col-sm-12 col-xl-6 box-col-6">
        <div class="card">
            <div class="card-header">
                <h3>Radar Chart </h3>
            </div>
            <div class="card-body">
                <div id="radarchart">
                    <apexchart height="350" type="radar" :options="chartOptions" :series="series"></apexchart>
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
                name: 'Series 1',
                data: [20, 100, 40, 30, 50, 80, 33],
            }],
            chartOptions: {
                chart: {
                    height: 350,
                    type: 'radar',
                    toolbar: {
                        show: false
                    }
                },
                series: [{
                    name: 'Series 1',
                    data: [20, 100, 40, 30, 50, 80, 33],
                }],
                labels: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
                plotOptions: {
                    radar: {
                        size: 140,
                        polygons: {
                            strokeColor: primary,
                            fill: {
                                colors: ['#f8f8f8', '#fff']
                            }
                        }
                    }
                },
                title: {
                    text: 'Radar with Polygon Fill'
                },

                colors: [secondary],
                markers: {
                    size: 4,
                    colors: ['#fff'],
                    strokeColor: primary,
                    strokeWidth: 2,
                },
                tooltip: {
                    y: {
                        formatter: function (val) {
                            return val
                        }
                    }
                },
                yaxis: {
                    tickAmount: 7,
                    labels: {
                        formatter: function (val, i) {
                            if (i % 2 === 0) {
                                return val
                            } else {
                                return ''
                            }
                        }
                    }
                },


            }
        }
    }
}
</script>