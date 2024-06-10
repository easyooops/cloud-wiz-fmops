<template>
    <div>
        <Breadcrumbs main="Icons" title="Font Awesome Icon" />

        <div class="container-fluid">
            <div class="row">
                <iconsView @selected="icon_bar" />
                <CurrencyIcons @selected="icon_bar" />
                <WebAppIcons @selected="icon_bar" />
                <SpinnerIcons @selected="icon_bar" />
                <formControl @selected="icon_bar" />
                <textEditor @selected="icon_bar" />
                <directionalIcons @selected="icon_bar" />
                <videoPlayer @selected="icon_bar" />
                <brandIcons @selected="icon_bar" />
                <medicalIcons @selected="icon_bar" />
            </div>
        </div>
        <div class="icon-hover-bottom p-fixed fa-fa-icon-show-div" :class="{ 'opecity-0': !icon_bar_status }"
            :style="[icon_bar_status ? { 'display': 'block' } : { 'display': 'none' }]">
            <div class="container-fluid">
                <div class="row">
                    <div class="icon-popup">
                        <div class="close-icon" v-on:click="close_icon_bar"><i class="icofont icofont-close"></i></div>
                        <div class="icon-first"><i class="fa-2x" :class="[select_icon.class]"></i></div>
                        <div class="icon-class">
                            <label class="icon-title">Class</label><span v-text="select_icon.class"></span>
                        </div>
                        <div class="icon-last icon-last">
                            <label class="icon-title">Markup</label>
                            <div class="form-inline">
                                <div class="form-group">
                                    <input class="inp-val form-control m-r-10" type="text" ref="text"
                                        :value="select_icon.tag" readonly="readonly">
                                    <button class="btn btn-primary notification" v-on:click="copy_icon">Copy text</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { toast } from 'vue3-toastify';
import iconsView from "@/components/icons/font_awesome/iconsView.vue"
import CurrencyIcons from "@/components/icons/font_awesome/CurrencyIcons.vue"
import WebAppIcons from "@/components/icons/font_awesome/WebAppIcons.vue"
import SpinnerIcons from "@/components/icons/font_awesome/SpinnerIcons.vue"
import formControl from "@/components/icons/font_awesome/formControl.vue"
import textEditor from "@/components/icons/font_awesome/textEditor.vue"
import directionalIcons from "@/components/icons/font_awesome/directionalIcons.vue"
import videoPlayer from "@/components/icons/font_awesome/videoPlayer.vue"
import brandIcons from "@/components/icons/font_awesome/brandIcons.vue"
import medicalIcons from "@/components/icons/font_awesome/medicalIcons.vue"
export default {
    components: {
        iconsView, CurrencyIcons, WebAppIcons, SpinnerIcons, formControl, textEditor, directionalIcons, videoPlayer, brandIcons, medicalIcons
    },
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
            this.select_icon.class = 'fa fa-' + icon;
            this.select_icon.tag = '<i class="fa fa-' + icon + '"></i>';
            this.icon_bar_status = true;
        },
        close_icon_bar() {
            this.icon_bar_status = false;
        },
        copy_icon() {
            this.$refs.text.select();
            document.execCommand('copy');
            toast.success("Code Copied to clipboard!", {
                theme: 'colored',
                icon: false,
                hideProgressBar: true,
                transition: this.customAnimation,
                autoClose: 1000,
                position: toast.POSITION.BOTTOM_RIGHT,
            });
        }
    }
};
</script>
<style lang="scss" scoped>
@import "@/assets/scss/vendors/animate.scss"
</style>