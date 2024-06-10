<template>
    <li class="nav-item">
        <button class="badge-light-primary btn-block btn-mail w-100" type="button" data-bs-toggle="modal"
            data-bs-target="#exampleModal"><vue-feather class="me-2" type="check-circle"></vue-feather>New Task</button>
        <Teleport to="body">
            <div class="modal fade modal-bookmark" id="exampleModal" tabindex="-1" role="dialog"
                aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="exampleModalLabel">Add Task</h5>
                            <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"> </button>
                        </div>
                        <div class="modal-body">
                            <form class="form-bookmark needs-validation" id="bookmark-form" novalidate="">
                                <div class="row">
                                    <div class="mb-3 mt-0 col-md-12">
                                        <label for="task-title">Task Title</label>
                                        <input class="form-control" id="task-title" type="text" v-model="name" required=""
                                            autocomplete="off">
                                    </div>
                                    <div class="mb-3 mt-0 col-md-12">
                                        <label for="sub-task">Sub task</label>
                                        <input class="form-control" id="sub-task" type="text" required="" v-model="type"
                                            autocomplete="off">
                                    </div>
                                    <div class="mb-3 mt-0 col-md-12">
                                        <div class="d-flex date-details">
                                            <div class="d-inline-block">
                                                <label class="d-block mb-0"><input class="checkbox_animated"
                                                        type="checkbox">Remind on
                                                </label>
                                            </div>
                                            <div class="d-inline-block">
                                                <input class="datepicker-here form-control digits" type="text"
                                                    data-language="en" placeholder="Date">
                                            </div>
                                            <div class="d-inline-block">
                                                <select class="form-control">
                                                    <option>7:00 am</option>
                                                    <option>7:30 am</option>
                                                    <option>8:00 am</option>
                                                    <option>8:30 am</option>
                                                    <option>9:00 am</option>
                                                    <option>9:30 am</option>
                                                    <option>10:00 am</option>
                                                    <option>10:30 am</option>
                                                    <option>11:00 am</option>
                                                    <option>11:30 am</option>
                                                    <option>12:00 pm</option>
                                                    <option>12:30 pm</option>
                                                    <option>1:00 pm</option>
                                                    <option>2:00 pm</option>
                                                    <option>3:00 pm</option>
                                                    <option>4:00 pm</option>
                                                    <option>5:00 pm</option>
                                                    <option>6:00 pm</option>
                                                </select>
                                            </div>
                                            <div class="d-inline-block">
                                                <label class="d-block mb-0"><input class="checkbox_animated"
                                                        type="checkbox">Notification
                                                </label>
                                            </div>
                                            <div class="d-inline-block">
                                                <label class="d-block mb-0">
                                                    <input class="checkbox_animated" type="checkbox">Mail
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mb-3 mt-0 col-md-6">
                                        <select class="js-example-basic-single">
                                            <option value="task">My Task</option>
                                        </select>
                                    </div>
                                    <div class="mb-3 mt-0 col-md-6">
                                        <select class="js-example-disabled-results" id="bm-collection">
                                            <option value="general">General</option>
                                        </select>
                                    </div>
                                    <div class="mb-3 mt-0 col-md-6">
                                        <textarea class="form-control" required="" v-model="desc"
                                            autocomplete="off">  </textarea>
                                    </div>
                                </div>
                                <input id="index_var" type="hidden" value="6">
                                <button class="btn btn-secondary" type="submit" id="Bookmark" @click="submitBookmark()"
                                    data-bs-dismiss="modal">Save</button>
                                <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel </button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </Teleport>
    </li>
</template>
<script>
import { useTagStore } from '~~/store/tags'
export default {
    data() {
        return {
            name: '', type: '', desc: ''
        }
    },
    methods: {
        submitBookmark() {
            let arr = { name: this.name, type: this.type, desc: this.desc }
            useTagStore().add(arr)
        }
    },
}
</script>