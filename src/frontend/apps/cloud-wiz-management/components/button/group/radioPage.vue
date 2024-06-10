<template>
  <div class="col-12">
    <div class="card">
      <div class="card-header">
        <h5>Radio button group</h5><span>Add <code>.active</code> for active state and<code>.disabled</code> class or
          <code>disabled="disabled"</code> attribute</span>
      </div>
      <div class="card-body btn-group-showcase">
        <div class="row">
          <div class="col-xxl-4 col-md-6 col-sm-12">
            <div class="btn-radio">
              <div class="btn-group" data-bs-toggle="buttons">
                <div class="btn btn-primary">
                  <div class="radio radio-primary">
                    <input id="radio7" type="radio" name="radio1" value="option1">
                    <label for="radio7">Option 1</label>
                  </div>
                </div>
                <div class="btn btn-primary active">
                  <div class="radio radio-primary">
                    <input id="radio8" type="radio" name="radio1" value="option1" checked>
                    <label for="radio8">Option 2</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xxl-4 col-md-6 col-sm-12">
            <div class="btn-radio">
              <div class="btn-group" data-bs-toggle="buttons">
                <div class="btn btn-secondary">
                  <div class="radio radio-secondary">
                    <input id="radio11" type="radio" name="radio2" value="option1">
                    <label for="radio11">Option 1</label>
                  </div>
                </div>
                <div class="btn btn-secondary active">
                  <div class="radio radio-secondary">
                    <input id="radio12" type="radio" name="radio2" value="option1" checked>
                    <label for="radio12">Option 2</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xxl-4 col-md-6 col-sm-12">
            <div class="btn-radio">
              <div class="btn-group" data-bs-toggle="buttons">
                <div class="btn btn-success">
                  <div class="radio radio-success">
                    <input id="radio13" type="radio" name="radio3" value="option1">
                    <label for="radio13">Option 1</label>
                  </div>
                </div>
                <div class="btn btn-success active">
                  <div class="radio radio-success">
                    <input id="radio14" type="radio" name="radio3" value="option1" checked>
                    <label for="radio14">Option 2</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xxl-4 col-md-6 col-sm-12">
            <div class="btn-radio">
              <div class="btn-group" data-bs-toggle="buttons">
                <div class="btn btn-info">
                  <div class="radio radio-info">
                    <input id="radio15" type="radio" name="radio4" value="option1">
                    <label for="radio15">Option 1</label>
                  </div>
                </div>
                <div class="btn btn-info active">
                  <div class="radio radio-info">
                    <input id="radio16" type="radio" name="radio4" value="option1" checked>
                    <label for="radio16">Option 2</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <radioPage2 />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import radioPage2 from "./radioPage2.vue"
export default {
  components: { radioPage2 }
}
</script>