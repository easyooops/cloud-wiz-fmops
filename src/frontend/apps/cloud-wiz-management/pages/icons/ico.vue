<template>
    <div>
        <Breadcrumbs main="Icons" title="Ico Icon" />
        <div class="container-fluid">
            <div class="row">
                <abstractIcon @selected="icon_bar" />
                <animalIcon @selected="icon_bar" />
                <brandIcons @selected="icon_bar" />
                <Business @selected="icon_bar" />
                <Chart @selected="icon_bar" />
                <Construction @selected="icon_bar" />
                <Currency @selected="icon_bar" />
                <Device @selected="icon_bar" />
                <Directional @selected="icon_bar" />
                <Education @selected="icon_bar" />
                <Emoticon @selected="icon_bar" />
                <Filetype @selected="icon_bar" />
                <Food @selected="icon_bar" />
                <Kids @selected="icon_bar" />
                <Law @selected="icon_bar" />
                <Mathematical @selected="icon_bar" />
                <Medical @selected="icon_bar" />
                <Mobile @selected="icon_bar" />
                <Multimedia @selected="icon_bar" />
                <Payment @selected="icon_bar" />
                <Person @selected="icon_bar" />
                <Search @selected="icon_bar" />
                <Social @selected="icon_bar" />
                <Sport @selected="icon_bar" />
                <Text @selected="icon_bar" />
                <Transport @selected="icon_bar" />
                <Travel @selected="icon_bar" />
                <Weather @selected="icon_bar" />
                <Web @selected="icon_bar" />

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
import abstractIcon from "@/components/icons/ico_icon/abstractIcon.vue"
import animalIcon from "@/components/icons/ico_icon/animalIcon.vue"
import brandIcons from "@/components/icons/ico_icon/brandIcons.vue"
import Business from "@/components/icons/ico_icon/Business.vue"
import Chart from "@/components/icons/ico_icon/Chart.vue"
import Construction from "@/components/icons/ico_icon/Construction.vue"
import Currency from "@/components/icons/ico_icon/Currency.vue"
import Device from "@/components/icons/ico_icon/Device.vue"
import Directional from "@/components/icons/ico_icon/Directional.vue"
import Education from "@/components/icons/ico_icon/Education.vue"
import Filetype from "@/components/icons/ico_icon/Filetype.vue"
import Emoticon from "@/components/icons/ico_icon/Emoticon.vue"
import Food from "@/components/icons/ico_icon/Food.vue"
import Kids from "@/components/icons/ico_icon/Kids.vue"
import Law from "@/components/icons/ico_icon/Law.vue"
import Mathematical from "@/components/icons/ico_icon/Mathematical.vue"
import Medical from "@/components/icons/ico_icon/Medical.vue"
import Mobile from "@/components/icons/ico_icon/Mobile.vue"
import Multimedia from "@/components/icons/ico_icon/Multimedia.vue"
import Payment from "@/components/icons/ico_icon/Payment.vue"
import Person from "@/components/icons/ico_icon/Person.vue"
import Search from "@/components/icons/ico_icon/Search.vue"
import Social from "@/components/icons/ico_icon/Social.vue"
import Sport from "@/components/icons/ico_icon/Sport.vue"
import Text from "@/components/icons/ico_icon/Text.vue"
import Transport from "@/components/icons/ico_icon/Transport.vue"
import Travel from "@/components/icons/ico_icon/Travel.vue"
import Weather from "@/components/icons/ico_icon/Weather.vue"
import Web from "@/components/icons/ico_icon/Web.vue"
export default {
    components: {
        abstractIcon, animalIcon, brandIcons, Business, Chart, Construction, Currency, Device, Directional, Education,
        Filetype, Emoticon, Food, Kids, Law, Mathematical, Medical, Mobile, Multimedia, Payment, Person,
        Search, Social, Sport, Text, Transport, Travel, Weather, Web
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
            this.select_icon.class = 'icofont icofont-' + icon;
            this.select_icon.tag = '<i class="icofont icofont-' + icon + '"></i>';
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