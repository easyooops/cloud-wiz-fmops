<template>
    <div class="col-xxl-9 box-col-12">
        <div class="card">
            <div class="card-header card-no-border">
                <h5>Order Overview</h5>
            </div>
            <div class="card-body pt-0">
                <div class="row m-0 overall-card overview-card">
                    <div class="col-xl-9 col-md-8 col-sm-7 p-0 box-col-7">
                        <div class="chart-right">
                            <div class="row">
                                <div class="col-xl-12">
                                    <div class="card-body p-0">
                                        <ul class="balance-data">
                                            <li>
                                                <span class="circle bg-secondary"></span><span
                                                    class="f-light ms-1">Refunds</span>
                                            </li>
                                            <li>
                                                <span class="circle bg-primary"> </span><span
                                                    class="f-light ms-1">Earning</span>
                                            </li>
                                            <li>
                                                <span class="circle bg-success"> </span><span
                                                    class="f-light ms-1">Order</span>
                                            </li>
                                        </ul>
                                        <div class="current-sale-container order-container">
                                            <div class="overview-wrapper">
                                                <apexchart height="265" type="line" :options="ecomDashboard.options2"
                                                    :series="ecomDashboard.series2"></apexchart>
                                            </div>
                                            <div class="back-bar-container">
                                                <apexchart height="195" type="bar" :options="ecomDashboard.options3"
                                                    :series="ecomDashboard.series3"></apexchart>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-3 col-md-4 col-sm-5 p-0 box-col-5">
                        <div class="row g-sm-3 g-2">
                            <div class="col-md-12" v-for="item in orderOverview" :key="item">
                                <div class="light-card balance-card widget-hover">
                                    <div class="svg-box">
                                        <svg class="svg-fill">
                                            <use :xlink:href="getImgURL(item.svgIcon)"></use>
                                        </svg>
                                    </div>
                                    <div>
                                        <span class="f-light">{{ item.title }}</span>
                                        <h6 class="mt-1 mb-0">{{ item.overviewInNumber }}</h6>
                                    </div>
                                    <div class="ms-auto text-end">
                                        <DropDown1 />
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
import DropDown1 from "../base/dropDown1.vue"
import {
    ecomDashboard
} from "@/data/comon";
import {
    orderOverview
} from "@/data/dashboard/ecommerce.json"
export default {
    components: {
        DropDown1
    },
    data() {
        return {
            ecomDashboard: ecomDashboard,
            orderOverview: orderOverview
        }
    },
    methods: {
        getImgURL(path) {
            return '/svg/icon-sprite.svg' + `#${path}`
        }
    }
}
</script>
    