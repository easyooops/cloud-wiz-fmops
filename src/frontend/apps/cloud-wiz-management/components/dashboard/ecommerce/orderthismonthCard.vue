<template>
    <div class="col-xxl-4 col-sm-6 box-col-6">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Order this month</h5>
                    <div class="card-header-right-icon">
                        <DropDown1 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="light-card balance-card d-inline-block">
                    <h4 class="mb-0">
                        $12,000 <span class="f-light f-14">(15,080 To Goal)</span>
                    </h4>
                </div>
                <div class="order-wrapper">
                    <apexchart height="245" type="line" :options="ecomDashboard.options" :series="ecomDashboard.series">
                    </apexchart>
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

export default {
    components: {
        DropDown1
    },
    data() {
        return {
            ecomDashboard: ecomDashboard,
        }
    },
}
</script>
    