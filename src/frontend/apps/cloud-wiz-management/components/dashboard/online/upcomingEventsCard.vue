<template>
    <div class="col-xxl-3 col-ed-5 col-xl-5 col-md-6 box-col-5">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Upcoming Events</h5>
                    <DropDown1 />
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="upcoming-event-wrap">
                    <apexchart height="385" type="bar" :options="onlineDashboard.options3"
                        :series="onlineDashboard.series3"></apexchart>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import "@vuepic/vue-datepicker/dist/main.css";
import DropDown1 from "../base/dropDown1.vue"
import {
    onlineDashboard
} from "@/data/comon";

export default {
    components: {
        DropDown1
    },
    data() {
        return {
            date1: new Date(),
            onlineDashboard: onlineDashboard,
        };
    },
};
</script>
    