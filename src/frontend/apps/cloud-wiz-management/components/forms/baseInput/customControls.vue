<template>
    <div class="text-start">
        <div class="card">
          <div class="card-header">
            <h3>Custom controls</h3>
          </div>
                  <form class="form theme-form">
                    <div class="card-body">
                      <div class="row">
                        <div class="col">
                          <div class="mb-3 row">
                            <label class="col-sm-3 col-form-label">Upload File</label>
                            <div class="col-sm-9">
                              <input class="form-control" type="file">
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="row">
                        <div class="col">
                          <div class="row">
                            <label class="col-sm-3 col-form-label">Custom select</label>
                            <div class="col-sm-9">
                              <select class="custom-select form-select">
                                <option selected="">Open this select menu</option>
                                <option value="1">One</option>
                                <option value="2">Two</option>
                                <option value="3">Three</option>
                              </select>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="card-footer text-end">
                      <button class="btn btn-primary m-r-10" type="submit">Submit</button>
                      <input class="btn btn-light" type="reset" value="Cancel">
                    </div>
                  </form>
                </div>
    </div>
</template>