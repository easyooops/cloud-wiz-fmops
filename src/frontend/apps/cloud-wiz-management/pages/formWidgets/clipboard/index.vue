<template>
    <Breadcrumbs main="Form Widgets" title="clipboard" />
    <div class="container-fluid">
        <div class="row">
            <clipboardTextInput />
            <clipboardTextarea />
            <cipboardParagraph />
            <copyPortion />
        </div>
    </div>
</template>
<script>
import clipboardTextInput from "@/components/formWidgets/clipboard/clipboardTextInput.vue"
import clipboardTextarea from "@/components/formWidgets/clipboard/clipboardTextarea.vue"
import cipboardParagraph from "@/components/formWidgets/clipboard/cipboardParagraph.vue"
import copyPortion from "@/components/formWidgets/clipboard/copyPortion.vue"
export default {
    components: {
        clipboardTextInput,
        clipboardTextarea,
        cipboardParagraph,
        copyPortion
    }
}
</script>