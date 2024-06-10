<template>
    <Breadcrumbs main="Dashboard" title="default" />

    <div class="container-fluid">
        <div class="row widget-grid">
            <welcomeCardVue />
            <purchasesaleCard />
            <orderprofitCard />
            <overallbalanceCard />
            <recentorderCard />
            <activityCard />
            <recentsalesCard />
            <timelineCard />
            <proaccountCard />
            <totalusersCard />
            <papernoteCard />
        </div>
    </div>
</template>
    
<script>
import welcomeCardVue from "./welcomeCard.vue";
import purchasesaleCard from "./purchasesaleCard.vue";
import orderprofitCard from './orderprofitCard.vue'
import overallbalanceCard from "./overallbalanceCard.vue";
import recentorderCard from "./recentorderCard.vue"
import activityCard from "./activityCard.vue";
import recentsalesCard from "./recentsalesCard.vue";
import timelineCard from "./timelineCard.vue"
import proaccountCard from "./proaccountCard.vue"
import totalusersCard from "./totalusersCard.vue"
import papernoteCard from './papernoteCard.vue';

export default {
    components: {
        welcomeCardVue,
        purchasesaleCard,
        orderprofitCard,
        overallbalanceCard,
        recentorderCard,
        activityCard,
        recentsalesCard,
        timelineCard,
        proaccountCard,
        totalusersCard,
        papernoteCard
    },
};
</script>
