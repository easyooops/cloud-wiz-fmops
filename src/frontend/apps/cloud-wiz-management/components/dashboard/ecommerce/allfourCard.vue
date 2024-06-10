<template>
    <div class="col-xxl-5 col-md-7 box-col-7">
        <div class="row">
            <div class="col-sm-12">
                <div class="card o-hidden">
                    <div class="card-body balance-widget">
                        <span class="f-w-500 f-light">Total Balance</span>
                        <h4 class="mb-3 mt-1 f-w-500 mb-0 f-22">
                            $<span class="counter">245,154.00 </span><span class="f-light f-14 f-w-400 ms-1">this
                                month</span>
                        </h4>
                        <a class="
                                  purchase-btn
                                  btn btn-primary btn-hover-effect
                                  f-w-500
                                " href="#">Tap Up Balance</a>
                        <div class="mobile-right-img">
                            <img class="left-mobile-img" src="/images/dashboard-2/widget-img.png" alt="" /><img
                                class="mobile-img" src="/images/dashboard-2/mobile.gif" alt="mobile with coin" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-6" v-for="allDetail in allDetails" :key="allDetail">
                <div class="card small-widget">
                    <div :class="allDetail.cardClass">
                        <span class="f-light">{{ allDetail.title }}</span>
                        <div class="d-flex align-items-end gap-1">
                            <h4>{{ allDetail.dataInNumber }}</h4>
                            <span :class="allDetail.spanClass"><i :class="allDetail.iconClass"></i><span>{{ allDetail.status
                            }}</span></span>
                        </div>
                        <div class="bg-gradient">
                            <svg class="stroke-icon svg-fill">
                                <use :xlink:href="getImgURL(allDetail.svgIcon)"></use>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {
    allDetails
} from "@/data/dashboard/ecommerce.json"
export default {
    data() {
        return {
            allDetails: allDetails
        }
    },
    methods: {
        getImgURL(path) {
            return '/svg/icon-sprite.svg/' + `#${path}`
        }
    }
}
</script>
