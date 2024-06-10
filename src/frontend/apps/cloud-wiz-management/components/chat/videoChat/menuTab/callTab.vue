<template>
    <div class="people-list">
        <ul class="list digits custom-scrollbar">
            <li class="clearfix" v-for="(user, index) in users" :key="index" @click="setActiveuser(user.id)">
                <img class="rounded-circle user-image" :src="getImgUrl(user.thumb)" alt="" />
                <div class="about">
                    <div class="name">{{ user.name }}</div>
                    <div class="status">
                        <i class="fa fa-share font-success me-1"></i>{{ user.time }}
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>

import {
    useChatStore
} from '~~/store/chat';

export default {

    data() {
        return {
            chatmenutoogle: false,
            activeTab: 'call',
        }
    },
    computed: {
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
