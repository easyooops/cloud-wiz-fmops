<template>
    <div class="col-md-4 col-sm-6">
        <div class="card social-widget widget-hover">
            <div class="card-body">
                <div class="d-flex align-items-center justify-content-between">
                    <div class="d-flex align-items-center gap-2">
                        <div class="social-icons">
                            <img src="/images/dashboard-5/social/1.png" alt="facebook icon" />
                        </div>
                        <span>Facebook</span>
                    </div>
                    <span class="font-success f-12 d-xxl-block d-xl-none">+22.9%</span>
                </div>
                <div class="social-content">
                    <div>
                        <h5 class="mb-1">12,098</h5>
                        <span class="f-light">Followers</span>
                    </div>
                    <div class="social-chart">
                        <apexchart height="96.4" type="radialBar" :options="socialDashboard.options"
                            :series="socialDashboard.series"></apexchart>
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
    