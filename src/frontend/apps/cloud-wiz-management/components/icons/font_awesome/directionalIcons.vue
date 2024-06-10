<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Directional Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(dire, index) in directionalicons" :key="index"
                        v-on:click="icon_bar(dire.name)">
                        <i class="" :class="'fa fa-' + dire.name"></i>{{ dire.name }}
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

            directionalicons: [{ name: 'angle-double-down' }, { name: 'angle-double-left' }, { name: 'angle-double-right' }, { name: 'angle-double-up' }, { name: 'angle-down' }, { name: 'angle-left' }, { name: 'angle-right' }, { name: 'angle-up' }, { name: 'arrow-circle-down' }, { name: 'arrow-circle-left' }, { name: 'arrow-circle-o-down' }, { name: 'arrow-circle-o-left' }, { name: 'arrow-circle-o-right' }, { name: 'arrow-circle-o-up' }, { name: 'arrow-circle-right' }, { name: 'arrow-circle-up' }, { name: 'arrow-down' }, { name: 'arrow-left' }, { name: 'arrow-right' }, { name: 'arrow-up' }, { name: 'arrows' }, { name: 'arrows-alt' }, { name: 'arrows-h' }, { name: 'arrows-v' }, { name: 'caret-down' }, { name: 'caret-left' }, { name: 'caret-right' }, { name: 'caret-up' }, { name: 'caret-square-o-left' }, { name: 'caret-square-o-right' }, { name: 'caret-square-o-up' }, { name: 'caret-square-o-down' }, { name: 'chevron-circle-down' }, { name: 'chevron-circle-left' }, { name: 'chevron-circle-right' }, { name: 'chevron-circle-up' }, { name: 'chevron-down' }, { name: 'chevron-left' }, { name: 'chevron-right' }, { name: 'chevron-up' }, { name: 'hand-o-down' }, { name: 'hand-o-left' }, { name: 'hand-o-right' }, { name: 'hand-o-up' }, { name: 'long-arrow-down' }, { name: 'long-arrow-left' }, { name: 'long-arrow-right' }, { name: 'long-arrow-up' }, { name: 'toggle-down' }, { name: 'toggle-left' }, { name: 'toggle-right' }, { name: 'toggle-up' }],
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