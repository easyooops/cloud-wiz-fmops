<template>
    <div class="tab-pane active" id="input">
        <draggable @end="finish()" :group="{ name: 'universalGroup', pull: 'clone', put: false }">
            <div class="component" id="text">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="textinput">Text Input</label>
                    <div class="col-lg-12">
                        <input name="textinput" type="text" placeholder="placeholder"
                            class="form-control btn-square input-md">
                        <p class="help-block">help</p>
                    </div>
                </div>
            </div>
            <div class="component" id="password">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start">Password Input</label>
                    <div class="col-lg-12">
                        <input id="passwordinput" name="passwordinput" type="password" placeholder="placeholder"
                            class="form-control btn-square input-md">
                        <span class="help-block">help</span>
                    </div>
                </div>
            </div>
            <div class="component" id="search">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="searchinput">Search Input</label>
                    <div class="col-lg-12">
                        <input id="searchinput" name="searchinput" type="search" placeholder="placeholder"
                            class="form-control btn-square input-md">
                        <p class="help-block">help</p>
                    </div>
                </div>
            </div>
            <div class="component" id="pre">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="prependedtext">Prepended Text</label>
                    <div class="col-lg-12">
                        <div class="input-group">
                            <span class="input-group-text btn btn-primary">prepend</span>
                            <input id="prependedtext" name="prependedtext" class="form-control btn-square"
                                placeholder="placeholder" type="text">
                        </div>
                        <p class="help-block">help</p>
                    </div>
                </div>
            </div>
            <div class="component" id="ape">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="appendedtext">Appended Text</label>
                    <div class="col-lg-12">
                        <div class="input-group">
                            <input id="appendedtext" name="appendedtext" class="form-control btn-square"
                                placeholder="placeholder" type="text">
                            <span class="input-group-text btn btn-primary btn-right">append</span>
                        </div>
                        <p class="help-block">help</p>
                    </div>
                </div>
            </div>
            <div class="component" id="pcheck">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="prependedcheckbox">Prepended Checkbox</label>
                    <div class="col-lg-12">
                        <div class="input-group">
                            <span class="input-group-text">
                                <input type="checkbox">
                            </span>
                            <input id="prependedcheckbox" name="prependedcheckbox" class="form-control btn-square"
                                type="text" placeholder="placeholder">
                        </div>
                        <p class="help-block">help</p>
                    </div>
                </div>
            </div>
            <div class="component" id="acheck">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="appendedcheckbox">Appended Checkbox</label>
                    <div class="col-lg-12">
                        <div class="input-group">
                            <input id="appendedcheckbox" name="appendedcheckbox" class="form-control btn-square" type="text"
                                placeholder="placeholder">
                            <span class="input-group-text checkbox-radius">
                                <input type="checkbox">
                            </span>
                        </div>
                    </div>
                    <p class="help-block">help</p>
                </div>
            </div>
            <div class="component" id="button">
                <div class="mb-3 row">
                    <label class="col-lg-12 form-label text-lg-start" for="buttondropdown">Button Drop Down</label>
                    <div class="col-lg-12">
                        <div class="input-group">
                            <input id="buttondropdown" name="buttondropdown" class="form-control btn-square"
                                placeholder="placeholder" type="text">
                            <div class="input-group-text p-0">
                                <button type="button" class="btn btn-primary dropdown-toggle btn-square"
                                    data-toggle="dropdown">
                                    Action
                                    <span class="caret"></span>
                                </button>
                                <ul class="dropdown-menu pull-right">
                                    <li><a href="#" class="dropdown-item">Option one</a></li>
                                    <li><a href="#" class="dropdown-item">Option two</a></li>
                                    <li><a href="#" class="dropdown-item">Option three</a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="component" id="area">
                <div class="mb-3 row mb-0">
                    <label class="col-lg-12 form-label text-lg-start" for="textarea">Text Area</label>
                    <div class="col-lg-12">
                        <textarea class="form-control btn-square" id="textarea" name="textarea">default text</textarea>
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
            text: '',
            lista: []
        }
    },
    components: {
        draggable: VueDraggableNext,
    },
    methods: {
        finish() {
            if (document.getElementById('formhtml') === null) {
                this.text = ''
            }
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