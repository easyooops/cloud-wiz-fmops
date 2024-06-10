<template>
    <li><a  data-bs-toggle="modal" data-bs-target="#exampleModal" ><vue-feather type="edit-2"></vue-feather></a>   </li>  
        
          <div class="modal fade modal-bookmark" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title" id="exampleModalLabel">Edit Bookmark</h3>
                  <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close">                                                 </button>
                </div>
                <div class="modal-body">
                  <form class="form-bookmark needs-validation" id="bookmark-form" novalidate>
                    <div class="form-row">
                      <div class="form-group col-md-12">
                        <label for="bm-weburl">Web Url</label>
                        <input class="form-control" id="bm-weburl" type="text" required autocomplete="off" value="http://admin.pixelstrap.com/endless/ltr/landing-page.html">
                      </div>
                      <div class="form-group col-md-12">
                        <label for="bm-title">Title</label>
                        <input class="form-control" id="bm-title" type="text" required autocomplete="off" value="Admin Template">
                      </div>
                      <div class="form-group col-md-12">
                        <label>Description</label>
                        <textarea class="form-control" id="bm-desc" required autocomplete="off">Endless is beautifully crafted, clean and modern designed admin theme with 6 different demos and light - dark versions.</textarea>
                      </div>
                      <div class="row">
                        <div class="form-group col mb-0">
                          <label>Group</label>
                          <select class="js-example-basic-single" id="bm-group">
                            <option value="bookmark">My Bookmarks</option>
                          </select>
                        </div>
                        <div class="form-group col mb-0">
                          <label>Collection</label>
                          <select class="js-example-disabled-results" id="bm-collection">
                            <option value="general">General</option>
                            <option value="fs">fs</option>
                          </select>
                        </div>
                      </div>
                    </div>
                    <input id="index_var" type="hidden" value="6">
                    <button class="btn btn-secondary" id="Bookmark" onclick="submitBookMark()" type="submit">Save</button>
                    <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel          </button>
                  </form>
                </div>
              </div>
            </div>
          </div>
</template>
