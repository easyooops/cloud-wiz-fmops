<template>
    <div class="col-xxl-3 col-ed-5 col-xl-5 col-sm-6 box-col-5">
        <div class="card">
            <div class="card-body">
                <div class="default-datepicker">
                    <Datepicker1 class="datepicker-here" inline autoApply v-model="date1" range data-language="en"></Datepicker1>
                </div>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    import Datepicker1 from "@vuepic/vue-datepicker";
    import "@vuepic/vue-datepicker/dist/main.css";
    export default {
        components: {
            Datepicker1,
        },
        data() {
            return {
                date1: new Date(),
            };
        },
    };
    </script>
    