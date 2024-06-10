<template>
  <div>
    <Breadcrumbs main title="Knowledge Base" />

    <div class="container-fluid knowledgebase-page">
      <div class="row">
        <knowledgeBase />
        <browseArticles />
        <featured />
        <latestArticles />
      </div>
    </div>
  </div>
</template>
  
<script>
import { mapState } from 'pinia';
import pxcard from '@/components/Pxcard.vue'
import { useCommonStore } from '~~/store/common'
import knowledgeBase from "@/components/knowledgebase/knowledgeBase.vue"
import browseArticles from "@/components/knowledgebase/browseArticles.vue"
import featured from "@/components/knowledgebase/featuredPage.vue"
import latestArticles from "@/components/knowledgebase/latestArticles.vue"
export default {
  components: {
    'px-card': pxcard, knowledgeBase, browseArticles, featured, latestArticles
  },
  data() {
    return {};
  },
  computed: {
    ...mapState(useCommonStore, {
      // knowledgebasedata: (state) => state.common.knowledgebasedata,
      knowledgebasedata: 'knowledgebasedata'
    }),
  },
};
</script>
  
<style>
.search-form.search-knowledge .form-group {
  position: relative;
}

.search-form.search-knowledge .form-group:after {
  position: absolute;
  content: "\F002";
  font-family: FontAwesome;
  top: 10px;
  left: 30px;
}
</style>