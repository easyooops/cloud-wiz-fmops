<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Abstract</h5><span>New</span>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(ab, index) in abstract" :key="index"
                        v-on:click="icon_bar(ab.name)">
                        <i class="icofont" :class="'icofont-' + ab.name"></i>{{ ab.name }}
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