<template>
    <Breadcrumbs title="To-Do" main="App" />

    <div class="container-fluid email-wrap bookmark-wrap todo-wrap">
        <div class="row">
            <todosidebar />
            <div class="col-xl-9 xl-70 box-col-12">
                <addtask />
            </div>
        </div>
    </div>
</template>
<script>
import todosidebar from '@/components/todo/todosidebar.vue'
import addtask from '@/components/todo/addtask.vue'
export default {
    components: {
        todosidebar,
        addtask
    }
}
</script>