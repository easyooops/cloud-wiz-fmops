<template>
    <div class="col-xxl-3 col-ed-6 col-md-5 col-sm-6 box-col-5">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Active Lessons</h5>
                    <div class="card-header-right-icon">
                        <a class="link-only" href="#">View <vue-feather type="arrow-right"></vue-feather></a>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <ul class="lessons-lists">
                    <li>
                        <img src="/images/dashboard-3/lessons/1.png" alt="ux icon" />
                        <div>
                            <h6 class="f-14 f-w-400 mb-0">UI/UX</h6>
                            <span class="f-light">Web design</span>
                        </div>
                        <div class="lesson-wrap ms-auto">
                            <div id="lessonChart1">
                                <apexchart height="60.75" type="donut" :options="onlineDashboard.options4"
                                    :series="onlineDashboard.series4"></apexchart>
                            </div>
                        </div>
                    </li>
                    <li>
                        <img src="/images/dashboard-3/lessons/2.png" alt="vue icon" />
                        <div>
                            <h6 class="f-14 f-w-400 mb-0">Vue 3</h6>
                            <span class="f-light">JS Framework</span>
                        </div>
                        <div class="lesson-wrap ms-auto">
                            <div id="lessonChart2">
                                <apexchart height="60.75" type="donut" :options="onlineDashboard.options5"
                                    :series="onlineDashboard.series5"></apexchart>
                            </div>
                        </div>
                    </li>
                    <li>
                        <img src="/images/dashboard-3/lessons/3.png" alt="bootstrap icon" />
                        <div>
                            <h6 class="f-14 f-w-400 mb-0">Bootstrap 5</h6>
                            <span class="f-light">Framework</span>
                        </div>
                        <div class="lesson-wrap ms-auto">
                            <div id="lessonChart3">
                                <apexchart height="60.75" type="donut" :options="onlineDashboard.options6"
                                    :series="onlineDashboard.series6"></apexchart>
                            </div>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    onlineDashboard
} from "@/data/comon";



export default {
    data() {
        return {
            onlineDashboard: onlineDashboard,

        };
    },
};
</script>
    