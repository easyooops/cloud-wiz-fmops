<template>
    <breadCrumbs title="Basic Data Table" main="Data Table" title1="Basic Data Table" />
    <div class="container-fluid text-start">
        <div class="row">
            <zeroConfiguration />
        </div>
    </div>
</template>
<script>
import zeroConfiguration from "@/components/tables/dataTable/zeroConfiguration.vue"

export default {
    components: {
        zeroConfiguration,
    },
    data() {
        return {
        }
    },

}
</script>