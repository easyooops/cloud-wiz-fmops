<template>
    <div class="col-xxl-12 order-xxl-0 order-1">
        <div class="card portfolio-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">My Portfolio</h5>
                    <div class="card-header-right-icon">
                        <div class="dropdown">
                            <button class="btn dropdown-toggle" id="portfolioButton" type="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                BTC
                            </button>
                            <div class="dropdown-menu dropdown-menu-end" aria-labelledby="portfolioButton">
                                <a class="dropdown-item" href="#">ETH</a><a class="dropdown-item" href="#">USD</a><a
                                    class="dropdown-item" href="#">LTC</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-xxl-12 col-xl-7 col-sm-6 box-col-6">
                        <div class="portfolio-chart-container">
                            <apexchart height="298.7" type="radialBar" :options="cryptoDashboard?.options7"
                                :series="cryptoDashboard?.series7"></apexchart>
                        </div>
                    </div>
                    <div class="col-xxl-12 col-xl-5 col-sm-6 box-col-6">
                        <div class="portfolio-table recent-table table-responsive">
                            <table class="table">
                                <tbody>
                                    <tr v-for="portfolio in portfolios" :key="portfolio">
                                        <td>
                                            <div class="d-flex align-items-center gap-2">
                                                <div :class="portfolio.CurremcyClass">
                                                    <svg>
                                                        <use :xlink:href="getImgURL(portfolio.svgIcon)"></use>
                                                    </svg>
                                                </div>
                                                <div>
                                                    <h6 class="f-14 mb-1">{{ portfolio.coinName }}</h6>
                                                    <div class="d-flex align-items-center gap-1">
                                                        <span :class="portfolio.statusClass"></span><span class="f-light">{{
                                                            portfolio.status }}</span>
                                                    </div>
                                                </div>
                                            </div>
                                        </td>
                                        <td class="text-end">
                                            <h6 class="f-14 f-w-400 mb-1">{{ portfolio.totalCoin }}</h6>
                                            <span :class="portfolio.priceClass">{{ portfolio.price }}</span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    portfolios
} from "@/data/dashboard/crypto"
import {
    cryptoDashboard
} from "@/data/comon";
export default {
    data() {
        return {
            cryptoDashboard: cryptoDashboard,
            portfolios: portfolios
        };
    },
    methods: {
        getImgURL(path) {
            return '/svg/icon-sprite.svg/' + `#${path}`
        }
    }
};
</script>
    