<template>
  <Breadcrumbs main="Form Widgets" title="Typeahead" />
  <div class="container-fluid">
    <div class="typeahead">
      <div class="row">
        <basicDemo />
        <preFetch />
        <blooDhound />
        <remoteView />
        <customTemplates />
        <defaultSuggestions />
        <rtlSupport />

      </div>
    </div>
  </div>
</template>
<script>
import basicDemo from "@/components/formWidgets/typeahead/basicDemo.vue"
import preFetch from "@/components/formWidgets/typeahead/preFetch.vue"
import blooDhound from "@/components/formWidgets/typeahead/blooDhound.vue"
import remoteView from "@/components/formWidgets/typeahead/remoteView.vue"
import customTemplates from "@/components/formWidgets/typeahead/customTemplates.vue"
import defaultSuggestions from "@/components/formWidgets/typeahead/defaultSuggestions.vue"
import rtlSupport from "@/components/formWidgets/typeahead/rtlSupport.vue"
export default {
  components: {
    basicDemo,
    preFetch,
    blooDhound,
    remoteView,
    customTemplates,
    defaultSuggestions,
    rtlSupport,
  }
}
</script>