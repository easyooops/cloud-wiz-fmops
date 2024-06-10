<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Spinner Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(spi, index) in spinner" :key="index"
                        v-on:click="icon_bar(spi.name)">
                        <i class="" :class="'fa fa-' + spi.name"></i>{{ spi.name }}
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

            spinner: [{ name: 'circle-o-notch' }, { name: 'cog' }, { name: 'gear' }, { name: 'refresh' }, { name: 'spinner' }],
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