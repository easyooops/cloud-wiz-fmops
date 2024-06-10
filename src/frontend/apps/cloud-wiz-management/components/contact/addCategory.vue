<template>
    <li>
        <button class="btn btn-category" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal1"><span class="title"> + Add Category</span></button>
        <div class="modal fade" id="exampleModal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel1" aria-hidden="true">
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title" id="exampleModalLabel1">Add Category</h3>
                  <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <form class="form-bookmark">
                    <div class="row g-2">
                      <div class="mb-3 col-md-12">
                        <input class="form-control" type="text" required placeholder="Enter category name" autocomplete="off">
                      </div>
                    </div>
                    <button class="btn btn-secondary" type="button">Save</button>
                    <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel        </button>
                  </form>
                </div>
              </div>
            </div>
          </div>  
    </li>
</template>
