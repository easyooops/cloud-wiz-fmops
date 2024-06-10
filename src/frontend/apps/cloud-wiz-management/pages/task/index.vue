<template>
    <Breadcrumbs title="Tasks" main="Apps" />

    <div class="container-fluid">
        <div class="email-wrap bookmark-wrap">
            <div class="row">
                <addTask />
            </div>
        </div>
    </div>
</template>

<script>
import addTask from '@/components/task/addTask.vue'
export default {
    components: {
        addTask
    },
}
</script>
