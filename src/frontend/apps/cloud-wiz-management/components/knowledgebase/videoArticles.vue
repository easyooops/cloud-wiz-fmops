<template>
  <div class="col-xl-4 col-md-6">
    <div class="row">
      <div class="col-sm-12">
        <px-card :actions="false">
          <template v-slot:with-padding>
            <div class="media">
              <vue-feather type="file-text" class="m-r-30"></vue-feather>
              <div class="media-body">
                <h6 class="f-w-600">Donec pede justo</h6>
                <p>
                  Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                </p>
              </div>
            </div>
          </template>
        </px-card>
      </div>
      <div class="col-sm-12">
        <px-card :actions="false">
          <template v-slot:with-padding>
            <div class="media">
              <vue-feather type="file-text" class="m-r-30"></vue-feather>
              <div class="media-body">
                <h6 class="f-w-600">Nam quam nunc</h6>
                <p>
                  Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                </p>
              </div>
            </div>
          </template>
        </px-card>
      </div>
      <div class="col-sm-12">
        <px-card :actions="false">
          <template v-slot:with-padding>
            <div class="media">
              <vue-feather type="file-text" class="m-r-30"></vue-feather>
              <div class="media-body">
                <h6 class="f-w-600">Using Video</h6>
                <p>
                  Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                </p>
              </div>
            </div>
          </template>
        </px-card>
      </div>
    </div>
  </div>
  <video2Articles />
</template>
<script>
import { mapState } from 'pinia';
import pxcard from '../Pxcard.vue'
import { useCommonStore } from '~~/store/common';
import video2Articles from "./video2Articles.vue"
export default {
  components: {
    'px-card': pxcard, video2Articles
  },
  data() {
    return {};
  },
  computed: {
    ...mapState(useCommonStore, {
      knowledgebasedata: 'knowledgebasedata',
    }),
  },
};
</script>