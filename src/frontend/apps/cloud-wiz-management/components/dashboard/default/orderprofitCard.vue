<template>
    <div class="col-xxl-auto col-xl-12 col-sm-6 box-col-6">
        <div class="row">
            <div class="col-xxl-12 col-xl-6 box-col-12">
                <div class="card widget-1 widget-with-chart">
                    <div class="card-body">
                        <div>
                            <h4 class="mb-1">1,80k</h4>
                            <span class="f-light">Orders</span>
                        </div>
                        <div class="order-chart">
                            <apexchart height="125" width="200" type="bar" :options="apexDashboard.options"
                                :series="apexDashboard.series"></apexchart>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-xxl-12 col-xl-6 box-col-12">
                <div class="card widget-1 widget-with-chart">
                    <div class="card-body">
                        <div>
                            <h4 class="mb-1">6,90k</h4>
                            <span class="f-light">Traffic</span>
                        </div>
                        <div class="profit-chart">
                            <apexchart height="146" type="line" :options="apexDashboard.options2"
                                :series="apexDashboard.series2"></apexchart>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    apexDashboard
} from "~/data/comon";
export default {
    data() {
        return {
            apexDashboard: apexDashboard,
        };
    },
}
</script>
    