<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Progress" />

    <div class="container-fluid">
      <div class="row">
        <BasicProgressBars />
        <SizingProgressBars />
        <CustomHeightProgressBars />
        <Multiplebars />
        <ProgressBarsStriped />
        <ProgressBarsanimated />
      </div>
    </div>

  </div>
</template>
  
<script>
import BasicProgressBars from '@/components/uikits/progress_bar/BasicProgressBars.vue';
import SizingProgressBars from "@/components/uikits/progress_bar/SizingProgressBars.vue"
import CustomHeightProgressBars from "@/components/uikits/progress_bar/CustomHeightProgressBars.vue"
import Multiplebars from "@/components/uikits/progress_bar/Multiplebars.vue"
import ProgressBarsStriped from "@/components/uikits/progress_bar/ProgressBarsStriped.vue"
import ProgressBarsanimated from "@/components/uikits/progress_bar/ProgressBarsanimated.vue"

export default {
  components: {
    BasicProgressBars,
    SizingProgressBars,
    CustomHeightProgressBars,
    Multiplebars,
    ProgressBarsStriped,
    ProgressBarsanimated
  }
};
</script>
  