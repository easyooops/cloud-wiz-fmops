<template>
    <Breadcrumbs main="Provider" title="Providers List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <providerHeader />
        </div>
    </div>
</template>

<script>
import providerHeader from '../list/providerHeader.vue'
export default {
    name: 'indexList',
    components: {
        providerHeader
    },

}

</script>
