<template>
    <div class="col-xxl-4 col-xl-5 col-md-6 col-sm-7 notification box-col-6">
        <div class="card height-equal">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Activity</h5>
                    <div class="card-header-right-icon">
                        <DropDown2 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <ul>
                    <li class="d-flex" v-for="item in activities" :key="item">
                        <div :class="item.class"></div>
                        <div class="w-100 ms-3">
                            <p class="d-flex justify-content-between mb-2">
                                <span class="date-content light-background">{{ item.date }}</span><span>{{ item.day
                                }}</span>
                            </p>
                            <h6>
                                {{ item.title }}<span class="dot-notification"></span>
                            </h6>
                            <p class="f-light">
                                {{ item.decription }}
                            </p>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown2 from "../base/dropDown2.vue";
import {
    activities
} from "@/data/dashboard/default"
import {
    apexDashboard
} from "@/data/comon";
export default {
    components: {
        DropDown2
    },
    data() {
        return {
            apexDashboard: apexDashboard,
            activities: activities
        };
    },
}
</script>
    