<template>
    <div class="col-sm-12">
        <ul class="nav nav-tabs border-tab nav-primary" id="top-tab" role="tablist">
            <li class="nav-item" @click="tabContent('call')">
                <a class="nav-link" id="top-home-tab" data-toggle="tab" role="tab" aria-controls="top-home"
                    aria-selected="false" :class="[{ active: activeTab == 'call' }]">CALL</a>
                <div class="material-border"></div>
            </li>
            <li class="nav-item" @click="tabContent('status')">
                <a class="nav-link" id="profile-top-tab" data-toggle="tab" role="tab" aria-controls="top-profile"
                    aria-selected="false" :class="[{ active: activeTab == 'status' }]">STATUS</a>
                <div class="material-border"></div>
            </li>
            <li class="nav-item" @click="tabContent('profile')">
                <a class="nav-link" id="contact-top-tab" data-toggle="tab" role="tab" aria-controls="top-contact"
                    aria-selected="true" :class="[{ active: activeTab == 'profile' }]">PROFILE</a>
                <div class="material-border"></div>
            </li>
        </ul>
        <div class="tab-content custom-scrollbar" id="top-tabContent">
            <div class="tab-pane fade" :class="{ 'show active': activeTab == 'call' }" id="top-home" role="tabpanel"
                aria-labelledby="top-home-tab">
                <callTab />
            </div>
            <div class="tab-pane fade" :class="{ 'show active': activeTab == 'status' }" id="top-profile" role="tabpanel"
                aria-labelledby="profile-top-tab">
                <statusTab />
            </div>
            <div class="tab-pane fade" id="top-contact" role="tabpanel" :class="{ 'show active': activeTab == 'profile' }"
                aria-labelledby="contact-top-tab">
                <profileTab />
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    mapState
} from 'pinia';
import {
    useChatStore
} from '~~/store/chat';
import callTab from './menuTab/callTab.vue';
import statusTab from './menuTab/statusTab.vue';
import profileTab from './menuTab/profileTab.vue';
export default {
    components: {
        callTab,
        statusTab,
        profileTab
    },
    data() {
        return {
            currentchat: [],
            chatmenutoogle: false,
            activeTab: 'call',
        }
    },
    computed: {
        ...mapState(useChatStore, {
            activeuser: 'activeuser',
            serchUser: 'serchUser',
            currentChat() {
                return (this.currentchat = useChatStore().currentChat);
            },
        }),
        users() {
            return useChatStore().users.filter(function (user) {
                if (user.id !== 0) return user;
            })
        },
        activeusers() {
            return useChatStore().users.filter(function (user) {
                if (user.active === 'active' && user.id !== 0) return user;
            })
        }
    },

    methods: {
        getImgUrl(path) {
            return ('/images/' + path);
        },
        tabContent(val) {
            this.activeTab = val;
        },
        setActiveuser: function (id) {

            useChatStore().setActiveuser(id)
        },
    }
}
</script>
    