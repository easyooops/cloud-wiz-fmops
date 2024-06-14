<template>
    <div class="row chat-box">
        <div class="col pe-0 chat-right-aside">
            <div class="chat">
                <div class="chat-history chat-msg-box custom-scrollbar" ref="chatInput">
                    <ul>
                        <li v-for="(chat, index) in currentChat.chat.messages" :key="index" v-bind:class="{ clearfix: chat.sender == 0 }">
                            <div class="message" v-bind:class="{ 'other-message pull-right': chat.sender == 0,
                        'my-message': chat.sender != 0}">
                                <img class="rounded-circle float-start chat-user-img img-30 text-end" alt="" v-if="currentchat.thumb && chat.sender != 0" v-bind:src="getImgUrl(currentchat.thumb)" />
                                <img class="rounded-circle float-end chat-user-img img-30" alt="" v-if="chat.sender == 0" v-bind:src="getImgUrl('user/1.jpg')" />
                                <div class="message-data text-end" v-bind:class="{ 'text-start': chat.sender == 0 }">
                                    <span class="message-data-time">{{ chat.time }}</span>
                                </div>
                                {{ chat.text }}
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="chat-message clearfix">
                    <div class="row">
                        <div class="col-xl-12 d-flex">
                            <div class="input-group text-box" ref="abc">
                                <input class="form-control input-txt-bx" id="message-to-send" v-model="text" v-on:keyup.enter="addChat()"
                                    type="text" name="message-to-send" placeholder="Type a message......" />
                            </div>
                            <button @click="addChat()" class="btn btn-primary" type="button">
                                <i class="fa fa-send-o"></i>
                            </button>
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
    name: 'prompt',
    components: {
    },
    data() {
        return {
            text: "",            
            currentchat: [],
            chatmenutoogle: false
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
        addChat() {
            var container = this.$el.querySelector(".chat-history")
            setTimeout(function () {
                container.scrollBy({
                    top: 200,
                    behavior: 'smooth'
                });
            }, 310);
            setTimeout(function () {
                container.scrollBy({
                    top: 200,
                    behavior: 'smooth'
                });
            }, 1100);
        }
    },

}
</script>

<style scoped>
.chat-box .chat-right-aside .chat .chat-msg-box { 
    height: 700px; 
    border-top: 1px solid #f4f4f4;
    padding: 30px;
};
</style>