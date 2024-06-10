<template>
    <div class="card">
        <div class="card-header b-bottom">
            <div class="todo-list-header">
                <div class="new-task-wrapper input-group">
                    <input class="form-control" id="new-task" placeholder="Enter new task here. . ."
                        v-on:keyup.enter="addnewtask" v-model="task"><span
                        class="btn btn-primary d-flex input-group-text add-new-task-btn" id="add-task"
                        @click="addnewtask()">Add Task</span>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="todo">
                <div class="todo-list-wrapper">
                    <div class="todo-list-container">
                        <div class="todo-list-body custom-scrollbar">
                            <ul id="todo-list">
                                <li v-for="(todo, index) in todolist" :key="index" class="task"
                                    :class="{ 'completed': todo.status == 'complete' }">
                                    <div class="task-container">
                                        <h4 class="task-label "> {{ todo.title }} </h4>
                                        <div class="d-flex align-items-center gap-4"><span class="badge "
                                                :class="todo.badgeClass">{{ todo.priority }}</span>
                                            <h5 class="assign-name m-0">{{ todo.date }}</h5>
                                            <span class="task-action-btn">
                                                <span @click="tododelete(todo.id)" class="action-box large delete-btn"
                                                    title="Delete Task"><i class="icon"><i
                                                            class="icon-trash"></i></i></span>
                                                <span @click="taskcomplete(todo.id, todo.status)"
                                                    class="action-box large complete-btn" title="Mark Complete"><i
                                                        class="icon"><i class="icon-check"></i></i></span>
                                            </span>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from 'pinia';
import { useTodoStore } from '~~/store/todo';
export default {
    data() {
        return {
            markallread: true, task: '',
            addtask: false, showinputBox: false
        }
    },
    computed: {
        ...mapState(useTodoStore, { todolist: 'todo' })
    },
    methods: {
        addnewtask() {
            if (this.task !== '') {
                useTodoStore().addtodo(this.task)
                this.task = ''; this.addtask = false;
                useNuxtApp().$showToast({ msg: " Task list is updated ", type: "success" })
            }
        },
        alltaskcomplete() {
            useTodoStore().alltaskcomplete(this.markallread)
            this.markallread = !this.markallread;
            if (this.markallread)
                useNuxtApp().$showToast({ msg: " All tasks marked as Incomplete. ", type: "error" })
            else
                useNuxtApp().$showToast({ msg: 'All tasks marked as complete.', type: "success" })
        },
        tododelete(id) {
            useTodoStore().tododelete(id)
            useNuxtApp().$showToast({ msg: 'Task has been deleted.', type: "success" })
        },
        taskcomplete(id, status) {
            useTodoStore().taskcomplete(id)
            if (status !== 'complete')
                useNuxtApp().$showToast({ msg: 'Task has been complete.', type: "success" })
            else
                useNuxtApp().$showToast({ msg: 'Task has been incomplete.', type: "error" })
        },
    },
}
</script>