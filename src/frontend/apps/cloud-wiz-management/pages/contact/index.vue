<template>
  <Breadcrumbs title="Contacts" main="Apps" />
  <div class="container-fluid">
    <contectSidebar />
  </div>
</template>
<script>
import contectSidebar from "@/components/contact/contectSidebar.vue"
export default {
  name: 'contactView',

  components: {
    contectSidebar
  },

}
</script>