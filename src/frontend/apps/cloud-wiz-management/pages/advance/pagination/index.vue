<template>
    <Breadcrumbs title="Pagination" main="Bonus UI" />

    <div class="container-fluid">
        <div class="row">
            <pagination />
            <paginationIcons />
            <paginationAlignment />
            <activeAndDisabled />
            <paginationColor />
            <paginationSizing />
        </div>
    </div>
</template>
<script>
import pagination from "@/components/advance/pagination/paginationPage.vue"
import paginationIcons from "@/components/advance/pagination/paginationIcons.vue"
import paginationAlignment from "@/components/advance/pagination/paginationAlignment.vue"
import activeAndDisabled from "@/components/advance/pagination/activeAndDisabled.vue"
import paginationColor from "@/components/advance/pagination/paginationColor.vue"
import paginationSizing from "@/components/advance/pagination/paginationSizing.vue"
export default {
    components: {
        pagination,
        paginationIcons,
        paginationAlignment,
        activeAndDisabled,
        paginationColor,
        paginationSizing
    }
}
</script>