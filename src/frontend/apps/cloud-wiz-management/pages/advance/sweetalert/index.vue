<template>
    <Breadcrumbs title="Sweetalert" main="Bonus UI" />
    <div class="container-fluid">
        <div class="row">
            <basicExample />
            <advanceState />
            <alertPage />
        </div>
    </div>
</template>
<script>
import basicExample from '@/components/advance/sweetalert/basicExample.vue'
import advanceState from '@/components/advance/sweetalert/advancedState.vue'
import alertPage from '@/components/advance/sweetalert/alertState.vue'
export default {
    components: {
        basicExample,
        advanceState,
        alertPage
    }
}
</script>

