<template>
  <li class="nav-item">
    <button class="badge-light-primary btn-block btn-mail w-100" type="button" data-bs-toggle="modal"
      data-bs-target="#exampleModal">
      <vue-feather class="me-2" type="bookmark"></vue-feather> New Bookmark
    </button>
    <div class="modal fade modal-bookmark" id="exampleModal" tabindex="-1" role="dialog"
      aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h3 class="modal-title" id="exampleModalLabel">Add Bookmark</h3>
            <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"> </button>
          </div>
          <div class="modal-body">
            <form class="form-bookmark needs-validation" id="bookmark-form" novalidate>
              <div class="form-row">
                <div class="form-group col-md-12">
                  <label for="bm-weburl">Web Url</label>
                  <input class="form-control" id="bm-weburl" type="text" v-model="web" required autocomplete="off">
                </div>
                <div class="form-group col-md-12">
                  <label for="bm-title">Title</label>
                  <input class="form-control" id="bm-title" type="text" v-model="title" required autocomplete="off">
                </div>
                <div class="form-group col-md-12">
                  <label>Description</label>
                  <textarea class="form-control" id="bm-desc" v-model="description" required
                    autocomplete="off"></textarea>
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
              <button class="btn btn-secondary" type="button" @click="submitBookmark()"
                data-bs-dismiss="modal">Save</button>
              <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </li>
</template>
<script>
import { useCommonStore } from '~~/store/common'
export default {
  data() {
    return {
      web: '',
      title: '',
      description: ''
    }
  },
  methods: {
    submitBookmark() {
      let arr =
      {
        fillstar: false,
        website_url: this.web,
        title: this.title,
        desc: this.description,
        image: "lightgallry/05.jpg",
        collection: "General",
        active: false
      }
      useCommonStore().add(arr)
    }
  },
}
</script>

