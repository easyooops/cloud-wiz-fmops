<template>
  <div>
    <Breadcrumbs main="UI Kits" title="lists" />

    <div class="container-fluid">
      <div class="row">
        <Defaultlist />
        <Linksandbuttons />
        <FlushStyle />
        <Contextualclasses />
        <Withbadges />
        <Customcontent />
        <JavaScriptbehavior />
        <images />

      </div>
    </div>

  </div>
</template>

<script>
import Defaultlist from "@/components/uikits/lists/Defaultlist.vue"
import Linksandbuttons from "@/components/uikits/lists/Linksandbuttons.vue"
import FlushStyle from "@/components/uikits/lists/FlushStyle.vue"
import Contextualclasses from "@/components/uikits/lists/Contextualclasses.vue"
import Withbadges from "@/components/uikits/lists/Withbadges.vue"
import Customcontent from "@/components/uikits/lists/Customcontent.vue"
import JavaScriptbehavior from "@/components/uikits/lists/JavaScriptbehavior.vue"
import images from "@/components/uikits/lists/images.vue"
export default {
  components: {
    Defaultlist,
    Linksandbuttons,
    FlushStyle,
    Contextualclasses,
    Withbadges,
    Customcontent,
    JavaScriptbehavior,
    images
  }

};
</script>