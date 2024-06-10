<template>
    <div class="col-md-4 col-sm-6">
        <div class="card social-widget widget-hover">
            <div class="card-body">
                <div class="d-flex align-items-center justify-content-between">
                    <div class="d-flex align-items-center gap-2">
                        <div class="social-icons">
                            <img src="/images/dashboard-5/social/2.png" alt="instagram icon" />
                        </div>
                        <span>Instagram</span>
                    </div>
                    <span class="font-success f-12 d-xxl-block d-xl-none">+27.4%</span>
                </div>
                <div class="social-content">
                    <div>
                        <h5 class="mb-1">15,080</h5>
                        <span class="f-light">Followers</span>
                    </div>
                    <div class="social-chart">
                        <apexchart height="96.4" type="radialBar" :options="socialDashboard.options1"
                            :series="socialDashboard.series1"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    socialDashboard
} from "@/data/comon";

export default {
    data() {
        return {
            socialDashboard: socialDashboard,
        };
    },
};
</script>
    