<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Medical Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(medica, index) in medicalicons" :key="index"
                        v-on:click="icon_bar(medica.name)">
                        <i class="" :class="'fa fa-' + medica.name"></i>{{ medica.name }}
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    data() {
        return {
            customAnimation: {
                enter: "animated bounce",
                exit: "animated bounce",
            },
            icon_bar_status: false,

            select_icon: {
                class: '',
                tag: ''
            },

            medicalicons: [{ name: 'ambulance' }, { name: 'h-square' }, { name: 'hospital-o' }, { name: 'medkit' }, { name: 'plus-square' }, { name: 'stethoscope' }, { name: 'user-md' }, { name: 'wheelchair' }]
        };
    },
    methods: {
        icon_bar(icon) {

            this.$emit('selected', icon);
        },
    }
};
</script>
<style lang="scss" scoped>
@import "@/assets/scss/vendors/animate.scss"
</style>