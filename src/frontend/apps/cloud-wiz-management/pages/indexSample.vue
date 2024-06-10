<template>
    <div>
        <defaultDashboard />
    </div>
</template>
<script>
import defaultDashboard from './dashboard/default12Sample.vue'
definePageMeta({
  layout: 'default-sample'
})
export default {
    components: {
        defaultDashboard
    }
}
</script>
