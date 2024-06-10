<template>
    <div class="col-xl-12 col-sm-6">
        <div class="card widget-hover">
            <div class="card-body radial-progress-card">
                <div>
                    <h6 class="mb-0">Average Profit Per Day</h6>
                    <div class="sale-details">
                        <h5 class="font-secondary mb-0">89.6%</h5>
                        <span class="f-12 f-light f-w-500"><i data-feather="arrow-up"></i>+2.7%</span>
                    </div>
                    <p class="f-light">The point of using Lorem Ipsum</p>
                </div>
                <div class="radial-chart-wrap">
                    <apexchart height="96.4" type="radialBar" :options="cryptoDashboard?.options1"
                        :series="cryptoDashboard?.series1"></apexchart>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    cryptoDashboard
} from "@/data/comon";
export default {
    data() {
        return {
            cryptoDashboard: cryptoDashboard,
        };
    },
};
</script>
    