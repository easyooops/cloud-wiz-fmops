<template>
    <div class="col-md-8">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">
                        Instagram Subscribers<span class="f-14 f-w-500 ms-1 f-light">(75% activity growth)</span>
                    </h5>
                    <div class="card-header-right-icon">
                        <div class="dropdown icon-dropdown">
                            <button class="btn dropdown-toggle" id="subscribeButton" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                <i class="icon-more-alt"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-end" aria-labelledby="subscribeButton">
                                <a class="dropdown-item" href="#">Today</a><a class="dropdown-item" href="#">Tomorrow</a><a
                                    class="dropdown-item" href="#">Yesterday</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="subscriber-chart-container">
                    <apexchart height="255" type="line" :options="socialDashboard.options3"
                        :series="socialDashboard.series3"></apexchart>
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
    