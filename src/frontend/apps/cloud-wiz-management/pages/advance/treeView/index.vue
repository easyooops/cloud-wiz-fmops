<template>
    <Breadcrumbs title="Calender Basic" main="Bonus UI" />
    <div class="container-fluid">
        <div class="row">
            <basicPage />
            <checkboxPage />
            <dragPage />
            <contextPage />
        </div>
    </div>
</template>
<script>
import basicPage from '@/components/advance/treeView/basicPage.vue'
import checkboxPage from '@/components/advance/treeView/checkboxPage.vue'
import contextPage from '@/components/advance/treeView/contextPage.vue'
import dragPage from '@/components/advance/treeView/dragPage.vue'
export default {
    components: {
        basicPage, checkboxPage, dragPage, contextPage
    }
}
</script>
