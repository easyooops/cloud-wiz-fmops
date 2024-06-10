<template>
    <div class="tab-pane fade" id="pills-select" role="tabpanel" aria-labelledby="pills-select-tab">
        <form class="theme-form">
            <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                <div class="mb-3 draggable">
                    <label for="formcontrol-select1">Example select</label>
                    <select class="form-control btn-square" id="formcontrol-select1">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                    </select>
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label for="formcontrol-select2">Example multiple select</label>
                    <select class="form-control btn-square" id="formcontrol-select2" multiple>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                    </select>
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