<template>
<div class="col-md-12 project-list">
    <div class="card">
        <div class="row">
            <div class="col-md-6 d-flex">
                <ul class="nav nav-tabs border-tab" id="top-tab" role="tablist" v-for="(item,index) in tab" :key="index">
                    <li class="nav-item"><a class="nav-link" :class="{'active': item.active}" id="top-home-tab" data-bs-toggle="tab" href="javascript:void(0)" role="tab" aria-controls="top-home" :aria-selected="item.active ? 'true':'false'" @click.prevent="active(item)">
                            <vue-feather :type=item.icon></vue-feather>{{item.name}}
                        </a></li>

                </ul>
            </div>
            <div class="col-md-6">
                <div class="form-group mb-0 me-0"></div>
                <nuxt-link class="btn btn-primary" to='/project/createproject'>
                    <vue-feather class="me-1" type="plus-square"> </vue-feather>Create New Project
                </nuxt-link>
            </div>
        </div>
    </div>
</div>
<div class="col-sm-12">
    <div class="card">
        <div class="card-body">
            <div class="tab-content" id="top-tabContent">
                <div class="tab-pane fade" :class="{'active show': item.active}" :id=item.id role="tabpanel" :aria-labelledby=item.label v-for="(item,index) in tab" :key="index">
                    <component :is=item.type></component>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import allPage from '../projectlist/allPage.vue'
import doingPage from '../projectlist/doingPage.vue'
import donePage from '../projectlist/donePage.vue'
export default {
    name: 'topMenu',
    components: {

        allPage,
        doingPage,
        donePage
    },
    data() {
        return {
            tab: [{
                    type: "allPage",
                    name: "All",
                    active: true,
                    icon: "target",
                    id: 'top-home',
                    id1: 'top-tabContent',
                    label: 'top-home-tab'
                },
                {
                    type: 'doingPage',
                    name: "Doing",
                    active: false,
                    icon: "info",
                    id: 'top-profile',
                    label: 'profile-top-tab'
                },
                {
                    type: 'donePage',
                    name: "Done",
                    active: false,
                    icon: "check-circle",
                    id: 'top-contact',
                    label: 'contact-top-tab'
                }
            ]
        }

    },
    methods: {
        active(item) {

            if (!item.active) {
                this.tab.forEach(a => {

                    a.active = false;
                })
            }
            item.active = !item.active
        }
    }
}
</script>
