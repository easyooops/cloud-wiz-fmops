<template>
    <Breadcrumbs main="Storage" title="Storage List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <storageHeader />
        </div>
    </div>
</template>

<script>
import storageHeader from '../list/storageHeader.vue'
export default {
    name: 'indexList',
    components: {
        storageHeader
    },

}

</script>
