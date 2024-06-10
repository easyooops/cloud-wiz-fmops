<template>
  <Breadcrumbs title="FAQ" />
  <div class="container-fluid">
    <div class="faq-wrap">
      <div class="row">
        <faq />
        <faq1 />
        <featured />
        <articles />
      </div>
    </div>
  </div>
</template>
<script>
import faq from "@/components/faq/faqPage.vue"
import faq1 from "@/components/faq/faq1Page.vue"
import featured from "@/components/faq/featuredPage.vue"
import articles from "@/components/faq/articlesPage.vue"
export default {
  components: {
    faq,
    faq1,
    featured,
    articles
  }
}
</script>