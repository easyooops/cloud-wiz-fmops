<template>
    <Breadcrumbs title="Basic Cards" main="Bonus UI" />

    <div class="container-fluid">
        <div class="row">
            <basic6Page />
            <basicRest />
        </div>
    </div>
</template>
<script>
import basic6Page from '@/components/advance/basicCard/basic6Page.vue';
import basicRest from '@/components/advance/basicCard/basicRest.vue'
export default {
    components: {
        basic6Page,
        basicRest
    }
}
</script>