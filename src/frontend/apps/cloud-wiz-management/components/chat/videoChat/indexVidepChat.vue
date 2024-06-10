<template>
  <Breadcrumbs title="Video Chat" main="Chat"  />
    <div class="container-fluid">
      <div class="row">
         <searchChat/>
         <videochatBody/>
      </div>
    </div>
</template>
<script>
import videochatBody from "./videochatBody.vue"
import searchChat from ".././searchChat.vue"
export default {
    components:{
      searchChat,
      videochatBody,
    }
}
</script>