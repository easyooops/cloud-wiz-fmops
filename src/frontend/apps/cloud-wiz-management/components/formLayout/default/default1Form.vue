<template>
    <div class="col-sm-12 col-xl-6">
        <div class="row">
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header">
                <h3>Mega form</h3>
              </div>
              <div class="card-body">
                <form class="theme-form mega-form">
                  <h4>Account Information</h4>
                  <div class="mb-3">
                    <label class="col-form-label">Your Name</label>
                    <input class="form-control" type="text" placeholder="your Name">
                  </div>
                  <div class="mb-3">
                    <label class="col-form-label">Email Address</label>
                    <input class="form-control" type="email" placeholder="Enter email">
                  </div>
                  <div class="mb-3">
                    <label class="col-form-label">Contact Number</label>
                    <input class="form-control" type="Number" placeholder="Enter contact number">
                  </div>
                  <hr class="mt-4 mb-4">
                  <h4>Company Information</h4>
                  <div class="mb-3">
                    <label class="col-form-label">Company Name</label>
                    <input class="form-control" type="text" placeholder="Company Name">
                  </div>
                  <div class="mb-3">
                    <label class="col-form-label">Website</label>
                    <input class="form-control" type="text" placeholder="Website">
                  </div>
                </form>
                <hr class="mt-4 mb-4">
                <h4 class="pb-3 mb-0">Billing Information</h4>
                <form class="form-space theme-form row">
                  <div class="col-auto">
                    <input class="form-control" type="text" placeholder="Name On Card">
                  </div>
                  <div class="col-auto">
                    <input class="form-control" type="number" name="cardNumber" placeholder="Card Number">
                  </div>
                  <div class="col-auto">
                    <input class="form-control" type="text" name="inputPassword" placeholder="Zip Code">
                  </div>
                </form>
              </div>
              <div class="card-footer text-end">
                <button class="btn btn-primary me-2">Submit</button>
                <button class="btn btn-secondary">Cancel</button>
              </div>
            </div>
          </div>
          <div class="col-xl-12">
            <div class="card">
              <div class="card-header">
                <h3>Inline Form</h3><span>Use<code>.form-inline</code>class in the form to style with inline fields.</span>
              </div>
              <div class="card-body">
                <h4>Inline Form with Label</h4>
                <form class="row theme-form mt-3">
                  <div class="col-xxl-4 mb-3 d-flex">
                    <label class="col-form-label pe-2" for="inputInlineUsername">Username</label>
                    <input class="form-control" id="inputInlineUsername" type="text" name="inputUsername" placeholder="Username" autocomplete="off">
                  </div>
                  <div class="col-xxl-4 mb-3 d-flex">
                    <label class="col-form-label pe-2" for="inputInlinePassword">Password</label>
                    <input class="form-control" id="inputInlinePassword" type="password" name="inputPassword" placeholder="Password" autocomplete="off">
                  </div>
                  <div class="col-xxl-4 mb-3 d-flex">
                    <button class="btn btn-primary">Login</button>
                  </div>
                </form>
                <h4>Inline Form without Label</h4>
                <form class="row row-cols-sm-3 theme-form mt-3 form-bottom">
                  <div class="mb-3 d-flex">
                    <input class="form-control" type="text" name="inputUnlabelUsername" placeholder="Username" autocomplete="off">
                  </div>
                  <div class="mb-3 d-flex">
                    <input class="form-control" id="inputUnlabelPassword" type="password" name="inputPassword" placeholder="Password" autocomplete="off">
                  </div>
                  <div class="mb-3 d-flex">
                    <button class="btn btn-secondary">Login</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
</template>