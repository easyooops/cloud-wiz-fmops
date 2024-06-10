<template>
    <div class="tab-pane" id="radio">
        <draggable :group="{ name: 'universalGroup', pull: 'clone', put: false }">
            <div class="component" id="multiple">
                <div class="mb-3 row">
                    <label class="col-sm-3 form-label text-lg-start" for="radios">Multiple Radios</label>
                    <div class="col-sm-9 pl-md-radios">
                        <div class="radio">
                            <label for="radios-0">Option one</label>
                            <input type="radio" name="radios" id="radios-5" value="1" checked="checked">
                        </div>
                        <div class="radio">
                            <label for="radios-1">Option two</label>
                            <input type="radio" name="radios" id="radios-6" value="2">
                        </div>
                    </div>
                </div>
            </div>
            <div class="component" id="inline">
                <div class="mb-3 row">
                    <label class="col-sm-3 form-label text-lg-start" for="radios">Inline Radios</label>
                    <div class="col-sm-9  pl-md-radios">
                        <div class="m-checkbox-inline">
                            <div class="radio radio-primary">
                                <label class="radio-inline" for="radios-0"> 1</label>
                                <input type="radio" name="radios" id="radios-0" value="1" checked="checked">
                            </div>
                            <div class="radio radio-primary">
                                <label class="radio-inline" for="radios-1"> 2</label>
                                <input type="radio" name="radios" id="radios-1" value="2">
                            </div>
                            <div class="radio radio-primary">
                                <label class="radio-inline" for="radios-2"> 3</label>
                                <input type="radio" name="radios" id="radios-2" value="3">
                            </div>
                            <div class="radio radio-primary">
                                <label class="radio-inline" for="radios-3"> 4</label>
                                <input type="radio" name="radios" id="radios-3" value="4">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="component" id="cmuliple">
                <div class="mb-3 row">
                    <label class="col-sm-3 form-label text-lg-start" for="checkboxes">Multiple Checkboxes</label>
                    <div class="col-sm-9">
                        <div class="checkbox">
                            <input type="checkbox" name="checkboxes" id="checkboxes-0" value="1">
                            <label for="checkboxes-0" class="mt-0">Option one</label>
                        </div>
                        <div class="checkbox">
                            <input type="checkbox" name="checkboxes" id="checkboxes-1" value="2">
                            <label for="checkboxes-1" class="mt-0">Option two </label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="component" id="cinline">
                <div class="mb-3 row mb-0">
                    <label class="col-sm-3 form-label text-lg-start mb-0" for="checkboxes">Inline Checkboxes</label>
                    <div class="col-sm-9">
                        <div class="m-checkbox-inline">
                            <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-7" value="1">
                                <label class="checkbox-inline mb-0" for="checkboxes-0">1 </label>
                            </div>
                            <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-8" value="2">
                                <label class="checkbox-inline mb-0" for="checkboxes-1">2 </label>
                            </div>
                            <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-9" value="3">
                                <label class="checkbox-inline mb-0" for="checkboxes-2"> 3 </label>
                            </div>
                            <div class="checkbox"> <input type="checkbox" name="checkboxes" id="checkboxes-10" value="4">
                                <label class="checkbox-inline mb-0" for="checkboxes-3"> 4</label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </draggable>
    </div>
</template>
<script>
import { VueDraggableNext } from 'vue-draggable-next'
export default {
    inject: ['list'],
    data() {
        return {
            text: '', lista: []
        }
    },
    components: {
        draggable: VueDraggableNext,
    },
    methods: {
        finish() {
            if (document.getElementById('formhtml') === null) { this.text = '' }
            else {
                document.getElementById('formhtml').innerHTML = document.getElementById('formhtml').outerHTML
                this.text = document.getElementById('formhtml').innerHTML
            }
        },
    },
    mounted() {
        this.lista = this.list
    }
}
</script>