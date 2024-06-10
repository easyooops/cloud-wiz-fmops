<template>
  <div>
    <Breadcrumbs main="UI Kits" title="typography" />

    <div class="container-fluid">
      <div class="row">
        <Headings />
        <Thin />
        <Normal />
        <Bold />
        <Fancydisplay />
        <ListingCom />
        <Blockquotes />
      </div>
    </div>

  </div>
</template>
  
<script>
import Headings from "@/components/uikits/typographyComponent/Headings.vue"
import Thin from "@/components/uikits/typographyComponent/Thin.vue"
import Normal from "@/components/uikits/typographyComponent/Normal.vue"
import Bold from "@/components/uikits/typographyComponent/Blod.vue"
import Fancydisplay from "@/components/uikits/typographyComponent/Fancydisplay.vue"
import ListingCom from "@/components/uikits/typographyComponent/Listing.vue"
import Blockquotes from "@/components/uikits/typographyComponent/Blockquotes.vue"
export default {
  components: {
    Headings,
    Thin,
    Normal,
    Bold,
    Fancydisplay,
    ListingCom,
    Blockquotes

  }
};
</script>
  