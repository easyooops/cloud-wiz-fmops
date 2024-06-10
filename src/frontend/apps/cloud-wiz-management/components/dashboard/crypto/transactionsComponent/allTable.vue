<template>
    <div class="table-responsive recent-table transaction-table">
        <table class="table">
            <tbody>
                <tr v-for="all in alls" :key="all">
                    <td>
                        <div class="d-flex">
                            <vue-feather :class="all.iconClass" :type="all.trandingClass"></vue-feather>
                            <div>
                                <h6 class="f-14 mb-0">{{ all.companyStatus }}</h6>
                                <span class="f-light">{{ all.date }}</span>
                            </div>
                        </div>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ all.number }}</span>
                    </td>
                    <td>
                        <span class="f-light f-w-500">{{ all.amount }}</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import {
    alls,
} from "@/data/dashboard/crypto.json"
export default {
    data() {
        return {
            alls: alls,

        }
    },
}
</script>
