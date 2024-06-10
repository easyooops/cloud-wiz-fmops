<template>
   <Breadcrumbs main="Form Widgets" title="Select2" />

   <div class="container-fluid text-start">
      <div class="select2-drpdwn">
         <div class="row">
            <selectView />
            <Outline />
            <fullcolored />
         </div>
      </div>
   </div>
</template>
<script>
import Outline from "@/components/formWidgets/select2/OutlinePage.vue"
import fullcolored from "@/components/formWidgets/select2/fullcoloredPage.vue"
import selectView from "@/components/formWidgets/select2/selectPAge.vue"
export default {
   components: {
      Outline,
      fullcolored,
      selectView
   }
}
</script>