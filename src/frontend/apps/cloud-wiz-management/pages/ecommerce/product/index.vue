<template>
  <Breadcrumbs main="Ecommerce" title="Product" />
  <topPage />
</template>

<script>
import topPage from '@/components/ecommerce/product/toppage.vue'

export default {
  name: 'indexProduct',
  components: {
    topPage
  }
}
</script>
