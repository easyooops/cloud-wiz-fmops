<template>
    <div class="col-12">
        <div class="card">
            <div class="card-header ">
                <h3>Custom Board </h3>
                <p class="mb-0">| colors, gutter, click on board&apos;s item and restricting which boards to drag items to
                </p>
            </div>
            <div class="card-body">
                <div id="demo2">
                    <div class="kanban-container" style="width: 1290px;">
                        <draggable>
                            <div data-id="_todo" data-order="1" class="kanban-board"
                                style="width: 400px; margin-left: 15px; margin-right: 15px;position: relative;float: left;"
                                v-for="index in columns" :key="index.title">
                                <header class="kanban-board-header" :class="index.bgclass">
                                    <div class="kanban-title-board">{{ index.title }} (Item only in Working)</div>
                                </header>
                                <draggable :list="index.tasks" :animation="200" ghost-class="ghost-card" group="tasks"
                                    style="min-height: 100px">
                                    <div class="kanban-item" v-for="(task) in index.tasks" :key="task.id"
                                        :class="index.lightbgclass">
                                        <a class="kanban-box" href="javascript:void(0)" data-bs-original-title="" title="">
                                            <span class="date">{{ task.date }}</span>
                                            <span class="badge f-right" :class="task.badgetype">{{ task.badge }}</span>
                                            <h6>{{ task.title }}</h6>
                                            <div class="media">
                                                <img class="img-20 me-1 rounded-circle" src="/images/user/3.jpg" alt=""
                                                    data-original-title="" title="">
                                                <div class="media-body">
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
                                <footer></footer>
                            </div>
                        </draggable>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { VueDraggableNext } from 'vue-draggable-next'
import kanban from "@/mixin/kanban"

export default {
    name: "App",
    mixins: [kanban],
    components: {
        draggable: VueDraggableNext,
    },
};
</script>