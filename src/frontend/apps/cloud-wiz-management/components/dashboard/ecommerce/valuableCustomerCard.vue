<template>
    <div class="col-xxl-3 col-md-5 col-sm-6 box-col-5">
        <div class="appointment">
            <div class="card">
                <div class="card-header card-no-border">
                    <div class="header-top">
                        <h5 class="m-0">Valuable Customer</h5>
                        <div class="card-header-right-icon">
                            <DropDown1 />
                        </div>
                    </div>
                </div>
                <div class="card-body pt-0">
                    <div class="appointment-table customer-table table-responsive">
                        <table class="table table-bordernone">
                            <tbody>
                                <tr v-for="item in valuableCustomer" :key="item">
                                    <td>
                                        <img class="img-fluid img-40 rounded-circle me-2" :src="getImgURL(item.image)"
                                            alt="user" />
                                    </td>
                                    <td class="img-content-box">
                                        <a class="f-w-500">
                                            <NuxtLink to="/users/profile">{{ item.name }}</NuxtLink>
                                        </a><span class="f-light">{{ item.email }}</span>
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
import {
    valuableCustomer
} from "@/data/dashboard/ecommerce.json"
import DropDown1 from "../base/dropDown1.vue"
export default {
    components: {
        DropDown1
    },
    data() {
        return {
            valuableCustomer: valuableCustomer
        }
    },
    methods: {
        getImgURL(path) {
            return "/images/dashboard/" + path
        }
    }
}
</script>
    