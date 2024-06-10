<template>
    <div class="tab-pane fade" id="pills-radcheck" role="tabpanel" aria-labelledby="pills-radcheck-tab">
        <form class="theme-form">
            <draggable @end="finish" :group="{ name: 'universalGroup', pull: 'clone', put: false }">
                <div class="mb-3 draggable">
                    <label>Inline checkbox</label>
                    <div class="col">
                        <div class="m-checkbox-inline">
                            <div class="checkbox">
                                <input id="checkbox1" type="checkbox">
                                <label for="checkbox1">Default 1</label>
                            </div>
                            <div class="checkbox">
                                <input id="checkbox2" type="checkbox">
                                <label for="checkbox2">Default 2</label>
                            </div>
                            <div class="checkbox">
                                <input id="checkbox3" type="checkbox">
                                <label for="checkbox3">Default 3</label>
                            </div>
                        </div>
                    </div>
                    <p class="help-block m-t-help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label>Inline Radiobox</label>
                    <div class="col">
                        <div class="m-checkbox-inline">
                            <div class="radio radio-theme">
                                <input id="radioinline1" type="radio" name="radio1" value="option1">
                                <label for="radioinline1">Option 1</label>
                            </div>
                            <div class="radio radio-theme">
                                <input id="radioinline2" type="radio" name="radio1" value="option2">
                                <label for="radioinline2">Option 2</label>
                            </div>
                            <div class="radio radio-theme">
                                <input id="radioinline3" type="radio" name="radio1" value="option3">
                                <label for="radioinline3">Option 3</label>
                            </div>
                        </div>
                    </div>
                    <p class="help-block m-t-help-block">Example block-level help text here.</p>
                </div>
                <hr>
                <div class="mb-3 draggable">
                    <label>Custom checkbox</label>
                    <div class="col">
                        <div class="checkbox">
                            <input id="checkbox-def" type="checkbox">
                            <label for="checkbox-def">Default</label>
                        </div>
                        <div class="checkbox">
                            <input id="checkbox-dis" type="checkbox" disabled="">
                            <label for="checkbox-dis">Disabled</label>
                        </div>
                        <div class="checkbox">
                            <input id="checkbox-chk" type="checkbox" checked="">
                            <label for="checkbox-chk">Checked</label>
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