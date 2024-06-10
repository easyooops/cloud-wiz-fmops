<template>
    <Breadcrumbs title="Raised Style" main="Buttons" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12 ">
                <raised />
                <raised2 />
                <raised3 />
            </div>
        </div>
    </div>
</template>
<script>
import raised from "@/components/button/raised/raisedPage.vue"
import raised2 from "@/components/button/raised/raised2Page.vue"
import raised3 from "@/components/button/raised/raised3Page.vue"
export default {
    components: {
        raised,
        raised2,
        raised3
    }
}
</script>