<template>
    <div class="col-xl-12 col-sm-6">
        <div class="card widget-hover">
            <div class="card-body radial-progress-card">
                <div>
                    <h6 class="mb-0">Average Sales Per Day</h6>
                    <div class="sale-details">
                        <h5 class="font-primary mb-0">45,908</h5>
                        <span class="f-12 f-light f-w-500">
                            <vue-feather type="arrow-up"></vue-feather>+5.7%
                        </span>
                    </div>
                    <p class="f-light">The point of using Lorem Ipsum</p>
                </div>
                <div class="radial-chart-wrap">
                    <apexchart height="96.4" type="radialBar" :options="cryptoDashboard?.options"
                        :series="cryptoDashboard?.series"></apexchart>
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
    