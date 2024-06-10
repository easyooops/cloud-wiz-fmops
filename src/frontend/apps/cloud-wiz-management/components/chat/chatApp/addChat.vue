<template>
  <div class="chat-message clearfix">
    <div class="row">
      <div class="col-xl-12 d-flex">
        <div class="smiley-box bg-primary">
          <div class="picker">
            <img src="/images/smiley.png" alt="" />
          </div>
        </div>
        <div class="input-group text-box" ref="abc">
          <input class="form-control input-txt-bx" id="message-to-send" v-model="text" v-on:keyup.enter="addChat()"
            type="text" name="message-to-send" placeholder="Type a message......" />
          <button @click="addChat()" class="btn btn-primary input-group-text" type="button">
            SEND
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'pinia';
import { useChatStore } from '~~/store/chat';

export default {
  name: 'addChat',
  props: {
    chatElement: String
  },
  data() {
    return {
      text: "",
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
    addChat: function () {
      this.$emit("message")
      if (this.text !== '') {

        useChatStore().addChat(this.text)
        this.text = '';

      }
    },
  }
}
</script>