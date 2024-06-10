<template>
    <div class="col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h3>Custom checkbox</h3>
                  </div>
                  <div class="card-body">
                    <div class="row">
                      <div class="col-sm-12">
                        <h5>Custom checkbox</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15">
                          <div class="checkbox ">
                            <input id="checkbox1" type="checkbox">
                            <label for="checkbox1">Default</label>
                          </div>
                          <div class="checkbox">
                            <input id="checkbox2" type="checkbox" disabled="">
                            <label for="checkbox2">Disabled</label>
                          </div>
                          <div class="checkbox">
                            <input id="checkbox3" type="checkbox" >
                            <label for="checkbox3">Checked</label>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-12">
                        <h5>Checkbox states</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15">
                          <div class="checkbox checkbox-primary">
                            <input id="checkbox-primary-1" type="checkbox">
                            <label for="checkbox-primary-1">primary state</label>
                          </div>
                          <div class="checkbox checkbox-secondary">
                            <input id="checkbox-dark" type="checkbox" disabled="">
                            <label for="checkbox-dark">Brand state</label>
                          </div>
                          <div class="checkbox checkbox-success">
                            <input id="checkbox-primary" type="checkbox">
                            <label for="checkbox-primary">success state</label>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-12">
                        <h5>Inline checkbox</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15 m-checkbox-inline mb-0">
                          <div class="checkbox checkbox-dark">
                            <input id="inline-1" type="checkbox">
                            <label for="inline-1">Option<span class="digits"> 1</span></label>
                          </div>
                          <div class="checkbox checkbox-dark">
                            <input id="inline-2" type="checkbox">
                            <label for="inline-2">Option<span class="digits"> 2</span></label>
                          </div>
                          <div class="checkbox checkbox-dark">
                            <input id="inline-3" type="checkbox">
                            <label for="inline-3">Option<span class="digits"> 3</span></label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
</template>