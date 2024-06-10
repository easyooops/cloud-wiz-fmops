<template>
  <div class="text-start">
    <div class="card">
      <div class="card-header">
        <h3>Tooltips</h3><span>If your form layout allows it, you can swap the <code
            class="text-danger">.{valid|invalid}-feedback</code> classes for <code
            class="text-danger">.{valid|invalid}-tooltip</code> classes to display validation feedback in a styled
          tooltip. Be sure to have a parent with <code class="text-danger">position: relative</code> on it for tooltip
          positioning. In the example below, our column classes have this already, but your project may require an
          alternative setup.</span>
      </div>
      <div class="card-body">
        <form class="row g-3 needs-validation" novalidate="" @submit.prevent="onCustomStyleSubmit">
          <div class="col-md-4 position-relative">
            <label class="form-label" for="validationTooltip01">First name</label>
            <input class="form-control" id="validationTooltip01"
              v-bind:class="formSubmitted ? firstError ? 'is-invalid' : 'is-valid' : ''" placeholder="Your name"
              v-model="firstname" type="text" required="">
            <div class="valid-tooltip" v-if="errors[0]" data-bs-toggle="tooltip" title="Looks good!">Looks good!</div>
          </div>
          <div class="col-md-4 position-relative">
            <label class="form-label" for="validationTooltip02">Last name</label>
            <input class="form-control" id="validationTooltip02" type="text"
              v-bind:class="formSubmitted ? lastError ? 'is-invalid' : 'is-valid' : ''" placeholder="Your name"
              v-model="lastname" required="">
            <div class="valid-tooltip" v-if="errors[0]" data-bs-toggle="tooltip" title="Looks good!">Looks good!</div>
          </div>
          <div class="col-md-4 position-relative">
            <label class="form-label" for="validationTooltipUsername">Username</label>
            <div class="input-group has-validation"><span class="input-group-text"
                id="validationTooltipUsernamePrepend">@</span>
              <input class="form-control" id="validationTooltipUsername" type="text"
                aria-describedby="validationTooltipUsernamePrepend"
                v-bind:class="formSubmitted ? userError ? 'is-invalid' : 'is-valid' : ''" placeholder="Username"
                v-model="username" required="">
              <div class="invalid-tooltip" v-if="errors[1]" data-bs-toggle="tooltip">Please choose a unique and valid
                username.</div>
            </div>
          </div>
          <div class="col-md-6 position-relative">
            <label class="form-label" for="validationTooltip03">City</label>
            <input class="form-control" id="validationTooltip03" type="text"
              v-bind:class="formSubmitted ? cityError ? 'is-invalid' : 'is-valid' : ''" placeholder="City" required=""
              v-model="city">
            <div class="invalid-tooltip" v-if="errors[2]" data-bs-toggle="tooltip">Please provide a valid city.</div>
          </div>
          <div class="col-md-3 position-relative">
            <label class="form-label" for="validationTooltip04">State</label>
            <select class="form-select" id="validationTooltip04"
              v-bind:class="formSubmitted ? stateError ? 'is-invalid' : 'is-valid' : ''" v-model="state" required="">
              <option selected="" disabled="" value="">Choose...</option>
              <option>...</option>
            </select>
            <div class="invalid-tooltip" v-if="errors[3]" data-bs-toggle="tooltip">Please select a valid state.</div>
          </div>
          <div class="col-md-3 position-relative">
            <label class="form-label" for="validationTooltip05">Zip</label>
            <input class="form-control" id="validationTooltip05" type="text" required=""
              v-bind:class="formSubmitted ? zipError ? 'is-invalid' : 'is-valid' : ''" v-model="zip" placeholder="Zip">
            <div class="invalid-tooltip" v-if="errors[4]" data-bs-toggle="tooltip">Please provide a valid zip.</div>
          </div>
          <div class="col-12">
            <button class="btn btn-primary">Submit form</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
import formValidation from "@/mixin/commen/formValidation"
export default {
  inject: ['Tooltip'],
  mixins: [formValidation],
  mounted() {
    new this.Tooltip(document.body, {
      selector: "[data-bs-toggle='tooltip']",
    })
  }
}
</script>