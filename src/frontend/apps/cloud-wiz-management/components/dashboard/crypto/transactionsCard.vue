<template>
    <div class="col-sm-12">
        <div class="card tranaction-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Transactions</h5>
                    <ul class="nav nav-tabs custom-tab" id="myTab" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active" id="all-tab" data-bs-toggle="tab" data-bs-target="#all" type="button" role="tab" aria-controls="all" aria-selected="true">
                                All
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="buy-tab" data-bs-toggle="tab" data-bs-target="#buy" type="button" role="tab" aria-controls="buy" aria-selected="false">
                                Buy
                            </button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link" id="sell-tab" data-bs-toggle="tab" data-bs-target="#sell" type="button" role="tab" aria-controls="sell" aria-selected="false">
                                Sell
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="card-body pt-0">
                <div class="tab-content" id="myTabContent">
                    <div class="tab-pane fade show active" id="all" role="tabpanel" aria-labelledby="all-tab">
                        <AllTable />
                    </div>
                    <div class="tab-pane fade" id="buy" role="tabpanel" aria-labelledby="buy-tab">
                        <BuyTableVue />
                    </div>
                    <div class="tab-pane fade" id="sell" role="tabpanel" aria-labelledby="sell-tab">
                        <SellTableVue />
                    </div>
                </div>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    import AllTable from "./transactionsComponent/allTable.vue"
    import BuyTableVue from './transactionsComponent/buyTable.vue'
    import SellTableVue from './transactionsComponent/sellTable.vue'
    
    export default {
        components: {
            AllTable,
            BuyTableVue,
            SellTableVue
        }
    }
    </script>
    