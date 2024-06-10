<template>
    <div class="row">
        <div class="col-xl-4 col-md-12 box-col-12">
            <div class="card o-hidden">
                <div class="chart-widget-top">
                    <div class="row card-body pb-0 m-0">
                        <div class="col-xl-9 col-lg-8 col-9 p-0">
                            <h6 class="mb-2">Total Sale</h6>
                            <h4>$3654.00</h4><span>Compare to last month</span>
                        </div>
                        <div class="col-xl-3 col-lg-4 col-3 text-end p-0">
                            <h6 class="txt-success">+65%</h6>
                        </div>
                    </div>
                    <div>
                        <apexchart height="170" type="area" :options="chart1.options" :series="chart1.series"></apexchart>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-md-12 box-col-12">
            <div class="card o-hidden">
                <div class="chart-widget-top">
                    <div class="row card-body pb-0 m-0">
                        <div class="col-xl-9 col-lg-8 col-9 p-0">
                            <h6 class="mb-2">Total Project</h6>
                            <h4>12569</h4><span>Compare to last month</span>
                        </div>
                        <div class="col-xl-3 col-lg-4 col-3 text-end p-0">
                            <h6 class="txt-success">+65%</h6>
                        </div>
                    </div>
                    <apexchart height="170" type="area" v-bind="chart2"></apexchart>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-md-12 box-col-12">
            <div class="card o-hidden">
                <div class="chart-widget-top">
                    <div class="row card-body pb-0 m-0">
                        <div class="col-xl-9 col-lg-8 col-9 p-0">
                            <h6 class="mb-2">Total Product</h6>
                            <h4>93M</h4><span>Compare to last month</span>
                        </div>
                        <div class="col-xl-3 col-lg-4 col-3 text-end p-0">
                            <h6 class="txt-success">+65%</h6>
                        </div>
                    </div>
                    <apexchart class="flot-chart-placeholder" height="170" type="area" :options="chart3.options"
                        :series="chart3.series"></apexchart>
                    <div class="flot-chart-placeholder" id="chart-widget-top-third"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { chart } from '@/data/comon'
export default {
    data() {
        return {
            chart1: chart.chart1,
            chart2: chart.chart2,
            chart3: chart.chart3
        }
    }
}
</script>
