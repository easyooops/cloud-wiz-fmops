<template>
    <div class="col-xl-7">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">All Campaigns</h5>
                    <div class="card-header-right-icon">
                        <DropDown1 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0 campaign-table">
                <div class="recent-table table-responsive currency-table">
                    <table class="table">
                        <thead>
                            <tr>
                                <th class="f-light">AD Platform</th>
                                <th class="f-light">Campaign</th>
                                <th class="f-light">GEO</th>
                                <th class="f-light">Profitability</th>
                                <th class="f-light">Max Participation Avai.</th>
                                <th class="f-light">Status</th>
                                <th class="f-light">Create</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="campaign in campaigns" :key="campaign">
                                <td :class="campaign.tdBorderIcon">
                                    <div>
                                        <div class="social-circle">
                                            <i :class="campaign.platformIcon"></i>
                                        </div>
                                    </div>
                                </td>
                                <td>{{ campaign.campaign }}</td>
                                <td>{{ campaign.geo }}</td>
                                <td>
                                    <div class="change-currency">
                                        <vue-feather :class="campaign.profitabilityIcon"
                                            :type="campaign.type"></vue-feather>{{ campaign.profitability }}
                                    </div>
                                </td>
                                <td>{{ campaign.maxParticipation }}</td>
                                <td>
                                    <button :class="campaign.statusClass">{{ campaign.status }}</button>
                                </td>
                                <td>
                                    <button class="plus-btn">+</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown1 from "../base/dropDown1.vue";
import {
    campaigns
} from "@/data/dashboard/social.json"

export default {
    components: {
        DropDown1,

    },
    data() {
        return {
            campaigns: campaigns
        }
    },
}
</script>
    