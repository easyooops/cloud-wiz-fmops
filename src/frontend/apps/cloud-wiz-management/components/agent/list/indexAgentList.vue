<template>
    <Breadcrumbs main="Agent" title="Agents List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <agentHeader />
            <Modal />
        </div>
    </div>
</template>

<script>
import agentHeader from '../list/agentHeader.vue'
import Modal from './modal.vue';
export default {
    name: 'indexList',
    components: {
        agentHeader,
        Modal
    },

}

</script>
