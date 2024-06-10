<template>
<div>
    <Breadcrumbs main="Dashboard" title="e-commerce" />
    <div class="container-fluid">
        <div class="row size-column">
            <div class="col-xxl-10 col-md-12 box-col-8 grid-ed-12">
                <div class="row">
                    <allfourCard />
                    <valuableCustomerCard />
                    <orderthismonthCard />
                    <monthlyProfitsCard />
                    <orderOverviewCard />
                    <discoverProCard />
                    <visitorsCard />
                    <recetOrderCard />
                   
                </div>
            </div>
            <div class="col-xxl-2 col-xl-3 col-md-4 grid-ed-none box-col-4e d-xxl-block d-none">

                <topCategoriesCardVue/>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import allfourCard from "./allfourCard.vue"
import valuableCustomerCard from "./valuableCustomerCard.vue"
import orderthismonthCard from './orderthismonthCard.vue'
import monthlyProfitsCard from "./monthlyProfitsCard.vue"
import orderOverviewCard from "./orderOverviewCard.vue"
import discoverProCard from "./discoverProCard.vue"
import visitorsCard from "./visitorsCard.vue"
import recetOrderCard from "./recetOrderCard.vue"
import topCategoriesCardVue from './topCategoriesCard.vue'

export default {
    components: {
        allfourCard,
        valuableCustomerCard,
        orderthismonthCard,
        monthlyProfitsCard,
        orderOverviewCard,
        discoverProCard,
        visitorsCard,
        recetOrderCard,
        topCategoriesCardVue
    },
}
</script>