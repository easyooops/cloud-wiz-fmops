<template>
    <div class="col-xxl-4 col-md-6 appointment-sec box-col-6">
        <div class="appointment">
            <div class="card">
                <div class="card-header card-no-border">
                    <div class="header-top">
                        <h5 class="m-0">Recent Sales</h5>
                        <div class="card-header-right-icon">
                            <DropDown2 />
                        </div>
                    </div>
                </div>
                <div class="card-body pt-0">
                    <div class="appointment-table table-responsive">
                        <table class="table table-bordernone">
                            <tbody>
                                <tr v-for="item in resentSales" :key="item">
                                    <td>
                                        <img class="img-fluid img-40 rounded-circle" :src="getImgURL(item.image)"
                                            alt="user" />
                                    </td>
                                    <td class="img-content-box">
                                        <a class="d-block f-w-500">
                                            <NuxtLink to="/users/profile">{{ item.name }}</NuxtLink>
                                        </a><span class="f-light">{{ item.time }}</span>
                                    </td>
                                    <td class="text-end">
                                        <p class="m-0 font-success">{{ item.amount }}</p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import DropDown2 from "../base/dropDown2.vue";
import {
    resentSales
} from "@/data/dashboard/default.json"
import {
    apexDashboard
} from "@/data/comon";
export default {
    components: {
        DropDown2
    },
    data() {
        return {
            apexDashboard: apexDashboard,
            resentSales: resentSales
        };
    },
    methods: {
        getImgURL(path) {
            return '/images/dashboard/' + path
        }
    }
}
</script>
    