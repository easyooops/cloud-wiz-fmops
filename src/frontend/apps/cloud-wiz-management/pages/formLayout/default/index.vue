<template>
  <Breadcrumbs title="Default Form" main="Form Layout" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12 col-xl-6">
        <div class="row">
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header">
                <h3>Default Form Layout</h3><span>Using the <a href="javascript:void(0)">card</a> component, you can
                  extend the default collapse behavior to create an accordion.</span>
              </div>
              <div class="card-body">
                <form class="theme-form">
                  <div class="mb-3">
                    <label class="col-form-label pt-0" for="exampleInputEmail1">Email address</label>
                    <input class="form-control" id="exampleInputEmail1" type="email" aria-describedby="emailHelp"
                      placeholder="Enter email"><small class="form-text text-muted" id="emailHelp">We'll never share your
                      email with anyone else.</small>
                  </div>
                  <div class="mb-3">
                    <label class="col-form-label pt-0" for="exampleInputPassword1">Password</label>
                    <input class="form-control" id="exampleInputPassword1" type="password" placeholder="Password">
                  </div>
                  <div class="checkbox p-0">
                    <input id="dafault-checkbox" type="checkbox">
                    <label class="mb-0" for="dafault-checkbox">Remember my preference</label>
                  </div>
                </form>
              </div>
              <div class="card-footer text-end">
                <button class="btn btn-primary me-2">Submit</button>
                <button class="btn btn-secondary">Cancel</button>
              </div>
            </div>
          </div>
          <horizontalForm />
        </div>
      </div>
      <default1Form />
    </div>
  </div>
</template>
<script>
import default1Form from '@/components/formLayout/default/default1Form.vue'
import horizontalForm from '@/components/formLayout/default/horizontalForm.vue';
export default {
  components: {
    default1Form,
    horizontalForm
  }
}
</script>