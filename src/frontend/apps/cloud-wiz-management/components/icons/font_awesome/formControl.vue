<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Form Control Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(form, index) in formicons" :key="index"
                        v-on:click="icon_bar(form.name)">
                        <i class="" :class="'fa fa-' + form.name"></i>{{ form.name }}
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

            formicons: [{ name: 'check-square' }, { name: 'check-square-o' }, { name: 'circle' }, { name: 'circle-o' }, { name: 'dot-circle-o' }, { name: 'minus-square' }, { name: 'minus-square-o' }, { name: 'plus-square' }, { name: 'plus-square-o' }, { name: 'square' }, { name: 'square-o' }],
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