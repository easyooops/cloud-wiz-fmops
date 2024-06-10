<template>
    <Breadcrumbs title="Mega Options" main="Forms Control" />
    <div class="container-fluid">
        <div class="row">
            <defaultStyle />
            <noBorder />
            <solidBorder />
            <offerStyle />
            <inlineStyle />
            <verticalStyle />
            <horizontalStyle />
        </div>
    </div>
</template>
<script>
import defaultStyle from "@/components/forms/megaOptions/defaultStyle.vue"
import noBorder from "@/components/forms/megaOptions/noBorder.vue"
import solidBorder from "@/components/forms/megaOptions/solidBorder.vue"
import offerStyle from "@/components/forms/megaOptions/offerStyle.vue"
import inlineStyle from "@/components/forms/megaOptions/inlineStyle.vue"
import verticalStyle from "@/components/forms/megaOptions/verticalStyle.vue"
import horizontalStyle from "@/components/forms/megaOptions/horizontalStyle.vue"
export default {
    components: {
        defaultStyle,
        noBorder,
        solidBorder,
        offerStyle,
        inlineStyle,
        verticalStyle,
        horizontalStyle
    }
}
</script>