<template>
    <div class="col-lg-12 col-sm-6">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top gap-1">
                    <h5>Follower Gender</h5>
                    <div class="dropdown icon-dropdown">
                        <button class="btn dropdown-toggle" id="followerdropdown" type="button" data-bs-toggle="dropdown"
                            aria-expanded="false">
                            <i class="icon-more-alt"></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-end" aria-labelledby="followerdropdown">
                            <a class="dropdown-item" href="#">Weekly</a><a class="dropdown-item" href="#">Monthly</a><a
                                class="dropdown-item" href="#">Yearly</a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="follower-chart">
                    <apexchart height="181.5" type="radialBar" :options="socialDashboard.options6"
                        :series="socialDashboard.series6"></apexchart>
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
    