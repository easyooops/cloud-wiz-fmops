<template>
    <div class="tab-pane fade" id="pills-button" role="tabpanel" aria-labelledby="pills-button-tab">
        <form class="theme-form">
            <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                <div class="mb-3 draggable">
                    <label class="m-r-10">Single Button</label><br>
                    <button class="btn btn-primary active" type="button" data-original-title="btn btn-dark active"
                        title="">Button</button>
                    <p class="help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label class="m-r-10">Double Button</label><br>
                    <button class="btn btn-primary" type="button" data-original-title="btn btn-primary-gradien"
                        title="">Primary</button>
                    <button class="btn btn-secondary" type="button" data-original-title="btn btn-primary-gradien"
                        title="">Secondary</button>
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