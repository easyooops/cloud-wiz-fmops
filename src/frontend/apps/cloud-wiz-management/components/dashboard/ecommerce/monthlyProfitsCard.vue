<template>
    <div class="col-xxl-3 col-md-6 box-col-6">
        <div class="card">
            <div class="card-header card-no-border">
                <h5>Monthly Profits</h5>
                <span class="f-light f-w-500 f-14">(Total profit growth of 30%)</span>
            </div>
            <div class="card-body pt-0">
                <div class="monthly-profit">
                    <apexchart height="271.3" type="donut" :options="ecomDashboard.options1"
                        :series="ecomDashboard.series1"></apexchart>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    ecomDashboard
} from "@/data/comon";

export default {
    data() {
        return {
            ecomDashboard: ecomDashboard,
        };
    },
};
</script>
    