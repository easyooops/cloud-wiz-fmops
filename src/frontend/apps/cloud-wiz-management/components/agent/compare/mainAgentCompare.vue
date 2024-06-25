<template>
    <div class="email-wrap bookmark-wrap">
        <div class="row">
            <div class="col-xl-4 box-col-6">
                <div class="card">
                    <div class="card-body">
                        <div class="email-app-sidebar left-bookmark">
                            <div class="media">
                                <div class="media-size-email">
                                    <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                </div>
                                <div class="media-body">
                                    <select class="form-select form-control-primary" v-model="modelType">
                                        <option value="C">Default Chat Agent</option>
                                        <option value="T">Default Text Agent</option>
                                        <option value="I">Default Embedding Agent</option>
                                    </select>
                                </div>                                         
                            </div>
                            <ul class="nav main-menu contact-options" role="tablist">
                                <prompt />
                            </ul>                                  
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Token Usage</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Expected Cost</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>                        
                    </div>
                </div>                
            </div>

            <div class="col-xl-4 box-col-6">
                <div class="card">
                    <div class="card-body">
                        <div class="email-app-sidebar left-bookmark">
                            <div class="media">
                                <div class="media-size-email">
                                    <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                </div>
                                <div class="media-body">
                                    <select class="form-select form-control-primary" v-model="modelType">
                                        <option value="C">Default Chat Agent</option>
                                        <option value="T">Default Text Agent</option>
                                        <option value="I">Default Embedding Agent</option>
                                    </select>
                                </div>                                         
                            </div>
                            <ul class="nav main-menu contact-options" role="tablist">
                                <prompt />
                            </ul>                                  
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Token Usage</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Expected Cost</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>                        
                    </div>
                </div>                  
            </div>

            <div class="col-xl-4 box-col-6">
                <div class="card">
                    <div class="card-body">
                        <div class="email-app-sidebar left-bookmark">
                            <div class="media">
                                <div class="media-size-email">
                                    <li class="list-inline-item"><i class="fa fa-comments"></i></li>
                                </div>
                                <div class="media-body">
                                    <select class="form-select form-control-primary" v-model="modelType">
                                        <option value="C">Default Chat Agent</option>
                                        <option value="T">Default Text Agent</option>
                                        <option value="I">Default Embedding Agent</option>
                                    </select>
                                </div>                                         
                            </div>
                            <ul class="nav main-menu contact-options" role="tablist">
                                <prompt />
                            </ul>                                  
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Token Usage</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>
                        <div class="row">
                            <div class="col-xl-11">
                                <label class="col-form-label"><h6>Expected Cost</h6></label>
                            </div>
                            <div class="col-xl-1">
                                <label class="col-form-label">0</label>
                            </div>                        
                        </div>                        
                    </div>
                </div>                  
            </div>

            <div class="col-xl-12 box-col-6">
                <div class="row chat-box">
                    <div class="col pe-0">
                        <div class="chat">
                            <div class="chat-message clearfix">
                                <div class="row">
                                    <div class="col-xl-1 d-flex"></div>
                                    <div class="col-xl-9 d-flex">
                                        <div class="input-group text-box" ref="abc">
                                            <input class="form-control input-txt-bx" id="message-to-send" v-model="text" v-on:keyup.enter="addChat()"
                                                type="text" name="message-to-send" placeholder="Type a message......" />
                                        </div>
                                    </div>
                                    <div class="col-xl-1">
                                        <button @click="addChat()" class="btn btn-primary" type="button">
                                            <i class="fa fa-send-o"></i>
                                        </button>
                                    </div>
                                    <div class="col-xl-1 d-flex"></div>                                 
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
    height: 700px;
}
.bookmark-tabcontent {
    height: 700px;
}
.media { margin-bottom: 10px;}
.fa {
    font: normal normal normal 30px / 1 FontAwesome;
    margin-right: 10px;
}

</style>
