<template>
  <div class="col-12 text-start">
    <div class="knowledgebase-bg">
      <img class="bg-img-cover bg-center img-fluid" src="/images/knowledgebase/bg_1.jpg" alt="looginpage">
    </div>
    <div class="knowledgebase-search">
      <div>
        <h3>How Can I help you?</h3>
        <form class="form-inline" action="#" method="get">
          <div class="form-group w-100 mb-0"><vue-feather type="search"></vue-feather>
            <input class="form-control-plaintext w-100" type="text" placeholder="Type question here" title="">
          </div>
        </form>
      </div>
    </div>
  </div>
  <faq />
</template>
<script>
import faq from "./articlesView.vue"

export default {
  components: {
    faq,
  }
}
</script>