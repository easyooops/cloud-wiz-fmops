<template>
    <div class="col-xxl-2 col-ed-3 col-xl-4 col-sm-6 box-col-5">
        <div class="card get-card">
            <div class="card-header card-no-border">
                <h5>Today Progress</h5>
                <span class="f-14 f-w-500 f-light">Your Daily Goal Almost Done!</span>
            </div>
            <div class="card-body pt-0">
                <div class="progress-chart-wrap">
                    <div id="progresschart">
                        <apexchart height="266.7" type="radialBar" :options="onlineDashboard.options"
                            :series="onlineDashboard.series"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import "@vuepic/vue-datepicker/dist/main.css";
import {
    onlineDashboard
} from "@/data/comon";

export default {
    data() {
        return {
            date1: new Date(),
            onlineDashboard: onlineDashboard,
        };
    },
};
</script>
    