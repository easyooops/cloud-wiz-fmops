<template>
    <Breadcrumbs main="Agent" title="Agents List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <agentHeader />
        </div>
    </div>
</template>

<script>
import agentHeader from '../list/agentHeader.vue'
export default {
    name: 'indexList',
    components: {
        agentHeader
    },

}

</script>
