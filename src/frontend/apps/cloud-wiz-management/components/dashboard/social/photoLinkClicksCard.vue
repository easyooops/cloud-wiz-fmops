<template>
    <div class="col-md-4">
        <div class="row">
            <div class="col-md-12 col-sm-6">
                <div class="card click-widgets widget-hover">
                    <div class="card-body">
                        <div class="dropdown icon-dropdown text-end">
                            <DropDown1 />
                        </div>
                        <div class="d-flex justify-content-around">
                            <div class="click-chart">
                                <apexchart height="165" type="line" :options="socialDashboard.options4"
                                    :series="socialDashboard.series4"></apexchart>
                            </div>
                            <div>
                                <h4 class="mb-0">%76</h4>
                                <span class="f-light d-block my-1">Photo Clicks</span><span
                                    class="font-success">+72.9%</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-12 col-sm-6">
                <div class="card click-widgets widget-hover">
                    <div class="card-body">
                        <div class="dropdown icon-dropdown text-end">
                            <DropDown1 />
                        </div>
                        <div class="d-flex justify-content-around">
                            <div class="click-chart">
                                <apexchart height="165" type="line" :options="socialDashboard.options5"
                                    :series="socialDashboard.series5"></apexchart>
                            </div>
                            <div>
                                <h4 class="mb-0">%89</h4>
                                <span class="f-light d-block my-1">Link Clicks</span><span
                                    class="font-secondary">79.9%</span>
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
    socialDashboard
} from "@/data/comon";
export default {
    components: {
        DropDown1
    },
    data() {
        return {
            socialDashboard: socialDashboard,
        };
    },
};
</script>
    