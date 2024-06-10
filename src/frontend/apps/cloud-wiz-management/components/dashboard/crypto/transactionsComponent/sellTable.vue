<template>
    <div class="table-responsive recent-table transaction-table">
        <table class="table">
            <tbody>
                <tr v-for="sell in sells" :key="sell">
                    <td>
                        <div class="d-flex">
                            <vue-feather :class="sell.iconClass" :type="sell.trandingClass"></vue-feather>
                            <div>
                                <h6 class="f-14 mb-0">{{ sell.companyStatus }}</h6>
                                <span class="f-light">{{ sell.date }}</span>
                            </div>
                        </div>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ sell.number }}</span>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ sell.amount }}</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import {
    sells
} from "@/data/dashboard/crypto.json"
export default {
    data() {
        return {
            sells: sells
        }
    },
}
</script>