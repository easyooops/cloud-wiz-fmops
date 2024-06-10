<template>
    <div class="mb-3 row g-3">
        <label class="col-sm-3 col-form-label text-sm-end">Disable days of week</label>
        <div class="col-xl-5 col-sm-9">
            <Datepicker1 class="datepicker-here form-control digits" v-model="date" :disabledDates="disabledDates"
                data-language="en"></Datepicker1>

        </div>
    </div>
</template>
<script>
import Datepicker from "vue3-datepicker";
import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref, computed } from 'vue';

export default {
    components: {
        Datepicker,
        Datepicker1,
    },
    setup() {
        const date = ref(new Date());
        const disabledDates = computed(() => {
            const today = new Date();

            const tomorrow = new Date(today)
            tomorrow.setDate(tomorrow.getDate() + 1)

            const afterTomorrow = new Date(tomorrow);
            afterTomorrow.setDate(tomorrow.getDate() + 1);

            return [tomorrow, afterTomorrow]
        })

        return {
            disabledDates,
            date,
        }
    }
}
</script>