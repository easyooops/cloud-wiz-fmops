<template>
    <div class="col-xxl-8 col-lg-12 box-col-12">
        <div class="card">
            <div class="card-header card-no-border">
                <h5>Overall balance</h5>
            </div>
            <div class="card-body pt-0">
                <div class="row m-0 overall-card">
                    <div class="col-xl-9 col-md-12 col-sm-7 p-0">
                        <div class="chart-right">
                            <div class="row">
                                <div class="col-xl-12">
                                    <div class="card-body p-0">
                                        <ul class="balance-data">
                                            <li>
                                                <span class="circle bg-warning"> </span><span
                                                    class="f-light ms-1">Earning</span>
                                            </li>
                                            <li>
                                                <span class="circle bg-primary"> </span><span
                                                    class="f-light ms-1">Expense</span>
                                            </li>
                                        </ul>
                                        <div class="current-sale-container">
                                            <apexchart height="305" type="bar" :options="apexDashboard.options3"
                                                :series="apexDashboard.series3"></apexchart>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-3 col-md-12 col-sm-5 p-0">
                        <div class="row g-sm-4 g-2">
                            <div class="col-xl-12 col-md-4" v-for="item in overallbalance" :key="item">
                                <div class="light-card balance-card widget-hover">
                                    <div class="svg-box">
                                        <svg class="svg-fill">
                                            <use :xlink:href="getImgURL(item.iconName)"></use>
                                        </svg>
                                    </div>
                                    <div>
                                        <span class="f-light">{{ item.title }}</span>
                                        <h6 class="mt-1 mb-0">{{ item.amount }}</h6>
                                    </div>
                                    <div class="ms-auto text-end">
                                        <dropdown1 />
                                        <span :class="item.balanceClass">{{ item.balance }}</span>
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
import dropdown1 from "../base/dropDown1.vue"
import {
    overallbalance
} from "@/data/dashboard/default.json"
import {
    apexDashboard
} from "@/data/comon";
export default {
    components: {
        dropdown1
    },
    data() {
        return {
            apexDashboard: apexDashboard,
            overallbalance: overallbalance
        };
    },
    methods: {
        getImgURL(path) {
            return '/svg/icon-sprite.svg/' + `#${path}`
        }
    },
}
</script>
