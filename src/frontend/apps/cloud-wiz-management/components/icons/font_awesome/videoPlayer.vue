<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Video Player Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(video, index) in videoicons" :key="index"
                        v-on:click="icon_bar(video.name)">
                        <i class="" :class="'fa fa-' + video.name"></i>{{ video.name }}
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

            videoicons: [{ name: 'arrows-alt' }, { name: 'backward' }, { name: 'compress' }, { name: 'eject' }, { name: 'expand' }, { name: 'fast-backward' }, { name: 'fast-forward' }, { name: 'forward' }, { name: 'pause' }, { name: 'play' }, { name: 'play-circle' }, { name: 'play-circle-o' }, { name: 'step-backward' }, { name: 'step-forward' }, { name: 'stop' }, { name: 'youtube-play' }],
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