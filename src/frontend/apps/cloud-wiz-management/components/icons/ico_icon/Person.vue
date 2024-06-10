<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Person</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-6 col-lg-4" v-for="(per, index) in person" :key="index"
                        v-on:click="icon_bar(per.name)">
                        <i class="icofont" :class="'icofont-' + per.name"></i>{{ per.name }}
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>

import iconMixin from "@/mixin/commen/iconMixin"
export default {
    mixins: [iconMixin],
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