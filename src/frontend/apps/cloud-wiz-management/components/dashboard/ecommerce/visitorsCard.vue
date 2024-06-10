<template>
    <div class="col-xxl-4 col-xl-4 col-sm-6 box-col-6">
        <div class="card visitor-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">
                        Visitors<span class="f-14 font-primary f-w-500 ms-1">
                            <svg class="svg-fill me-1">
                                <use href="@/assets/svg/icon-sprite.svg#user-visitor"></use>
                            </svg>(+2.8)</span>
                    </h5>
                    <div class="card-header-right-icon">
                        <div class="dropdown icon-dropdown">
                            <button class="btn dropdown-toggle" id="visitorButton" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                <i class="icon-more-alt"></i>
                            </button>
                            <div class="dropdown-menu dropdown-menu-end" aria-labelledby="visitorButton">
                                <a class="dropdown-item" href="#">Today</a><a class="dropdown-item" href="#">Tomorrow</a><a
                                    class="dropdown-item" href="#">Yesterday</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="visitors-container">
                    <div id="visitor-chart">
                        <apexchart height="285" type="bar" :options="ecomDashboard.options4"
                            :series="ecomDashboard.series4"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    ecomDashboard
} from "@/data/comon";

export default {
    data() {
        return {
            ecomDashboard: ecomDashboard,
        };
    },
};
</script>
    