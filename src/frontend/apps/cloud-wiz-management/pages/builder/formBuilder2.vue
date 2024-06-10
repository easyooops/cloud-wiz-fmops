<template>
    <div class="form-builder">
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">
                    <div class="card">
                        <div class="card-header">
                            <h5>Form Builder</h5>
                        </div>
                        <div class="card-body form-builder">
                            <div class="form-builder-column">
                                <div class="row">
                                    <div class="col-sm-12">
                                        <div class="form-builder-2-header">
                                            <div>
                                                <ul class="nav nav-primary" id="pills-tab" role="tablist">
                                                    <li class="nav-item"><a class="nav-link active" id="pills-input-tab"
                                                            data-bs-toggle="pill" href="#pills-input" role="tab"
                                                            aria-controls="pills-input" aria-selected="true">Input</a></li>
                                                    <li class="nav-item"><a class="nav-link" id="pills-radcheck-tab"
                                                            data-bs-toggle="pill" href="#pills-radcheck" role="tab"
                                                            aria-controls="pills-radcheck"
                                                            aria-selected="false">Radio/Checkbox</a></li>
                                                    <li class="nav-item"><a class="nav-link" id="pills-select-tab"
                                                            data-bs-toggle="pill" href="#pills-select" role="tab"
                                                            aria-controls="pills-select" aria-selected="false">Select</a>
                                                    </li>
                                                    <li class="nav-item"><a class="nav-link" id="pills-button-tab"
                                                            data-bs-toggle="pill" href="#pills-button" role="tab"
                                                            aria-controls="pills-button" aria-selected="false">Buttons</a>
                                                    </li>
                                                </ul>
                                            </div>
                                            <div>
                                                <nav class="navbar navbar-expand-md p-0">
                                                    <form class="form-inline" @submit.prevent="">
                                                        <div class="me-2">
                                                            <select class="btn form-control b-light" id="n-columns"
                                                                @change="change($event)">
                                                                <option value="1">1 Column</option>
                                                                <option value="2">2 Columns</option>
                                                            </select>
                                                        </div>
                                                        <button class="btn btn-primary" data-bs-toggle="modal"
                                                            data-bs-target="#exampleModalCenter">Copy HTML</button>
                                                    </form>
                                                </nav>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-xl-6">
                                        <div class="tab-content" id="pills-tabContent">
                                            <inputField2 />
                                            <radioField2 />
                                            <selectField2 />
                                            <buttonField2 />
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-xl-6 lg-mt">
                                        <!-- Form builder column wise start-->
                                        <div class="drag-bx card-body">
                                            <div class="text-muted empty-form text-center">
                                                <h6>Drag & Drop elements to build form.</h6>
                                            </div>
                                            <div class="form-body row form-builder-2">
                                                <div class="droppable sortable"
                                                    :class="show == 2 ? 'col-md-6' : 'col-md-12'">
                                                    <draggable :list="lista" style="min-height: 100px"
                                                        group="universalGroup" id="formhtml"></draggable>
                                                </div>
                                                <div class="col-md-6 droppable sortable"
                                                    :style="{ display: show == 2 ? '' : 'none' }">
                                                    <draggable :list="lista" style="min-height: 100px"
                                                        group="universalGroup" id="formhtml"></draggable>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="modal" id="exampleModalCenter" tabindex="-1" aria-hidden="true">
        <emptyForm />
    </div>
</template>
<script>
import { VueDraggableNext } from 'vue-draggable-next'
import inputField2 from "@/components/builder/form/inputField2.vue"
import radioField2 from "@/components/builder/form/radioField2.vue"
import selectField2 from "@/components/builder/form/selectField2.vue"
import buttonField2 from "@/components/builder/form/buttonField2.vue"
import emptyForm from "@/components/builder/form/emptyForm.vue"
import { list } from '@/data/draggable'
export default {
    data() {
        return {
            display: false, show: 1, text: '', lista: list
        }
    },
    components: {
        draggable: VueDraggableNext, inputField2, radioField2, selectField2, buttonField2, emptyForm
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
