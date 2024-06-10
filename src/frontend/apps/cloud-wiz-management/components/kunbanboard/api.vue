<template>
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h3>API</h3>
                <p class="mb-0">add item, add board, delete board: </p>
            </div>
            <div class="card-body">
                <div id="demo3">
                    <div class="kanban-container" style="width: 1290px;">
                        <draggable>
                            <div data-id="_todo" data-order="1" class="kanban-board"
                                style="width: 400px; margin-left: 15px; margin-right: 15px;" v-for="index in columns"
                                :key="index.title">
                                <header class="kanban-board-header info">
                                    <div class="kanban-title-board">{{ index.title }}</div>
                                </header>

                                <main class="kanban-drag">
                                    <draggable :list="index.tasks" :animation="200" ghost-class="ghost-card" group="tasks">
                                        <div class="kanban-item" v-for="(task) in index.tasks" :key="task.id">
                                            <a class="kanban-box" href="#"><span class="date">{{ task.date }}</span><span
                                                    class="badge badge-danger f-right">Argent</span>
                                                <img v-if="task.imagee == 'done'" class="mt-2 img-fluid"
                                                    src="/images/other-images/sidebar-bg.jpg" alt="" data-original-title=""
                                                    title="">
                                                <img v-if="task.imagee == 'working'" class="mt-2 img-fluid"
                                                    src="/images/other-images/maintenance-bg.jpg" alt=""
                                                    data-original-title="" title="">
                                                <h6>Test Sidebar</h6>
                                                <div class="media"><img class="img-20 me-1 rounded-circle"
                                                        src="/images/user/3.jpg" alt="" data-original-title="" title="">
                                                    <div class="media-body">
                                                        <p>Themeforest, australia</p>
                                                    </div>
                                                </div>
                                                <div class="d-flex mt-3">
                                                    <ul class="list">
                                                        <li><i class="fa fa-comments-o"></i>2</li>
                                                        <li><i class="fa fa-paperclip"></i>2</li>
                                                        <li><i class="fa fa-eye"></i></li>
                                                    </ul>
                                                    <div class="customers">
                                                        <ul>
                                                            <li class="d-inline-block me-3">
                                                                <p class="f-12">+5</p>
                                                            </li>
                                                            <li class="d-inline-block"><img class="img-20 rounded-circle"
                                                                    src="/images/user/3.jpg" alt="" data-original-title=""
                                                                    title=""></li>
                                                            <li class="d-inline-block"><img class="img-20 rounded-circle"
                                                                    src="/images/user/1.jpg" alt="" data-original-title=""
                                                                    title=""></li>
                                                            <li class="d-inline-block"><img class="img-20 rounded-circle"
                                                                    src="/images/user/5.jpg" alt="" data-original-title=""
                                                                    title=""></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </a>
                                        </div>
                                    </draggable>
                                </main>
                                <footer></footer>
                            </div>
                        </draggable>
                    </div>
                </div>
                <button class="btn btn-success" id="addDefault" @click.prevent="add">Add &quot;Default&quot; board</button>
                <button class="btn btn-success" id="addToDo" @click="addelment">Add element in &quot;To Do&quot;
                    Board</button>
                <button class="btn btn-danger" id="removeBoard" @click="remove">Remove &quot;Done&quot; Board</button>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    columns
} from "@/data/kanban/kanban.json"
import {
    VueDraggableNext
} from 'vue-draggable-next'
export default {
    name: "App",
    components: {
        draggable: VueDraggableNext,
    },
    data() {
        return {
            columns: columns,
        }
    },
    methods: {
        add() {
            this.columns.push({
                title: "default",
                tasks: [{
                    id: 1,

                    title: "Design Dashboard",
                    date: "23/07/20",
                    badge: "medium",
                    badgetype: "badge-primary",
                    location: "Themeforest, australia",
                },
                {
                    id: 2,

                    title: "Test Sidebar",
                    date: "24/7/20",
                    badge: "Urgent",
                    badgetype: "badge-danger",
                    location: "Themeforest, australia",
                },

                ]
            })
        },
        addelment() {
            this.columns[0].tasks.push({
                id: 1,
                title: "Design Dashboard",
                date: "23/07/20",
                badge: "medium",
                badgetype: "badge-primary",
                location: "Themeforest, australia",
            })
        },
        remove() {
            this.columns.forEach((element, index) => {
                if (element.title === 'Done') {
                    this.columns.splice(index, 1)
                }
            })
        }
    }
};
</script>
    