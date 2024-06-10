<template>
    <div class="mb-3 row g-3">
        <label class="col-sm-3 col-form-label text-sm-end">Month selection</label>
        <div class="col-xl-5 col-sm-9">
            <Datepicker1 class="datepicker-here form-control digits" v-model="month" monthPicker>
            </Datepicker1>

        </div>
    </div>
</template>
<script>
import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from 'vue';
export default {
    components: {

        Datepicker1,
    },

    setup() {
        const month = ref({
            month: new Date().getMonth(),
            year: new Date().getFullYear()
        });

        return {
            month
        }
    }
}
</script>
