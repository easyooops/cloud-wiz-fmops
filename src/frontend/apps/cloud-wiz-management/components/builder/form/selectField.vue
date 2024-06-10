<template>
    <div class="tab-pane" id="select">
        <draggable :group="{ name: 'universalGroup', pull: 'clone', put: false }">
            <div class="component" id="basic">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="selectbasic">Select Basic</label>
                    <div class="col-lg-12">
                        <select id="selectbasic" name="selectbasic" class="form-control btn-square">
                            <option value="1">Option one</option>
                            <option value="2">Option two</option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="component" id="smultiple">
                <div class="mb-3 row mb-0">
                    <label class="col-lg-12 form-label text-lg-start" for="selectmultiple">Select Multiple</label>
                    <div class="col-lg-12">
                        <select id="selectmultiple" name="selectmultiple" class="form-control btn-square" multiple>
                            <option value="1">Option one</option>
                            <option value="2">Option two</option>
                        </select>
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