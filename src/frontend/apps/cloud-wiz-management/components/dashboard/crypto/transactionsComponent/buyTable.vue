<template>
    <div class="table-responsive recent-table transaction-table">
        <table class="table">
            <tbody>
                <tr v-for="buy in buys" :key="buy">
                    <td>
                        <div class="d-flex">
                            <vue-feather :class="buy.iconClass" :type="buy.trandingClass"></vue-feather>
                            <div>
                                <h6 class="f-14 mb-0">{{ buy.companyStatus }}</h6>
                                <span class="f-light">{{ buy.date }}</span>
                            </div>
                        </div>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ buy.number }}</span>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ buy.amount }}</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
import {
    buys,
} from "@/data/dashboard/crypto.json"
export default {
    data() {
        return {
            buys: buys,
        }
    },
}
</script>