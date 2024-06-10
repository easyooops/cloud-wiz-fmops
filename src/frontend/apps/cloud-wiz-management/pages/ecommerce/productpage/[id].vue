<template>
  <Breadcrumbs main="Ecommerce" title="Product Page" />

  <div class="container-fluid">
    <div>
      <div class="row product-page-main p-0">
        <productSwiper />
        <peoductDetails />
        <collectionFilter />
      </div>
    </div>
    <div class="card">
      <div class="row product-page-main">
        <ProductExtraDetails />
      </div>
    </div>
  </div>
</template>

<script>
import productSwiper from "@/components/ecommerce/productpage/productSwiper.vue"
import peoductDetails from "@/components/ecommerce/productpage/peoductDetails.vue"
import collectionFilter from "@/components/ecommerce/productpage/collectionFilter.vue"
import ProductExtraDetails from "@/components/ecommerce/productpage/ProductExtraDetails.vue"
export default {
  name: "productPage",
  components: {
    productSwiper, peoductDetails, collectionFilter, ProductExtraDetails
  },
}
</script>