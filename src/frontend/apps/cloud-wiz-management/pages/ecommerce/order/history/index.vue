<template>
  <Breadcrumbs main="Ecommerce" title="Recent Orders" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <NewOrders />
        <ShippedOrders />
        <CancelledOrders />
      </div>
      <DatatableOrderHistory />
    </div>
  </div>
</template>
<script>
import { shipped } from '@/data/orderHistory'
import NewOrders from "@/components/ecommerce/order/NewOrders.vue"
import ShippedOrders from "@/components/ecommerce/order/ShippedOrders.vue"
import CancelledOrders from "@/components/ecommerce/order/CancelledOrders.vue"
import DatatableOrderHistory from "@/components/ecommerce/order/DatatableOrderHistory.vue"
export default {
  name: 'orderHistory',
  components: {
    NewOrders, ShippedOrders, CancelledOrders, DatatableOrderHistory
  },

}
</script>