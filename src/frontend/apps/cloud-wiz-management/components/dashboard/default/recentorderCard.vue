<template>
    <div class="col-xxl-4 col-xl-7 col-md-6 col-sm-5 box-col-6">
        <div class="card height-equal">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Recent Orders</h5>
                    <div class="card-header-right-icon">
                        <dropDown3 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="row recent-wrapper">
                    <div class="col-xl-6">
                        <div class="recent-chart">
                            <apexchart height="290.7" type="radialBar" :options="apexDashboard.options4"
                                :series="apexDashboard.series4"></apexchart>
                        </div>
                    </div>
                    <div class="col-xl-6">
                        <ul class="order-content">
                            <li v-for="item in items" :key="item">
                                <span :class="item.class"> </span>
                                <div>
                                    <span class="f-light f-w-500">{{ item.status }}</span>
                                    <h4 class="mt-1 mb-0">
                                        {{ item.orders
                                        }}<span class="f-light f-14 f-w-400 ms-1">({{ item.orderperiod }})
                                        </span>
                                    </h4>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    apexDashboard
} from "@/data/comon";
import dropDown3 from '../base/dropDown3.vue';
export default {
    components: {
        dropDown3
    },
    data() {
        return {
            apexDashboard: apexDashboard,
            items: [{
                status: "Cancelled",
                orders: "2,302",
                orderperiod: "Last 6 Month",
                class: "recent-circle bg-primary",
            },
            {
                status: "Delivered",
                orders: "9,302",
                orderperiod: "Last 6 Month",
                class: "recent-circle bg-info",
            },
            ],
        };
    },
};
</script>
    