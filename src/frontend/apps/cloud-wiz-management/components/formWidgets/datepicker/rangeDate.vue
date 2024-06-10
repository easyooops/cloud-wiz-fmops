<template>
    <div class="mb-3 row g-3">
        <label class="col-sm-3 col-form-label text-sm-end">Range of dates</label>
        <div class="col-xl-5 col-sm-9">
            <Datepicker1 class="datepicker-here form-control digits" :multi="true" v-model="date1" range data-language="en">
            </Datepicker1>
        </div>
    </div>
</template>
<script>

import Datepicker from "vue3-datepicker";
import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from 'vue';
export default {
    components: {
        Datepicker,
        Datepicker1,
    },
    data() {
        return {

            date1: [this.startDate, this.endDate],

        }
    },
    setup() {
        const date3 = ref();

        return {
            date3,
        }
    }
}
</script>
