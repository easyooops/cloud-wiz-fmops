<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0"><span class="digits">20</span> Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(ico, index) in icons" :key="index"
                        v-on:click="icon_bar(ico.name)">
                        <i class="" :class="'fa fa-' + ico.name"></i>{{ ico.name }}
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

            icons: [{ name: 'bluetooth' }, { name: 'bluetooth-b' }, { name: 'codiepie' }, { name: 'credit-card-alt' }, { name: 'edge' }, { name: 'fort-awesome' }, { name: 'hashtag' }, { name: 'mixcloud' }, { name: 'modx' }, { name: 'pause-circle' }, { name: 'pause-circle-o' }, { name: 'percent' }, { name: 'product-hunt' }, { name: 'reddit-alien' }, { name: 'scribd' }, { name: 'shopping-bag' }, { name: 'shopping-basket' }, { name: 'stop-circle' }, { name: 'stop-circle-o' }, { name: 'usb' }],
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