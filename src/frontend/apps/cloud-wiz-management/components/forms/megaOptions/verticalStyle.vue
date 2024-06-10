<template>
  <div class="col-sm-12 col-xxl-6 box-col-12">
    <div class="card height-equal">
      <div class="card-header">
        <h3>Vertical Style</h3><span>For Create inline megaoption add <code>.mega-vertical</code> class in form tag</span>
      </div>
      <div class="card-body">
        <form class="mega-vertical">
          <div class="row">
            <div class="col-sm-12">
              <p class="mega-title m-b-5">Delivery Option</p>
            </div>
            <div class="col-sm-6">
              <div class="card">
                <div class="d-flex p-20">
                  <div class="form-check radio radio-primary me-3">
                    <input class="form-check-input" id="radio23" type="radio" name="radio1" value="option1">
                    <label class="form-check-label" for="radio23"></label>
                  </div>
                  <div class="flex-grow-1">
                    <h6 class="mt-0 mega-title-badge">COD<span class="badge badge-primary pull-right digits">50 INR</span>
                    </h6>
                    <p>Estimated 10 to 15 Day Shipping ( Duties end tax may be due delivery )</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="card">
                <div class="d-flex p-20">
                  <div class="form-check radio radio-secondary me-3">
                    <input class="form-check-input" id="radio24" type="radio" name="radio1" value="option1">
                    <label class="form-check-label" for="radio24"></label>
                  </div>
                  <div class="flex-grow-1">
                    <h6 class="mt-0 mega-title-badge">Fast <span class="badge badge-secondary pull-right digits">100
                        INR</span></h6>
                    <p>Estimated 10 to 12 Day Shipping ( Duties end tax may be due delivery )</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="card">
                <div class="d-flex p-20">
                  <div class="form-check radio radio-success me-3">
                    <input class="form-check-input" id="radio25" type="radio" name="radio1" value="option1">
                    <label class="form-check-label" for="radio25"></label>
                  </div>
                  <div class="flex-grow-1">
                    <h6 class="mt-0 mega-title-badge">Standard <span class="badge badge-success pull-right digits">80
                        INR</span></h6>
                    <p>Estimated 3 to 5 Day Shipping ( Duties end tax may be due delivery )</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-sm-6">
              <div class="card">
                <div class="d-flex p-20">
                  <div class="form-check radio radio-info me-3">
                    <input class="form-check-input" id="radio5" type="radio" name="radio1" value="option1">
                    <label class="form-check-label" for="radio5"></label>
                  </div>
                  <div class="flex-grow-1">
                    <h6 class="mt-0 mega-title-badge">Local <span class="badge badge-info pull-right digits">Free</span>
                    </h6>
                    <p>Estimated 3 to 5 Day Shipping ( Duties end taxes may be due upon delivery )</p>
                  </div>
                </div>
              </div>
            </div>
            <buyingOption />
          </div>
        </form>
      </div>
      <div class="card-footer text-end">
        <button class="btn btn-primary m-r-15" type="submit">Submit</button>
        <button class="btn btn-light" type="submit">Cancel</button>
      </div>
    </div>
  </div>
</template>
<script>
import buyingOption from "./buyingOption.vue"
export default {
  data() {
    return {
      verticalStyle: 1
    }
  }, components: { buyingOption }
}
</script>