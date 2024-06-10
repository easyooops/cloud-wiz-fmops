<template>
    <div class="col call-chat-body">
        <div class="card">
            <div class="card-body p-0">
                <div class="row chat-box">
                    <div class="col pe-0 chat-right-aside">
                        <div class="chat">
                            <div class="chat-header">
                                <img class="rounded-circle" v-if="currentchat.thumb" :src="getImgUrl(currentchat.thumb)"
                                    alt="" />
                                <div class="about">
                                    <div class="name">
                                        {{ currentchat.name }}
                                    </div>
                                    <div class="status digits">
                                        {{ currentchat.lastSeenDate }}
                                    </div>
                                </div>
                                <ul class="list-inline float-start float-sm-end chat-menu-icons">
                                    <li class="list-inline-item">
                                        <a href="#"><i class="icon-search"></i></a>
                                    </li>
                                    <li class="list-inline-item">
                                        <a href="#"><i class="icon-clip"></i></a>
                                    </li>
                                    <li class="list-inline-item">
                                        <a href="#"><i class="icon-headphone-alt"></i></a>
                                    </li>
                                    <li class="list-inline-item">
                                        <a href="#"><i class="icon-video-camera"></i></a>
                                    </li>
                                    <li class="list-inline-item toogle-bar" data-bs-toggle="collapse"
                                        data-bs-target="#collapseExample" v-on:click="chatmenutoogle = !chatmenutoogle">
                                        <a href="#"><i class="icon-menu"></i></a>
                                    </li>
                                </ul>
                            </div>
                            <div class="chat-history chat-msg-box custom-scrollbar">
                                <div class="row" v-for="(chat, index) in currentChat.chat.video" :key="index"
                                    v-bind:class="{ clearfix: chat.sender == 0 }">
                                    <div class="col text-center pe-0 call-content ">
                                        <div>
                                            <div class="total-time">
                                                <h2 class="digits">{{ chat.time }}</h2>
                                            </div>
                                            <div class="call-icons">
                                                <ul class="list-inline">
                                                    <li class="list-inline-item"><a href="javascript:void(0)"><i
                                                                class="icon-video-camera"></i></a></li>
                                                    <li class="list-inline-item"><a href="javascript:void(0)"><i
                                                                class="icon-volume"></i></a></li>
                                                    <li class="list-inline-item"><a href="javascript:void(0)"><i
                                                                class="icon-user"></i></a></li>
                                                </ul>
                                            </div>
                                            <button class="btn btn-danger btn-block btn-lg">END CALL</button>
                                            <div class="receiver-img"><img src="/images/other-images/receiver-img.jpg"
                                                    alt=""></div>
                                        </div>
                                    </div>
                                    <div class="col-sm-6 caller-img-sec">
                                        <div class="caller-img"><img class="img-fluid bg-img-cover"
                                                src="/images/other-images/caller.jpg" alt=""></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col ps-0 chat-menu custom-scrollbar" :class="{ show: chatmenutoogle }" id="collapseExample">
                        <chatMenu />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {
    mapState
} from 'pinia';
import chatMenu from "./chatMenu.vue"
import {
    useChatStore
} from '~~/store/chat';
export default {
    components: {
        chatMenu
    },
    data() {
        return {
            currentchat: [],
            chatmenutoogle: false,
        }
    },
    computed: {
        ...mapState(useChatStore, {
            currentChat() {
                return (this.currentchat = useChatStore().currentChat);
            },
        }),
    },

    methods: {
        getImgUrl(path) {
            return ('/images/' + path);
        },
    }
}
</script>
