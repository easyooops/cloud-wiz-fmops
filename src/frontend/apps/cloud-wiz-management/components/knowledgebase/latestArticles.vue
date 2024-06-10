<template>
  <div class="col-lg-12">
    <div class="header-faq">
      <h5 class="mb-0">Latest articles and videos</h5>
    </div>
    <div class="row">
      <div class="col-xl-4 col-md-6">
        <div class="row">
          <div class="col-sm-12">
            <px-card :actions="false">
              <template v-slot:with-padding>
                <div class="media">
                  <vue-feather type="codepen" class="m-r-30"></vue-feather>
                  <div class="media-body">
                    <h6 class="f-w-600">Using Video</h6>
                    <p>
                      Cras dapibus. Vivamus elementum semper nisi. Aenean
                      vulputate eleifend tellus.
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
                  <vue-feather type="codepen" class="m-r-30"></vue-feather>
                  <div class="media-body">
                    <h6 class="f-w-600">Vel illum qu</h6>
                    <p>
                      Cras dapibus. Vivamus elementum semper nisi. Aenean
                      vulputate eleifend tellus.
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
                  <vue-feather type="codepen" class="m-r-30"></vue-feather>
                  <div class="media-body">
                    <h6 class="f-w-600">Cum sociis natoqu</h6>
                    <p>
                      Cras dapibus. Vivamus elementum semper nisi. Aenean
                      vulputate eleifend tellus.
                    </p>
                  </div>
                </div>
              </template>
            </px-card>
          </div>
        </div>
      </div>

      <videoArticles />
    </div>
  </div>
</template>
<script>

import { mapState } from 'pinia';
import pxcard from '../Pxcard.vue'
import videoArticles from "./videoArticles.vue"
import { useCommonStore } from '~~/store/common';
export default {
  components: {
    'px-card': pxcard, videoArticles
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