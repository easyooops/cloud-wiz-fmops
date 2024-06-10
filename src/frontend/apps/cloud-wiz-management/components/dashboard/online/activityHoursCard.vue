<template>
    <div class="col-xxl-4 col-ed-7 col-xl-7 col-md-6 box-col-7">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Activity Hours</h5>
                    <DropDown1 />
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="row m-0 overall-card">
                    <div class="col-xl-8">
                        <div class="chart-right">
                            <div class="row">
                                <div class="col-xl-12">
                                    <div class="card-body p-0">
                                        <div class="activity-wrap">
                                            <div id="activity-chart">
                                                <apexchart height="215" type="bar" :options="onlineDashboard.options2"
                                                    :series="onlineDashboard.series2"></apexchart>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-4 p-0">
                        <div class="row g-sm-3 g-2 mt-0">
                            <div class="col-xl-12 col-md-6 col-sm-4" v-for="activirtyhous in activirtyHours"
                                :key="activirtyhous">
                                <div class="light-card balance-card">
                                    <div>
                                        <span class="f-light">{{ activirtyhous.title }}</span>
                                        <h6 class="mt-1 mb-0">
                                            {{ activirtyhous.inNumber }}<span
                                                class="badge badge-light-success rounded-pill ms-1">{{
                                                    activirtyhous.inPercentage }}</span>
                                        </h6>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown1 from '../base/dropDown1.vue'
import "@vuepic/vue-datepicker/dist/main.css";
import {
    onlineDashboard
} from "@/data/comon";
import {
    activirtyHours
} from "@/data/dashboard/online.json"
export default {
    components: {
        DropDown1
    },
    data() {
        return {
            date1: new Date(),
            onlineDashboard: onlineDashboard,
            activirtyHours: activirtyHours
        };
    },
};
</script>
    