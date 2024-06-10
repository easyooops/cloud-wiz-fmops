<template>
    <div class="col-xl-3 box-col-6">
        <div class="md-sidebar"><a class="btn btn-primary md-sidebar-toggle" @click="collapse()">Task filter</a>
            <div class="md-sidebar-aside job-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                <div class="email-left-aside">
                    <div class="card">
                        <div class="card-body">
                            <div class="email-app-sidebar left-bookmark task-sidebar">
                                <div class="media">
                                    <div class="media-size-email"><img class="me-3 rounded-circle"
                                            src="/images/user/user.png" alt=""></div>
                                    <div class="media-body">
                                        <h6 class="f-w-600">MARK JENCO</h6>
                                        <p>Markjecno@gmail.com</p>
                                    </div>
                                </div>
                                <ul class="nav main-menu" role="tablist">
                                    <newTask />
                                    <li class="nav-item"><span class="main-title"> Views</span></li>
                                    <li><a :class="this.activeTab == 'pills-created-tab' ? 'active' : ''"
                                            id="pills-created-tab" data-bs-toggle="pill" href="#pills-created" role="tab"
                                            aria-controls="pills-created" aria-selected="true"><span class="title"
                                                @click="active('pills-created-tab')"> Created by me</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-todaytask-tab' ? 'active' : ''"
                                            id="pills-todaytask-tab" data-bs-toggle="pill" href="#pills-todaytask"
                                            role="tab" aria-controls="pills-todaytask" aria-selected="false"><span
                                                class="title" @click="active('pills-todaytask-tab')"> Today's
                                                Tasks</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-delayed-tab' ? 'active' : ''"
                                            id="pills-delayed-tab" data-bs-toggle="pill" href="#pills-delayed" role="tab"
                                            aria-controls="pills-delayed" aria-selected="false"><span class="title"
                                                @click="active('pills-delayed-tab')"> Delayed Tasks</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-upcoming-tab' ? 'active' : ''"
                                            id="pills-upcoming-tab" data-bs-toggle="pill" href="#pills-upcoming" role="tab"
                                            aria-controls="pills-upcoming" aria-selected="false"><span class="title"
                                                @click="active('pills-upcoming-tab')">Upcoming Tasks</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-weekly-tab' ? 'active' : ''"
                                            id="pills-weekly-tab" data-bs-toggle="pill" href="#pills-weekly" role="tab"
                                            aria-controls="pills-weekly" aria-selected="false"><span class="title"
                                                @click="active('pills-weekly-tab')">This week tasks</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-monthly-tab' ? 'active' : ''"
                                            id="pills-monthly-tab" data-bs-toggle="pill" href="#pills-monthly" role="tab"
                                            aria-controls="pills-monthly" aria-selected="false"><span class="title"
                                                @click="active('pills-monthly-tab')">This month tasks</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-assigned-tab' ? 'active' : ''"
                                            id="pills-assigned-tab" data-bs-toggle="pill" href="#pills-assigned" role="tab"
                                            aria-controls="pills-assigned" aria-selected="false"><span class="title"
                                                @click="active('pills-assigned-tab')">Assigned to me</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-tasks-tab' ? 'active' : ''"
                                            id="pills-tasks-tab" data-bs-toggle="pill" href="#pills-tasks" role="tab"
                                            aria-controls="pills-tasks" aria-selected="false"><span class="title"
                                                @click="active('pills-tasks-tab')">My tasks</span></a></li>
                                    <li>
                                        <hr>
                                    </li>
                                    <addTags />
                                    <li><a class="show" :class="this.activeTab == 'pills-notification-tab' ? 'active' : ''"
                                            id="pills-notification-tab" data-bs-toggle="pill" href="#pills-notification"
                                            role="tab" aria-controls="pills-notification" aria-selected="false"><span
                                                class="title" @click="active('pills-notification-tab')">
                                                Notification</span></a></li>
                                    <li><a class="show" :class="this.activeTab == 'pills-newsletter-tab' ? 'active' : ''"
                                            id="pills-newsletter-tab" data-bs-toggle="pill" href="#pills-newsletter"
                                            role="tab" aria-controls="pills-newsletter" aria-selected="false"><span
                                                class="title" @click="active('pills-newsletter-tab')"> Newsletter</span></a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="col-xl-9 col-md-12 box-col-12">
        <div class="email-right-aside bookmark-tabcontent">
            <div class="card email-body radius-left">
                <div class="ps-0">
                    <div class="tab-content">
                        <createdMe />
                        <someTask />
                        <assignTask />
                        <myTask />
                        <newsTask />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import assignTask from './assignTask.vue'
import myTask from './myTask.vue'
import newsTask from './newsTask.vue'
import someTask from './someTask.vue'
import createdMe from './createdMe.vue'
import { useTagStore } from '~~/store/tags'
import addTags from './addTags.vue'
import newTask from './newTask.vue'
export default {
    components: {
        newTask, addTags, createdMe, myTask, someTask, newsTask, assignTask
    },
    computed: {
        activeTab() {
            return useTagStore().activeclass
        }
    },
    data() {
        return {
            filtered: false,
        }
    },
    methods: {
        active: function (message) {
            useTagStore().active(message)
        },
        collapse() {
            this.filtered = !this.filtered
        }
    },
}
</script>