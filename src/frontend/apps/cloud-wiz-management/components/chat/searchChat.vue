<template>
    <div class="col call-chat-sidebar col-sm-12">
        <div class="card">
            <div class="card-body chat-body">
                <div class="chat-box">
                    <div class="chat-left-aside">
                        <div class="d-flex"><img class="rounded-circle user-image" src="/images/user/12.png" alt="">
                            <div class="flex-grow-1">
                                <div class="about"><a class="name f-w-600">
                                        <NuxtLink to="/users/profile">Mark Jecno</NuxtLink>
                                    </a>
                                    <div class="status">Status...</div>
                                </div>
                            </div>
                        </div>
                        <div class="people-list" id="people-list">
                            <div class="search">
                                <form class="theme-form">
                                    <div class="form-group mt-3 mb-4">
                                        <div class="input-group">
                                            <input v-model="search" v-on:keyup="setSerchUsers" class="form-control"
                                                type="text" placeholder="search" /><i class="fa fa-search"></i>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <ul class="list" v-if="search == ''">
                                <li class="clearfix" v-for="(user, index) in activeusers" :key="index"
                                    @click="setActiveuser(user.id)">
                                    <img class="rounded-circle user-image" :src="getImgUrl(user.thumb)" alt="" />
                                    <div class="status-circle away"></div>
                                    <div class="about">
                                        <div class="name">{{ user.name }}</div>
                                        <div class="status">{{ user.status }}</div>
                                    </div>
                                </li>
                            </ul>
                            <ul class="list" v-if="search != ''">
                                <li class="clearfix" v-for="(user, index) in serchUser" :key="index"
                                    @click="setActiveuserSerch(user.id)">
                                    <img class="rounded-circle user-image" :src="getImgUrl(user.thumb)" alt="" />
                                    <div class="status-circle away"></div>
                                    <div class="about">
                                        <div class="name">{{ user.name }}</div>
                                        <div class="status">{{ user.status }}</div>
                                    </div>
                                </li>
                                <div v-if="!serchUser.length">
                                    <div class="search-not-found chat-search text-center">
                                        <p> Sorry, We didn't find any results matching this search </p>
                                    </div>
                                </div>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from 'pinia';
import { useChatStore } from '~~/store/chat';
export default {
    name: 'searchChat',
    components: {},
    data() {
        return {
            text: '', search: '',
        };
    },
    computed: {
        ...mapState(useChatStore, {
            activeuser: 'activeuser', serchUser: 'serchUser',
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
        },
        chats() {
            return useChatStore().chats.find(function (chat) {
                if (chat.id === state.chat.activeuser) {
                    return chat;
                }
            })
        }
    },
    methods: {
        getImgUrl(path) {
            return ('/images/' + path);
        },
        setActiveuser: function (id) {
            useChatStore().setActiveuser(id)
        },
        setActiveuserSerch: function (id) {
            useChatStore().setActiveuser(id)
            this.search = '';
        },
        setSerchUsers: function () {
            if (this.search !== '')
                useChatStore().setSerchUsers(this.search)
        },
    },
};
</script>