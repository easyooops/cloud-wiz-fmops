<template>
  <Breadcrumbs main="Cards" title="Tabbed Card" />
  <div class="container-fluid">
    <div class="row">
      <simpleTab />
      <tabIcon />
      <colorTab />
      <colorOption />
      <materialTab />
      <materialIcon />
      <materialIcon2 />
      <materialIcon3 />
    </div>
  </div>
</template>
<script>
import simpleTab from "@/components/advance/TabbedCard/simpleTab.vue"
import tabIcon from "@/components/advance/TabbedCard/tabIcon.vue"
import colorTab from "@/components/advance/TabbedCard/colorTab.vue"
import colorOption from "@/components/advance/TabbedCard/colorOption.vue"
import materialTab from "@/components/advance/TabbedCard/materialTab.vue"
import materialIcon from "@/components/advance/TabbedCard/materialIcon.vue"
import materialIcon2 from "@/components/advance/TabbedCard/materialIcon2.vue"
import materialIcon3 from "@/components/advance/TabbedCard/materialIcon3.vue"
export default {
  components: {
    simpleTab,
    tabIcon,
    colorTab,
    colorOption,
    materialTab,
    materialIcon,
    materialIcon2,
    materialIcon3
  }
}
</script>