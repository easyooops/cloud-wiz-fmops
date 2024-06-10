<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Tag & Pills" />
    <div class="container-fluid">
      <div class="row">
        <ContextualVariations />
        <TagsWithNumber />
        <PillsWithNumber />
        <TagsWithIcon />
        <PillsWithIcon />
        <BadgesExample />
        <BadgesAsPartButtons />
      </div>
    </div>

  </div>
</template>

<script>
import ContextualVariations from "@/components/uikits/tag_pills/ContextualVariations.vue"
import TagsWithNumber from "@/components/uikits/tag_pills/TagsWithNumber.vue"
import PillsWithNumber from "@/components/uikits/tag_pills/PillsWithNumber.vue"
import TagsWithIcon from "@/components/uikits/tag_pills/TagsWithIcon.vue"
import PillsWithIcon from "@/components/uikits/tag_pills/PillsWithIcon.vue"
import BadgesExample from "@/components/uikits/tag_pills/BadgesExample.vue"
import BadgesAsPartButtons from "@/components/uikits/tag_pills/BadgesAsPartButtons.vue"
export default {
  components: {
    ContextualVariations,
    TagsWithNumber,
    PillsWithNumber,
    TagsWithIcon,
    PillsWithIcon,
    BadgesExample,
    BadgesAsPartButtons
  }
};
</script>