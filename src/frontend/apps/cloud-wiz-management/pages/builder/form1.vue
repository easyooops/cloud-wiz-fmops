<template>
    <div class="form-builder">
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-12">
                    <div class="card">
                        <div class="card-header">
                            <h5>Drag & Drop components</h5><span>Copy the html code from View HTML tab </span>
                        </div>
                        <div class="card-body">
                            <div class="row clearfix form-builder">
                                <div class="col-lg-12 col-xl-6">
                                    <div class="form-builder-header-1">
                                        <ul class="nav nav-primary" id="formtabs">
                                            <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5 active"
                                                    data-bs-target="#input">Input</a></li>
                                            <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5"
                                                    data-bs-target="#radio">Radios / Checkboxes</a></li>
                                            <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5"
                                                    data-bs-target="#select">Select</a></li>
                                            <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5"
                                                    data-bs-target="#buttons">Buttons</a></li>
                                            <li class="nav-item"><a data-bs-toggle="tab" class="nav-link m-r-5"
                                                    data-bs-target="#view">View HTML</a></li>
                                        </ul>
                                    </div>
                                    <form class="form-horizontal theme-form" id="components">
                                        <fieldset>
                                            <div class="tab-content">
                                                <inputField />
                                                <radioField />
                                                <selectField />
                                                <buttonField />
                                                <div class="tab-pane" id="view">
                                                    <h6>Rendered source of your form:</h6>

                                                    <textarea id="render" class="render p-3" spellcheck="false"
                                                        :value="text"></textarea>
                                                </div>
                                            </div>
                                        </fieldset>
                                    </form>
                                </div>
                                <div class="col-lg-12 col-xl-6 lg-mt-col">
                                    <div class="form-builder-header-1">
                                        <h6 class="mt-0">Drag Elements Here</h6>
                                    </div>
                                    <form class="form-horizontal drag-box" id="target">
                                        <fieldset>
                                            <div class="component" data-title="Form Name" data-trigger="manual"
                                                data-html="true">
                                                <h6 class="m-t-10">Form Name</h6>
                                                <hr>
                                                <draggable :list="lista" style="min-height: 100px" group="universalGroup"
                                                    id="formhtml"></draggable>
                                            </div>
                                        </fieldset>
                                    </form>
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
import { VueDraggableNext } from 'vue-draggable-next'
import radioField from "@/components/builder/form/radioField.vue"
import inputField from "@/components/builder/form/inputField.vue"
import selectField from "@/components/builder/form/selectField.vue"
import buttonField from "@/components/builder/form/buttonField.vue"
export default {
    inject: ['list'],
    data() {
        return {
            text: '',
            lista: []
        }
    },
    components: {
        draggable: VueDraggableNext, radioField, inputField, selectField, buttonField
    },
    methods: {
        finish() {
        },
    },
    mounted() {
        this.lista = this.list
    }
}
</script>