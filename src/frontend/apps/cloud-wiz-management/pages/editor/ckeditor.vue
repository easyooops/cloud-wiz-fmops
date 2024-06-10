<template>
  <div>
    <Breadcrumbs main="Editor" title="Ck Editor" />
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">cK Editor</h5>
            </div>
            <div class="card-body">
              <ClientOnly>

                <ckeditor :editor="editor" v-model="editorData"></ckeditor>
              </ClientOnly>
            </div>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  inject: ['ClassicEditor'],
  data() {
    return {
      editor: this.ClassicEditor,
      editorData: '<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>',
    };
  }
};
</script>


<style>
.ck-content {
  height: 500px;
}
</style>