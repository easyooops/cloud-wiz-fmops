<template>
  <Breadcrumbs title="Validation Forms" main="Forms Control" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <customStyle />
        <browserDefaults />
        <supportedElements />
        <toolTips />
      </div>
    </div>
  </div>
</template>
<script>
import customStyle from "@/components/forms/formValidetion/customStyle.vue"
import browserDefaults from "@/components/forms/formValidetion/browserDefaults.vue"
import supportedElements from "@/components/forms/formValidetion/supportedElements.vue"
import toolTips from "@/components/forms/formValidetion/toolTips.vue"
export default {
  components: {
    customStyle,
    browserDefaults,
    supportedElements,
    toolTips
  }
};
</script>