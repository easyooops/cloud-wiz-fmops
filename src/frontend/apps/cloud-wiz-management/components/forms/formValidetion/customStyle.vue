<template>
    <div class="card">
        <div class="card-header">
            <h3>Custom styles</h3><span>For custom Bootstrap form validation messages, you’ll need to add the <code
                    class="text-danger">novalidate</code> boolean attribute to your <code
                    class="text-danger">&lt;form&gt;</code>. This disables the browser default feedback tooltips, but still
                provides access to the form validation APIs in JavaScript. Try to submit the form below; our JavaScript will
                intercept the submit button and relay feedback to you.</span><span>When attempting to submit, you’ll see the
                <code class="text-danger">:invalid </code> and <code class="text-danger">:valid </code> styles applied to
                your form controls.</span>
        </div>
        <div class="card-body">
            <form class="needs-validation" novalidate="" @submit.prevent="onCustomStyleSubmit">
                <div class="row g-3">
                    <div class="col-md-4">
                        <label class="form-label">First name</label>
                        <input type="text" class="form-control"
                            v-bind:class="formSubmitted ? firstError ? 'is-invalid' : 'is-valid' : ''" id="name"
                            placeholder="Your name" v-model="firstname">
                        <div class="valid-feedback" id="feedback-1" v-if="errors[0]">{{ errors[0].message }}</div>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label" for="validationCustom02">Last name</label>
                        <input class="form-control" type="text"
                            v-bind:class="formSubmitted ? lastError ? 'is-invalid' : 'is-valid' : ''" id="name"
                            placeholder="Your name" v-model="lastname">
                        <div class="valid-feedback" id="feedback-1" v-if="errors[0]">{{ errors[0].message }}</div>
                    </div>
                    <div class="col-md-4 mb-3">
                        <label class="form-label" for="validationCustomUsername">Username</label>
                        <div class="input-group"><span class="input-group-text" id="inputGroupPrepend">@</span>
                            <input class="form-control" id="validationCustomUsername" type="text"
                                v-bind:class="formSubmitted ? userError ? 'is-invalid' : 'is-valid' : ''"
                                placeholder="Username" v-model="username">
                            <div class="invalid-feedback" v-if="errors[1]">{{ errors[1].message1 }}</div>
                        </div>
                    </div>
                </div>
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label" for="validationCustom03">City</label>
                        <input class="form-control" id="validationCustom03" type="text"
                            v-bind:class="formSubmitted ? cityError ? 'is-invalid' : 'is-valid' : ''" placeholder="City"
                            required="" v-model="city">
                        <div class="invalid-feedback" v-if="errors[1]">{{ errors[1].message2 }}</div>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label" for="validationCustom04">State</label>
                        <select class="form-select" id="validationCustom04"
                            v-bind:class="formSubmitted ? stateError ? 'is-invalid' : 'is-valid' : ''" v-model="state"
                            required="">
                            <option selected="" disabled="" value="">Choose...</option>
                            <option>gujarat</option>
                            <option>UP</option>
                            <option>MP</option>
                            <option>PUNJAB</option>
                        </select>
                        <div class="invalid-feedback" v-if="errors[1]">{{ errors[1].message3 }}</div>
                    </div>
                    <div class="col-md-3 mb-3">
                        <label class="form-label" for="validationCustom05">Zip</label>
                        <input class="form-control" id="validationCustom05" type="text"
                            v-bind:class="formSubmitted ? zipError ? 'is-invalid' : 'is-valid' : ''" v-model="zip"
                            placeholder="Zip" required="">
                        <div class="invalid-feedback" v-if="errors[1]">{{ errors[1].message4 }}</div>
                    </div>
                </div>
                <div class="mb-3">
                    <div class="form-check">
                        <div class="checkbox p-0">
                            <input class="form-check-input" id="invalidCheck" type="checkbox" required="">
                            <label class="form-check-label" for="invalidCheck">Agree to terms and conditions</label>
                    </div>
                    <div class="invalid-feedback">You must agree before submitting.</div>
                </div>
            </div>
            <button class="btn btn-primary">Submit form</button>
        </form>
    </div>
</div></template>

<script>
import formValidation from "@/mixin/commen/formValidation"
export default {
    mixins: [formValidation]
}
</script>
