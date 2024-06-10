<template>
    <Breadcrumbs main="Form Widgets" title="touchspin" />
    <div class="container-fluid">
        <div class="bootstrap-touchspin">
            <div class="row">
                <defaultTouchspin />
                <verticalTouchspin />
                <touchspinPostfix />
                <touchspinWithPrefix />
                <minMax />
                <initialValue />
                <touchspinSteps />
                <decimalValue />
                <changeButton />
                <touchspinWithIcon />
                <touchspinIconButton />
                <touchspinDropdown />
                <mousewheelDisable />
                <largeHorizontal />
            </div>
        </div>
    </div>
</template>
<script>
import defaultTouchspin from "@/components/formWidgets/touchspin/defaultTouchspin.vue"
import verticalTouchspin from "@/components/formWidgets/touchspin/verticalTouchspin.vue"
import touchspinPostfix from "@/components/formWidgets/touchspin/touchspinPostfix.vue"
import touchspinWithPrefix from "@/components/formWidgets/touchspin/touchspinWithPrefix.vue"
import minMax from "@/components/formWidgets/touchspin/minMax.vue"
import initialValue from "@/components/formWidgets/touchspin/initialValue.vue"
import touchspinSteps from "@/components/formWidgets/touchspin/touchspinSteps.vue"
import decimalValue from "@/components/formWidgets/touchspin/decimalValue.vue"
import changeButton from "@/components/formWidgets/touchspin/changeButton.vue"
import touchspinWithIcon from "@/components/formWidgets/touchspin/touchspinWithIcon.vue"
import touchspinIconButton from "@/components/formWidgets/touchspin/touchspinIconButton.vue"
import touchspinDropdown from "@/components/formWidgets/touchspin/touchspinDropdown.vue"
import mousewheelDisable from "@/components/formWidgets/touchspin/mousewheelDisable.vue"
import largeHorizontal from "@/components/formWidgets/touchspin/largeHorizontal.vue"
export default {
    components: {
        defaultTouchspin,
        verticalTouchspin,
        touchspinPostfix,
        touchspinWithPrefix,
        minMax,
        initialValue,
        touchspinSteps,
        decimalValue,
        changeButton,
        touchspinWithIcon,
        touchspinIconButton,
        touchspinDropdown,
        mousewheelDisable,
        largeHorizontal
    }
}
</script>