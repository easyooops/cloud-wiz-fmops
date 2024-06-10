<template>
    <Breadcrumbs main="Dashboard" title="Social" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-xxl-3 col-ed-4 col-xl-4 box-col-4">
                <div class="row">
                    <welcomeCard />
                    <mobileApplicationCard />
                </div>
            </div>
            <div class="col-xxl-6 col-ed-8 col-xl-8 box-col-8e">
                <div class="row">
                    <facebookCard />
                    <instagramCard />
                    <twitterCard />
                    <instagramSubscribersCard />
                    <photoLinkClicksCard />
                </div>
            </div>
            <div class="col-xl-3 col-ed-none d-xxl-block d-lg-none box-col-none">
                <div class="row">
                    <followerGenderCard />
                    <facebookCampaignCard />
                </div>
            </div>
            <allCampaignsCard />
            <viewsCard />
        </div>
    </div>
    </template>
    
    <script>
    import welcomeCard from './welcomeCard.vue';
    import mobileApplicationCard from './mobileApplicationCard.vue';
    import facebookCard from './facebookCard.vue';
    import instagramCard from './instagramCard.vue';
    import twitterCard from './twitterCard.vue';
    import instagramSubscribersCard from './instagramSubscribersCard.vue';
    import photoLinkClicksCard from './photoLinkClicksCard.vue';
    import followerGenderCard from './followerGenderCard.vue';
    import facebookCampaignCard from './facebookCampaignCard.vue';
    import allCampaignsCard from './allCampaignsCard.vue';
    import viewsCard from './viewsCard.vue';
    
    export default {
        components: {
            welcomeCard,
            mobileApplicationCard,
            facebookCard,
            instagramCard,
            twitterCard,
            instagramSubscribersCard,
            photoLinkClicksCard,
            followerGenderCard,
            facebookCampaignCard,
            allCampaignsCard,
            viewsCard
        }
    };
    </script>
    