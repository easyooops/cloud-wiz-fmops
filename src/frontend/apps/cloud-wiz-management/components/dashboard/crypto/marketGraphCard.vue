<template>
    <div class="col-xl-12">
        <div class="card market-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Market Graph</h5>
                    <ul class="nav nav-tabs custom-tab" id="tabdesign" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="hour-tab" data-bs-toggle="tab" data-bs-target="#hour" type="button"
                                role="tab" aria-selected="false">
                                1H
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="day-tab" data-bs-toggle="tab" data-bs-target="#day" type="button"
                                role="tab" aria-selected="false">
                                1D
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active" id="week-tab" data-bs-toggle="tab" data-bs-target="#week"
                                type="button" role="tab" aria-selected="true">
                                1W
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="month-tab" data-bs-toggle="tab" data-bs-target="#month"
                                type="button" role="tab" aria-selected="false">
                                1M
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="year-tab" data-bs-toggle="tab" data-bs-target="#year" type="button"
                                role="tab" aria-selected="false">
                                1Y
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="row m-0 overall-card">
                    <div class="col-xxl-8 col-xl-7 col-md-8 col-sm-7 p-0 box-col-7 col-ed-7 ">
                        <div class="market-chart-container">
                            <apexchart height="315" type="line" :options="cryptoDashboard?.options6"
                                :series="cryptoDashboard?.series6"></apexchart>
                        </div>
                    </div>
                    <div class="col-xxl-4 col-xl-5 col-md-4 col-sm-5 p-0 box-col-5 col-ed-5 ">
                        <div class="row g-sm-3 g-2">
                            <div class="col-md-12" v-for="market in markets" :key="market">
                                <div class="light-card balance-card align-items-center">
                                    <h6 class="f-w-400 f-14 mb-0">{{ market.name }}</h6>
                                    <div class="ms-auto text-end">
                                        <span :class="market.balanceClass">{{ market.balance }}</span>
                                    </div>
                                </div>
                            </div>
                            <div class="col-md-12">
                                <button class="btn btn-outline-dark w-100" type="button">
                                    See All Balance
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    cryptoDashboard
} from "@/data/comon";
import {
    markets
} from "@/data/dashboard/crypto.json"
export default {
    data() {
        return {
            cryptoDashboard: cryptoDashboard,
            markets: markets
        }
    },
}
</script>
    