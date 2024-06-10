<template>
    <Breadcrumbs title="Flat Style" main="Buttons" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12 ">
                <flat />
                <flat2 />
                <flat3 />
            </div>
        </div>
    </div>
</template>
<script>
import flat from "@/components/button/flat/flatPage.vue"
import flat2 from "@/components/button/flat/flat2Page.vue"
import flat3 from "@/components/button/flat/flat3Page.vue"
export default {
    components: {
        flat,
        flat2,
        flat3
    }
}
</script>