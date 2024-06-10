<template>
    <Breadcrumbs title="Breadcrumb" main="Bonus UI" />

    <div class="container-fluid">
        <div class="row">
            <defaultBreadcrumb />
            <navBreadcrumb />
            <coloredBreadcrumb />
        </div>
    </div>
</template>
<script>
import defaultBreadcrumb from "@/components/advance/breadcrumb/defaultBreadcrumb.vue"
import navBreadcrumb from "@/components/advance/breadcrumb/navBreadcrumb.vue"
import coloredBreadcrumb from "@/components/advance/breadcrumb/coloredBreadcrumb.vue"
export default {
    components: {
        defaultBreadcrumb,
        navBreadcrumb,
        coloredBreadcrumb
    }
}
</script>