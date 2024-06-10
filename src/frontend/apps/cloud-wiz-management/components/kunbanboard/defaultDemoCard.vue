<template>
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="mb-0">Default Demo </h5>
            </div>
            <div class="card-body">
                <div id="demo1">
                    <div class="kanban-container" style="width: 1290px;">
                        <draggable>
                            <div data-id="_todo" data-order="1" class="kanban-board"
                                style="width:400px; margin-left: 15px; margin-right: 15px;position: relative;float: left;"
                                v-for="index in columns" :key="index.title">
                                <header class="kanban-board-header">
                                    <div class="kanban-title-board">{{ index.title }}(2)</div>
                                </header>

                                <draggable :list="index.tasks" :animation="200" ghost-class="ghost-card" group="tasks"
                                    style="min-height: 100px">
                                    <div class="kanban-item" v-for="(task) in index.tasks" :key="task.id">
                                        <a class="kanban-box" href="javascript:void(0)" data-bs-original-title=""
                                            title=""><span class="date">{{ task.date }}</span><span class="badge f-right"
                                                :class="task.badgetype">{{ task.badge }}</span>
                                            <h6>{{ task.title }}</h6>
                                            <div class="d-flex align-items-start">
                                                <img class="img-20 me-1 rounded-circle" src="/images/user/3.jpg" alt=""
                                                    data-original-title="" title="">
                                                <div class="flex-grow-1">
                                                    <p>{{ task.location }}</p>
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
                                                            <p class="f-12">+10</p>
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

                            </div>
                        </draggable>
                    </div>
                </div>
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
    components: {
        draggable: VueDraggableNext,
    },
    data() {
        return {
            columns: columns
        }
    },
}
</script>
    
<style scoped>
.kanban-container {
    /* position: relative; */
    /* box-sizing: border-box; */
    width: auto;
}

.kanban-container * {
    box-sizing: border-box;
}

.kanban-container:after {
    clear: both;
    display: block;
    content: "";
}

.kanban-board {
    position: relative;
    float: left;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
}

.kanban-board.disabled-board {
    opacity: 0.3;
}

.kanban-board header {
    font-size: 16px;
    padding: 20px 30px;
}

.kanban-board header .kanban-title-board {
    font-weight: 500;
    margin: 0;
    padding: 0;
    display: inline;
}

.kanban-board header .kanban-title-button {
    float: right;
}

.kanban-board .kanban-drag {
    min-height: 200px;
    padding: 20px;
}

.kanban-board:after {
    clear: both;
    display: block;
    content: "";
}

.kanban-board.is-moving.gu-mirror {
    transform: rotate(3deg);
}

.kanban-board.is-moving.gu-mirror .kanban-drag {
    overflow: hidden;
    padding-right: 50px;
}

.kanban-item {
    background: #f8f8f8;
    padding: 15px;
    transition: all 0.3s cubic-bezier(0.23, 1, 0.32, 1);
    margin-bottom: 0;
}

.kanban-item:hover {
    cursor: move;
}

.kanban-item:last-child {
    margin: 0;
}

.kanban-item.is-moving.gu-mirror {
    transform: rotate(3deg);
    height: auto !important;
}

#myKanban {
    overflow-x: auto;
    padding: 20px 0;
}
</style>
    