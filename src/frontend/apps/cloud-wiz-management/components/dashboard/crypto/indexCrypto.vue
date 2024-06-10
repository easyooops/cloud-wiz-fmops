<template>
    <Breadcrumbs main="Dashboard" title="Crypto" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-xxl-3 col-xl-4 box-col-4">
                <div class="row">
                    <welcomeCard />
                    <averageSalesCard />
                    <averageProfitCard />
                    <averageVisitsCard />
                    <transactionsCard />
                </div>
            </div>
            <div class="col-xxl-6 col-xl-8 box-col-8e">
                <div class="row">
                    <bitcoinEthreumLeaveCard />
                    <marketGraphCard />
                    <myCurrenciesCard />
                    <buyCoinsCard />
                    <sellCoinsCard />
                </div>
            </div>
            <div class="col-xxl-3 box-col-12">
                <div class="row box-order">
                    <yourBalanceCard />
                    <myPortfolioCard />
                    <activitiesCard />
                </div>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    import welcomeCard from "./welcomeCard.vue";
    import averageSalesCard from "./averageSalesCard.vue";
    import averageProfitCard from "./averageProfitCard.vue";
    import averageVisitsCard from "./averageVisitsCard.vue";
    import transactionsCard from "./transactionsCard.vue";
    import bitcoinEthreumLeaveCard from "./bitcoinEthreumLeaveCard.vue";
    import marketGraphCard from "./marketGraphCard.vue";
    import myCurrenciesCard from "./myCurrenciesCard.vue";
    import buyCoinsCard from "./buyCoinsCard.vue";
    import sellCoinsCard from "./sellCoinsCard.vue";
    import yourBalanceCard from "./yourBalanceCard.vue";
    import myPortfolioCard from "./myPortfolioCard.vue";
    import activitiesCard from "./activitiesCard.vue";
    export default {
        components: {
            welcomeCard,
            averageSalesCard,
            averageProfitCard,
            averageVisitsCard,
            transactionsCard,
            bitcoinEthreumLeaveCard,
            marketGraphCard,
            myCurrenciesCard,
            buyCoinsCard,
            sellCoinsCard,
            yourBalanceCard,
            myPortfolioCard,
            activitiesCard
    
        },
    };
    </script>
    