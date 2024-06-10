<template>
  <Breadcrumbs main="Ecommerce" title="Paymen Details" />

  <div class="container-fluid credit-card">
    <div class="row">

      <CreditCard />

      <DebitCard />

      <COD />

      <EMI />

      <NetBanking />

    </div>
  </div>
</template>
<script>
import CreditCard from '@/components/ecommerce/payment/CreditCard.vue';
import DebitCard from '@/components/ecommerce/payment/DebitCard.vue';
import COD from '@/components/ecommerce/payment/COD.vue';
import EMI from '@/components/ecommerce/payment/EMI.vue';
import NetBanking from '@/components/ecommerce/payment/NetBanking.vue';
export default {
  name: 'paymentDetails',
  components: {
    CreditCard,
    DebitCard,
    COD,
    EMI,
    NetBanking
  }
}
</script>