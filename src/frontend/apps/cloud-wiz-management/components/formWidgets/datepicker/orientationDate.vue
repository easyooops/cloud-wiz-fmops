<template>
    <div class="mb-3 row g-3">
        <label class="col-sm-3 col-form-label text-sm-end">Orientation</label>
        <div class="col-xl-5 col-sm-9">
            <div class="form-row">
                <div class="col-md-12 mb-2">
                    <Datepicker1 class="datepicker-here form-control digits" position="left" v-model="date6"
                        data-language="en"></Datepicker1>
                </div>
                <div class="col-md-12 mb-2">
                    <Datepicker1 class="datepicker-here form-control digits" position="right" v-model="date7"
                        data-language="en"></Datepicker1>
                </div>
                <div class="col-md-12 mb-2">
                    <Datepicker1 class="datepicker-here form-control digits" position="center" v-model="date8"
                        data-language="en"></Datepicker1>
                </div>
                <div class="col-md-12">
                    <Datepicker1 class="datepicker-here form-control digits" position="left" v-model="date9"
                        data-language="en"></Datepicker1>
                </div>
            </div>
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

            date6: new Date(),
            date7: new Date(),
            date8: new Date(), date9: new Date(),


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
