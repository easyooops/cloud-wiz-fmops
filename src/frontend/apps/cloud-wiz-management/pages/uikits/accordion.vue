<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Accordion" />

    <div class="container-fluid">
      <div class="row">
        <BasicAccordion />
        <AllCloseAccordion />
        <ColorAccordion />
        <AccordionWithcononTitle />
        <Accordionopencloseicon />
      </div>
    </div>

  </div>
</template>

<script>
import BasicAccordion from '@/components/uikits/accordion/BasicAccordion.vue';
import AllCloseAccordion from '@/components/uikits/accordion/AllCloseAccordion.vue';
import ColorAccordion from '@/components/uikits/accordion/ColorAccordion.vue';
import AccordionWithcononTitle from '@/components/uikits/accordion/AccordionWithcononTitle.vue';
import Accordionopencloseicon from '@/components/uikits/accordion/Accordionopencloseicon.vue';
export default {
  components: {
    BasicAccordion,
    AllCloseAccordion,
    ColorAccordion,
    AccordionWithcononTitle,
    Accordionopencloseicon
  }
};
</script>