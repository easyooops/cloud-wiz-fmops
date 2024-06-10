<template>
  <Breadcrumbs title="Add Post" main="Blog" />

  <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5>Post Edit</h5>
            </div>
            <div class="card-body add-post">
              <form class="row needs-validation" novalidate>
                <div class="col-sm-12">
                  <div class="form-group mb-3">
                    <label for="validationCustom01">Title:</label>
                    <input class="form-control" id="validationCustom01" type="text" placeholder="Post Title" required>
                    <div class="valid-feedback">Looks good!</div>
                  </div>
                  <div class="form-group mb-3">
                    <label>Type:</label>
                    <div class="m-checkbox-inline">
                      <label class="f-w-500" for="edo-ani">
                        <input class="radio_animated" id="edo-ani" type="radio" name="rdo-ani" checked>Text
                      </label>
                      <label class="f-w-500" for="edo-ani1">
                        <input class="radio_animated" id="edo-ani1" type="radio" name="rdo-ani">Image
                      </label>
                      <label class="f-w-500" for="edo-ani2">
                        <input class="radio_animated" id="edo-ani2" type="radio" name="rdo-ani" checked>Audio
                      </label>
                      <label class="f-w-500" for="edo-ani3">
                        <input class="radio_animated" id="edo-ani3" type="radio" name="rdo-ani">Video
                      </label>
                    </div>
                  </div>
                  <div class="form-group mb-3">
                    <label class="d-block">Category:</label>
                    <select class=" col-sm-12 form-control" >
                      <option value="">Select from list</option>
                      <option value="AL">Lifestyle</option>
                      <option value="WY">Travel</option>
                    </select>
                  </div>
                  <div class="email-wrapper mb-3">
                    <div class="theme-form">
                      <div class="form-group">
                        <label>Content:</label>
                        <ckeditor :editor="editor" height="50px" v-model="editorData" :config="editorConfig"></ckeditor>
                      </div>
                    </div>
                  </div>
                </div>
              </form>
              <DropZone class="text-center" :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" :multipleUpload="true" :parallelUpload="2" />
              <div class="btn-showcase">
                <button class="btn btn-primary" type="submit">Post</button>
                <input class="btn btn-light" type="reset" value="Discard">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
import CKEditor from '@ckeditor/ckeditor5-vue';
import ClassicEditor from '@ckeditor/ckeditor5-build-classic';
export default {
  components:{
     
          ckeditor: CKEditor.component  
  },
  data(){
    return {
      type: 'inbox',
      editor: ClassicEditor,
      editorData: '',
      editorConfig: {
        config:{ height: '300px' }
      },
      menutoogle:false,
    };
  },
}
</script>
<style>
.ck-content { height:200px; }
</style>