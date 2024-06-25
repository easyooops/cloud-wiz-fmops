<template>
    <Breadcrumbs main="Trace" title="Trace List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <traceFilter />
            <traceLog />
        </div>
    </div>
</template>

<script>
import traceFilter from './traceFilter.vue'
import traceLog from './traceLog.vue'
export default {
    name: 'indexList',
    components: {
        traceFilter,
        traceLog
    },
}
</script>
