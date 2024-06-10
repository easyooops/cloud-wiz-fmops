<template>
    <div class="col-xl-5">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Views</h5>
                    <div class="card-header-right-icon">
                        <div class="dropdown">
                            <button class="btn dropdown-toggle" id="viewButton" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                Today
                            </button>
                            <div class="dropdown-menu dropdown-menu-end" aria-labelledby="viewButton">
                                <a class="dropdown-item" href="#">Today</a><a class="dropdown-item" href="#">Tomorrow</a><a
                                    class="dropdown-item" href="#">Yesterday</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="view-container">
                    <apexchart height="320" type="line" :options="socialDashboard.options7"
                        :series="socialDashboard.series7"></apexchart>
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
    