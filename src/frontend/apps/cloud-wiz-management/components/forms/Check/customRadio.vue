<template>
         <div class="col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h3>Custom Radio</h3>
                  </div>
                  <div class="card-body">
                    <div class="row">
                      <div class="col-sm-12">
                        <h5>Custom Radio</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15 custom-radio-ml">
                          <div class="radio radio-primary">
                            <input id="radio1" type="radio" name="radio1" value="option1">
                            <label for="radio1">Option<span class="digits"> 1</span></label>
                          </div>
                          <div class="radio radio-primary">
                            <input id="radio3" type="radio" name="radio1" value="option1" disabled="">
                            <label for="radio3">Disabled</label>
                          </div>
                          <div class="radio radio-primary">
                            <input id="radio4" type="radio" name="radio1" value="option1" checked="">
                            <label for="radio4">Checked</label>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-12">
                        <h5>Radio states</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15 custom-radio-ml">
                          <div class="radio radio-primary">
                            <input id="radio11" type="radio" name="radio1" value="option1">
                            <label for="radio11">Option<span class="digits"> 1</span></label>
                          </div>
                          <div class="radio radio-secondary">
                            <input id="radio22" type="radio" name="radio1" value="option1">
                            <label for="radio22">Option<span class="digits"> 2</span></label>
                          </div>
                          <div class="radio radio-success">
                            <input id="radio55" type="radio" name="radio1" value="option1">
                            <label for="radio55">Option<span class="digits"> 3</span></label>
                          </div>
                          <div class="radio radio-info">
                            <input id="radio33" type="radio" name="radio1" value="option1" disabled="">
                            <label for="radio33">Option<span class="digits"> 4</span></label>
                          </div>
                          <div class="radio radio-warning">
                            <input id="radio44" type="radio" name="radio1" value="option1">
                            <label for="radio44">Option<span class="digits"> 5</span></label>
                          </div>
                          <div class="radio radio-danger">
                            <input id="radio66" type="radio" name="radio1" value="option1" checked="">
                            <label for="radio66">Option<span class="digits"> 6</span></label>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-12">
                        <h5>Inline checkbox</h5>
                      </div>
                      <div class="col">
                        <div class="form-group m-t-15 m-checkbox-inline mb-0 custom-radio-ml">
                          <div class="radio radio-primary">
                            <input id="radioinline1" type="radio" name="radio1" value="option1">
                            <label class="mb-0" for="radioinline1">Option<span class="digits"> 1</span></label>
                          </div>
                          <div class="radio radio-primary">
                            <input id="radioinline2" type="radio" name="radio1" value="option1">
                            <label class="mb-0" for="radioinline2">Option<span class="digits"> 2</span></label>
                          </div>
                          <div class="radio radio-primary">
                            <input id="radioinline3" type="radio" name="radio1" value="option1">
                            <label class="mb-0" for="radioinline3">Option<span class="digits"> 3</span></label>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
</template>