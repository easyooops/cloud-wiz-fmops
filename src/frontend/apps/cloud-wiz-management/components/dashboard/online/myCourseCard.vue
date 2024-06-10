<template>
    <div class="col-xxl-5 col-ed-12 box-col-12">
        <div class="card course-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">My Course</h5>
                    <div class="card-header-right-icon">
                        <DropDown1 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="course-main-card">
                    <div class="course-wrapper" v-for="course in courses" :key="course">
                        <div class="course-icon-box">
                            <div class="icon-wrap">
                                <img :src="getImgURL(course.iconWrap)" alt="clock vector" />
                            </div>
                            <img class="arrow-bg" :src="getImgURL(course.backArrow)" alt="sqaure border arrow" />
                        </div>
                        <h6 class="f-14">{{ course.title }}</h6>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown1 from "../base/dropDown1.vue"
import "@vuepic/vue-datepicker/dist/main.css";
import {
    onlineDashboard
} from "@/data/comon";
import {
    courses
} from "@/data/dashboard/online.json"
export default {
    components: {
        DropDown1
    },
    data() {
        return {
            date1: new Date(),
            onlineDashboard: onlineDashboard,
            courses: courses
        };
    },
    methods: {
        getImgURL(path) {
            return "/images/dashboard-3/" + path
        }
    }
};
</script>
    