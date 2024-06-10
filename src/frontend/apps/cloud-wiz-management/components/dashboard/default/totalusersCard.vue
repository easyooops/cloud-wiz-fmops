<template>
    <div class="col-xxl-4 col-md-6 box-col-6 col-ed-6">
        <div class="row">
            <div class="col-xl-12">
                <div class="card">
                    <div class="card-header card-no-border">
                        <div class="header-top">
                            <h5>Total Users</h5>
                            <DropDown3 />
                        </div>
                    </div>
                    <div class="card-body pt-0">
                        <ul class="user-list">
                            <li>
                                <div class="user-icon primary">
                                    <div class="user-box">
                                        <vue-feather class="font-primary" type="user-plus"></vue-feather>
                                    </div>
                                </div>
                                <div>
                                    <h5 class="mb-1">178,098</h5>
                                    <span class="font-primary d-flex align-items-center"><i
                                            class="icon-arrow-up icon-rotate me-1"> </i><span
                                            class="f-w-500">+30.89</span></span>
                                </div>
                            </li>
                            <li>
                                <div class="user-icon success">
                                    <div class="user-box">
                                        <vue-feather class="font-success" type="user-minus"></vue-feather>
                                    </div>
                                </div>
                                <div>
                                    <h5 class="mb-1">178,098</h5>
                                    <span class="font-danger d-flex align-items-center"><i
                                            class="icon-arrow-down icon-rotate me-1"></i><span
                                            class="f-w-500">-08.89</span></span>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="col-xl-12">
                <div class="card growth-wrap">
                    <div class="card-header card-no-border">
                        <div class="header-top">
                            <h5>Followers Growth</h5>
                            <DropDown3 />
                        </div>
                    </div>
                    <div class="card-body pt-0">
                        <div class="growth-wrapper">
                            <apexchart height="200" type="line" :options="apexDashboard.options6"
                                :series="apexDashboard.series6"></apexchart>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown3 from "../base/dropDown3.vue"
import {
    apexDashboard
} from "@/data/comon";
export default {
    components: {
        DropDown3
    },
    data() {
        return {
            apexDashboard: apexDashboard,
        };
    },
}
</script>
    