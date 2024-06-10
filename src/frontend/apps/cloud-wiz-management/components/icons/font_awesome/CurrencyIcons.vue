<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Currency Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(cur, index) in currencyicons" :key="index"
                        v-on:click="icon_bar(cur.name)">
                        <i class="" :class="'fa fa-' + cur.name"></i>{{ cur.name }}
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

            currencyicons: [{ name: 'bitcoin' }, { name: 'btc' }, { name: 'cny' }, { name: 'dollar' }, { name: 'eur' }, { name: 'euro' }, { name: 'gbp' }, { name: 'inr' }, { name: 'jpy' }, { name: 'krw' }, { name: 'money' }, { name: 'rmb' }, { name: 'rouble' }, { name: 'rub' }, { name: 'ruble' }, { name: 'rupee' }, { name: 'try' }, { name: 'turkish-lira' }, { name: 'usd' }, { name: 'won' }, { name: 'yen' }],
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