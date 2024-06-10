<template>
    <div class="col-xxl-12 col-sm-6 box-col-6">
        <div class="card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Activities</h5>
                    <div class="card-header-right-icon">
                        <DropDown3 />
                    </div>
                </div>
            </div>
            <div class="card-body pt-0 activity-card">
                <div class="appointment-table customer-table table-responsive">
                    <table class="table table-bordernone">
                        <tbody>
                            <tr v-for="activity in activities" :key="activity">
                                <td>
                                    <img class="img-fluid img-40 rounded-circle me-2" :src="getImgURL(activity.image)"
                                        alt="user" />
                                </td>
                                <td class="img-content-box">
                                    <a class="d-block f-w-500">
                                        <NuxtLink to="/users/profile"> {{ activity.name }}</NuxtLink>
                                    </a><span class="f-light">{{ activity.to }}</span>
                                </td>
                                <td class="text-end">
                                    <span :class="activity.bnbClass">{{ activity.bnb }}</span><span
                                        class="d-block f-light">{{ activity.number }}</span>
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
import DropDown3 from '../base/dropDown3.vue';
import {
    activities
} from "@/data/dashboard/crypto.json"
export default {
    components: {
        DropDown3
    },
    data() {
        return {
            activities: activities
        }
    },
    methods: {
        getImgURL(path) {
            return '/images/dashboard/' + path
        }
    }
}
</script>
    