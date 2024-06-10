<template>
    <div class="tab-pane" id="buttons">
        <draggable :group="{ name: 'universalGroup', pull: 'clone', put: false }">

            <div class="component" id="file">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="filebutton">File Button</label>
                    <div class="col-lg-12">
                        <input id="filebutton" name="filebutton" class="input-file" type="file">
                    </div>
                </div>
            </div>
            <div class="component" id="single">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="singlebutton">Single Button</label>
                    <div class="col-lg-12">
                        <button id="singlebutton" name="singlebutton" class="btn btn-primary">Button</button>
                    </div>
                </div>
            </div>
            <div class="component" id="double">
                <div class="mb-3 row mb-0">
                    <label class="col-lg-12 form-label text-lg-start" for="button1id">Double Button</label>
                    <div class="col-md-9">
                        <button id="button1id" name="button1id" class="btn btn-success">Good Button</button>
                        <button id="button2id" name="button2id" class="btn btn-danger">Scary Button</button>
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