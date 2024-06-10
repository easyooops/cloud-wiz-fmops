<template>
    <div class="col-xxl-5 col-xl-4 box-col-12">
        <div class="card recent-order">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Recent Orders</h5>
                    <div class="card-header-right-icon">
                        <DropDown1 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="recent-sliders">
                    <div class="nav nav-pills" id="v-pills-tab" role="tablist">
                        <button class="active frame-box" id="v-pills-shirt-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-shirt" type="button" role="tab" aria-controls="v-pills-shirt"
                            aria-selected="true">
                            <span class="frame-image"><img src="/images/dashboard-2/order/1.png"
                                    alt="vector T-shirt" /></span>
                        </button>
                        <button class="frame-box" id="v-pills-television-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-television" type="button" role="tab" aria-controls="v-pills-television"
                            aria-selected="false">
                            <span class="frame-image"><img src="/images/dashboard-2/order/2.png"
                                    alt="vector television" /></span>
                        </button>
                        <button class="frame-box" id="v-pills-headphone-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-headphone" type="button" role="tab" aria-controls="v-pills-headphone"
                            aria-selected="false">
                            <span class="frame-image"><img src="/images/dashboard-2/order/3.png"
                                    alt="vector headphone" /></span>
                        </button>
                        <button class="frame-box" id="v-pills-chair-tab" data-bs-toggle="pill"
                            data-bs-target="#v-pills-chair" type="button" role="tab" aria-controls="v-pills-chair"
                            aria-selected="false">
                            <span class="frame-image"><img src="/images/dashboard-2/order/4.png"
                                    alt="vector chair" /></span>
                        </button>
                        <button class="frame-box" id="v-pills-lamp-tab" data-bs-toggle="pill" data-bs-target="#v-pills-lamp"
                            type="button" role="tab" aria-controls="v-pills-lamp" aria-selected="false">
                            <span class="frame-image"><img src="/images/dashboard-2/order/5.png" alt="vector lamp" /></span>
                        </button>
                    </div>
                    <div class="tab-content" id="v-pills-tabContent">
                        <div class="tab-pane fade show active" id="v-pills-shirt" role="tabpanel"
                            aria-labelledby="v-pills-shirt-tab">
                            <ShirtTable />
                        </div>
                        <div class="tab-pane fade" id="v-pills-television" role="tabpanel"
                            aria-labelledby="v-pills-television-tab">
                            <TelevisionTable />
                        </div>
                        <div class="tab-pane fade" id="v-pills-headphone" role="tabpanel"
                            aria-labelledby="v-pills-headphone-tab">
                            <HeadphoneTable />
                        </div>
                        <div class="tab-pane fade" id="v-pills-chair" role="tabpanel" aria-labelledby="v-pills-chair-tab">
                            <ChairTable />
                        </div>
                        <div class="tab-pane fade" id="v-pills-lamp" role="tabpanel" aria-labelledby="v-pills-lamp-tab">
                            <LampTable />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown1 from "../base/dropDown1.vue";
import ShirtTable from "./recentOrderComponents/shirtTable.vue"
import TelevisionTable from "./recentOrderComponents/televisionTable.vue";
import HeadphoneTable from "./recentOrderComponents/headphoneTable.vue";
import ChairTable from "./recentOrderComponents/chairTable.vue";
import LampTable from "./recentOrderComponents/lampTable.vue";
export default {
    components: {
        DropDown1,
        ShirtTable,
        TelevisionTable,
        HeadphoneTable,
        ChairTable,
        LampTable
    },
};
</script>
    