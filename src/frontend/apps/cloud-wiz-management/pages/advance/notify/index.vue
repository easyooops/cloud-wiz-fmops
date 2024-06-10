<template>
   <Breadcrumbs title="Notify" main="Bonus UI" />

   <div class="container-fluid">
      <div class="row">
         <toastr />
         <toastrIcon />
         <toastrPosition />
      </div>
   </div>
</template>
<script>
import toastr from "@/components/advance/notify/toastrPage.vue"
import toastrIcon from "@/components/advance/notify/toastrIcon.vue"
import toastrPosition from "@/components/advance/notify/toastrPosition.vue"
export default {
   components: {
      toastr,
      toastrIcon,
      toastrPosition
   }
}
</script>