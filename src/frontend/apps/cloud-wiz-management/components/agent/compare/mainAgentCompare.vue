<template>
    <div class="email-wrap bookmark-wrap">
        <div class="row">
            <div class="col-xl-4 box-col-6">
                <div class="md-sidebar">
                    <div class="md-sidebar-aside email-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                        <div class="card">
                            <div class="card-body">
                                <div class="email-app-sidebar left-bookmark">
                                    <div class="media">
                                        <div class="media-size-email">
                                            <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                        </div>
                                        <div class="media-body">
                                            <h6 class="f-w-700">Prompt</h6>
                                            <p>Cloudwiz AI FMOps</p>
                                        </div>
                                        <ul class="list-inline float-start float-sm-end chat-menu-icons">
                                            <li class="list-inline-item">
                                                <a href="#"><i class="fa fa-code"></i></a>
                                            </li>
                                        </ul>                                            
                                    </div>
                                    <ul class="nav main-menu contact-options" role="tablist">
                                        <prompt />
                                    </ul>                                  
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-xl-4 box-col-6">
                <div class="md-sidebar">
                    <div class="md-sidebar-aside email-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                        <div class="card">
                            <div class="card-body">
                                <div class="email-app-sidebar left-bookmark">
                                    <div class="media">
                                        <div class="media-size-email">
                                            <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                        </div>
                                        <div class="media-body">
                                            <h6 class="f-w-700">Prompt</h6>
                                            <p>Cloudwiz AI FMOps</p>
                                        </div>
                                        <ul class="list-inline float-start float-sm-end chat-menu-icons">
                                            <li class="list-inline-item">
                                                <a href="#"><i class="fa fa-code"></i></a>
                                            </li>
                                        </ul>                                            
                                    </div>
                                    <ul class="nav main-menu contact-options" role="tablist">
                                        <prompt />
                                    </ul>                                  
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-xl-4 box-col-6">
                <div class="md-sidebar">
                    <div class="md-sidebar-aside email-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                        <div class="card">
                            <div class="card-body">
                                <div class="email-app-sidebar left-bookmark">
                                    <div class="media">
                                        <div class="media-size-email">
                                            <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                        </div>
                                        <div class="media-body">
                                            <h6 class="f-w-700">Prompt</h6>
                                            <p>Cloudwiz AI FMOps</p>
                                        </div>
                                        <ul class="list-inline float-start float-sm-end chat-menu-icons">
                                            <li class="list-inline-item">
                                                <a href="#"><i class="fa fa-code"></i></a>
                                            </li>
                                        </ul>                                            
                                    </div>
                                    <ul class="nav main-menu contact-options" role="tablist">
                                        <prompt />
                                    </ul>                                  
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import prompt from './prompt.vue'
import menu from '@/data/contact.json'
import { useContactStore } from '~~/store/contact'
export default {
    name: 'agent',
    data() {
        return {
            activeclass: 'pills-personal-tab', menu: menu.data, filtered: false
        }
    },
    computed: {
        selectedUser() {
            return useContactStore().selectedUser1
        }
    },
    components: {
        prompt
    },
    methods: {
        active(item) {
            this.activeclass = item
        },
        collapseFilter() {
            this.filtered = !this.filtered
        },
        getImageUrl(path) {
            return ('/images/' + path)
        }
    },
}
</script>

<style scoped>
.left-bookmark {
    height: 840px;
}
.bookmark-tabcontent {
    height: 880px;
}
.media { margin-bottom: 10px;}
.fa {
    font: normal normal normal 30px / 1 FontAwesome;
    margin-right: 10px;
}

</style>
