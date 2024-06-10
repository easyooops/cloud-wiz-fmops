<template>
    <div class="col-xl-3 box-col-6">
        <div class="md-sidebar"><a class="btn btn-primary md-sidebar-toggle" href="javascript:void(0)"
                @click="collapseFilter()">bookmark filter</a>
            <div class="md-sidebar-aside job-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                <div class="email-left-aside">
                    <div class="card">
                        <div class="card-body">
                            <div class="email-app-sidebar left-bookmark">
                                <div class="media">
                                    <div class="media-size-email"><img class="me-3 rounded-circle"
                                            src="/images/user/user.png" alt=""></div>
                                    <div class="media-body">
                                        <h6 class="f-w-600">MARK JENCO</h6>
                                        <p>Markjecno@gmail.com</p>
                                    </div>
                                </div>
                                <ul class="nav main-menu" role="tablist">
                                    <newBookmark />
                                    <li class="nav-item"><span class="main-title"> Views</span></li>
                                    <li><a id="pills-created-tab" data-toggle="pill" href="javascript:void(0)" role="tab"
                                            aria-controls="pills-created" aria-selected="true"><span class="title"
                                                v-on:click="say('pills_created')"> Created by me</span></a></li>
                                    <li><a class="show" id="pills-favourites-tab" data-toggle="pill"
                                            href="javascript:void(0)" role="tab" aria-controls="pills-favourites"
                                            aria-selected="false"><span class="title" v-on:click="say('pills_favourites')">
                                                Favourites ({{ favourite.length }})</span></a></li>
                                    <li><a class="show" id="pills-shared-tab" data-toggle="pill" href="javascript:void(0)"
                                            role="tab" aria-controls="pills-shared" aria-selected="false"><span
                                                class="title" v-on:click="say('pills_shared')"> Shared with me</span></a>
                                    </li>
                                    <li><a class="show" id="pills-bookmark-tab" data-toggle="pill" href="javascript:void(0)"
                                            role="tab" aria-controls="pills-bookmark" aria-selected="false"><span
                                                class="title" v-on:click="say('pills_bookmark')"> My bookmark</span></a>
                                    </li>
                                    <li>
                                        <hr />
                                    </li>
                                    <li><span class="main-title"> Tags<span class="pull-right">
                                                <tagsmodal />
                                            </span></span></li>
                                    <li><a class="show" id="pills-notification-tab" data-toggle="pill"
                                            href="javascript:void(0)" role="tab" aria-controls="pills-notification"
                                            aria-selected="false"><span class="title" @click="say('pills_notification')">
                                                notification</span></a></li>
                                    <li><a class="show" id="pills-newsletter-tab" data-toggle="pill"
                                            href="javascript:void(0)" role="tab" aria-controls="pills-newsletter"
                                            aria-selected="false"><span class="title" @click="say('pills_newsletter')">
                                                Newsletter</span></a></li>
                                    <li><a class="show" id="pills-buisness-tab" data-toggle="pill" href="javascript:void(0)"
                                            role="tab" aria-controls="pills-newsletter" aria-selected="false"><span
                                                class="title" @click="say('pills_business')"> Business</span></a></li>
                                    <li><a class="show" id="pills-holiday-tab" data-toggle="pill" href="javascript:void(0)"
                                            role="tab" aria-controls="pills-newsletter" aria-selected="false"><span
                                                class="title" @click="say('pills_holiday')"> Holiday</span></a></li>
                                    <li><a class="show" id="pills-important-tab" data-toggle="pill"
                                            href="javascript:void(0)" role="tab" aria-controls="pills-newsletter"
                                            aria-selected="false"><span class="title" @click="say('pills_important')">
                                                Important</span></a></li>
                                    <li><a class="show" id="pills-organization-tab" data-toggle="pill"
                                            href="javascript:void(0)" role="tab" aria-controls="pills-newsletter"
                                            aria-selected="false"><span class="title" @click="say('pills_organization')">
                                                Organization</span></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xl-9 col-md-12 box-col-12">
        <div class="email-right-aside bookmark-tabcontent contacts-tabs">
            <div class="card email-body radius-left">
                <div class="ps-0">
                    <div class="tab-content">
                        <createdbyMe />
                        <favouritePage />
                        <shared />
                        <myBookmark />
                        <notification />
                        <newsletter />
                        <bHoliday />
                        <iOrganization />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import notification from "./notiFication.vue"
import newsletter from './newsPage.vue'
import shared from "./shareD.vue"
import newBookmark from "./newBookmark.vue"
import tagsmodal from "./tagsModal.vue"
import createdbyMe from "./createdbyMe.vue"
import favouritePage from './favouritePage.vue'
import myBookmark from './myBookmark.vue'
import bHoliday from './bHoliday.vue'
import iOrganization from './iOrganization.vue'
import { useCommonStore } from '~~/store/common'
export default {
    components: {
        notification, newsletter, shared, newBookmark, tagsmodal, createdbyMe, favouritePage, myBookmark, bHoliday, iOrganization
    },
    data() {
        return {
            liststyle: false, favourite: useCommonStore().favourite, filtered: false,
        };
    },
    methods: {
        say: function (message) {
            useCommonStore().active(message)
        },
        collapseFilter() {
            this.filtered = !this.filtered
        }
    }
}
</script>