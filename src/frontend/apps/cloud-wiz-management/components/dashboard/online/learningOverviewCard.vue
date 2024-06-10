<template>
    <div class="col-xxl-5 col-ed-7 col-xl-7 box-col-7">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">
                        Learning Overview<span class="f-14 f-w-500 ms-1 f-light">(75% activity growth)</span>
                    </h5>
                    <div class="card-header-right-icon">
                        <div class="dropdown icon-dropdown">
                            <button class="btn dropdown-toggle" id="learningButton" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                <i class="icon-more-alt"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-end" aria-labelledby="learningButton">
                                <a class="dropdown-item" href="#">Today</a><a class="dropdown-item" href="#">Tomorrow</a><a
                                    class="dropdown-item" href="#">Yesterday</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="learning-wrap">
                    <div id="learning-chart">
                        <apexchart height="280" type="line" :options="onlineDashboard.options1"
                            :series="onlineDashboard.series1"></apexchart>
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
    