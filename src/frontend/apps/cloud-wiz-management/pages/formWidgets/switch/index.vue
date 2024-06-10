<template>
    <Breadcrumbs main="Form Widgets" title="Switch" />
    <div class="container-fluid text-start">
        <div class="row">
            <basicSwitch />
            <switchColor />
            <switchOutline />
            <switchUnchecked />
            <switchSizing />
            <switchIcons />
            <switchwithColor />
        </div>
    </div>
</template>
<script>
import basicSwitch from "@/components/formWidgets/switch/basicSwitch.vue"
import switchColor from "@/components/formWidgets/switch/switchColor.vue"
import switchOutline from "@/components/formWidgets/switch/switchOutline.vue"
import switchUnchecked from "@/components/formWidgets/switch/switchUnchecked.vue"
import switchSizing from "@/components/formWidgets/switch/switchSizing.vue"
import switchIcons from "@/components/formWidgets/switch/switchIcons.vue"
import switchwithColor from "@/components/formWidgets/switch/switchwithColor.vue"
export default {
    components: {
        basicSwitch,
        switchColor,
        switchOutline,
        switchUnchecked,
        switchSizing,
        switchIcons,
        switchwithColor
    }
}
</script>