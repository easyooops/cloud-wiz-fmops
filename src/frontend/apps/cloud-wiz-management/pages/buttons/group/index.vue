<template>
    <Breadcrumbs title="Button Group" main="Buttons" />
    <div class="container-fluid">
        <div class="row">
            <group />
            <edges />
            <flat />
            <large />
            <largeEdges />
            <outline />
            <outline2 />
            <outline3 />
            <outlineEdges />
            <outlineFlat />
            <radio />
            <checkBox />
            <nesting />
        </div>
    </div>
</template>
<script>
import group from "@/components/button/group/groupPage.vue"
import edges from "@/components/button/group/edgesPage.vue"
import flat from "@/components/button/group/flatPage.vue"
import large from "@/components/button/group/largePage.vue"
import largeEdges from "@/components/button/group/largeEdges.vue"
import outline from "@/components/button/group/outlinePage.vue"
import outline2 from "@/components/button/group/outline2Page.vue"
import outline3 from "@/components/button/group/outline3Page.vue"
import outlineEdges from "@/components/button/group/outlineEdges.vue"
import outlineFlat from "@/components/button/group/outlineFlat.vue"
import radio from "@/components/button/group/radioPage.vue"
import checkBox from "@/components/button/group/checkBox.vue"
import nesting from "@/components/button/group/nestingPage.vue"
export default {
    components: {
        group,
        edges,
        flat,
        large,
        largeEdges,
        outline,
        outline2,
        outline3,
        outlineEdges,
        outlineFlat,
        radio,
        checkBox,
        nesting
    }
}
</script>