<template>
  <Breadcrumbs main="Chat" title="Chat App" />


  <div class="container-fluid text-start">
    <div class="row">
      <searchChat />
      <chatBody />
    </div>
  </div>
</template>
<script>
import chatBody from "./chatBody.vue"
import searchChat from ".././searchChat.vue"

export default {
  components: {
    searchChat,

    chatBody
  }
}
</script>