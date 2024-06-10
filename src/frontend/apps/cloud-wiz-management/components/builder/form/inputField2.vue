<template>
    <div class="tab-pane fade show active" id="pills-input" role="tabpanel" aria-labelledby="pills-input-tab">
        <form class="theme-form">
            <draggable @end="finish($event)" :group="{ name: 'universalGroup', pull: 'clone', put: false }">
                <div class="mb-3 draggable" id="input">
                    <label for="input-text-1">Text Input</label>
                    <input class="form-control btn-square" id="input-text-1" type="email" placeholder="Enter email">
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <p class="tools" id="add">
                    <a class="edit-link">Edit HTML</a>
                    <a class="remove-link">Remove</a>
                </p>
                <hr>
                <div class="mb-3 draggable">
                    <label for="input-password-1">Password</label>
                    <input class="form-control btn-square" id="input-password-1" type="password" placeholder="Password">
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label for="select-1">Select</label>
                    <select class="form-control btn-square" id="select-1">
                        <option value="Option 1">Option 1</option>
                        <option value="Option 2">Option 2</option>
                        <option value="Option 3">Option 3</option>
                    </select>
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label for="input-file-1">File input</label>
                    <input id="input-file-1" type="file">
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label for="prependedcheckbox">Appended Checkbox</label>
                    <div class="input-group"><span class="input-group-text">
                            <input class="me-0" type="checkbox"></span>
                        <input class="form-control btn-square" id="prependedcheckbox" name="prependedcheckbox" type="text"
                            placeholder="Placeholder">
                    </div>
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label for="prependedcheckbox">Button DropDown</label>
                    <div class="input-group">
                        <input class="form-control btn-square" id="buttondropdown" name="buttondropdown"
                            placeholder="Placeholder" type="text">
                        <div class="input-group-btn btn btn-square p-0">
                            <button class="btn btn-primary dropdown-toggle btn-square" type="button"
                                data-bs-toggle="dropdown">Action<span class="caret"></span></button>
                            <ul class="dropdown-menu pull-right">
                                <li><a class="dropdown-item" href="#">Option one</a></li>
                                <li><a class="dropdown-item" href="#">Option two</a></li>
                                <li><a class="dropdown-item" href="#">Option three</a></li>
                            </ul>
                        </div>
                    </div>
                    <p class="help-block">Example block-level help text here.</p>
                </div>
            </draggable>
        </form>
    </div>
</template>
<script>
import { VueDraggableNext } from 'vue-draggable-next'
import { list } from '@/data/draggable'
export default {
    data() {
        return {
            display: false, show: 1, text: '', lista: list
        }
    },
    components: {
        draggable: VueDraggableNext,
    },
    methods: {
        change(e) {
            this.show = e.target.value
        },
        finish(e) {
            if (process.client) {
                var a = document.getElementById(e.item.id)
                if (document.getElementById(e.item) == null) {
                    a[0].append(document.getElementById('add').outerHTML)
                }
                if (document.getElementById('formhtml') === null) {
                    this.text = ''
                } else {
                    document.getElementById('formhtml').innerHTML = document.getElementById('formhtml').outerHTML
                    this.text = document.getElementById('formhtml').innerHTML
                }
            }
        },
    }
}
</script>