<template>
    <div class="row">
        <div class="col-md-12 box-col-12">
            <div class="card o-hidden">
                <div class="card-header">
                    <h5>Monthly History</h5>
                </div>
                <div class="bar-chart-widget">
                    <div class="bottom-content card-body">
                        <div class="row">
                            <div class="col-12">
                                <apexchart height="350" type="bar" :options="chart4.options" :series="chart4.series">
                                </apexchart>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-12 box-col-6 xl-50">
            <div class="card">
                <div class="card-header">
                    <h5>Skill Status</h5>
                </div>
                <div class="card-body">
                    <div class="chart-container skill-chart">
                        <apexchart height="350" type="radialBar" :options="chart6.options" :series="chart6.series">
                        </apexchart>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-6 col-lg-12 box-col-6 xl-50">
            <div class="card">
                <div class="card-header">
                    <div class="header-top">
                        <h5>Order Status</h5>
                        <div class="card-header-right-icon">
                            <div class="dropdown">
                                <button class="btn dropdown-toggle" id="dropdownMenuButton" type="button"
                                    data-bs-toggle="dropdown">Today</button>
                                <div class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton"><a
                                        class="dropdown-item" href="#">Today</a><a class="dropdown-item"
                                        href="#">Tomorrow</a><a class="dropdown-item" href="#">Yesterday</a></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="chart-container progress-chart">
                        <apexchart height="70" type="bar" :options="progress1.options" :series="progress1.series">
                        </apexchart>
                    </div>
                    <apexchart height="70" type="bar" :options="progress2.options" :series="progress2.series"></apexchart>
                    <apexchart height="70" type="bar" :options="progress3.options" :series="progress3.series"></apexchart>
                    <apexchart height="70" type="bar" :options="progress4.options" :series="progress4.series"></apexchart>
                    <apexchart height="70" type="bar" :options="progress5.options" :series="progress5.series"></apexchart>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {
    chart
} from '@/data/comon'
export default {
    data() {
        return {
            chart4: chart.chart4,
            chart6: chart.chart6,
            progress1: chart.progress1,
            progress2: chart.progress2,
            progress3: chart.progress3,
            progress4: chart.progress4,
            progress5: chart.progress5,

        }
    }
}
</script>
