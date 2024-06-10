<template>
  <Breadcrumbs title="Pricing" main="Ecommerce" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>Become member</h5>
          </div>
          <div class="card-body row pricing-block">
            <div class="col-lg-3 col-sm-6" v-for="memberCard in memberCards" :key="memberCard">
              <div class="pricingtable">
                <div class="pricingtable-header">
                  <h3 class="title">{{ memberCard.title }}</h3>
                </div>
                <div class="price-value"><span class="currency">$</span><span class="amount">{{
                  memberCard.price }}</span><span class="duration">/mo</span></div>
                <ul class="pricing-content">
                  <li v-for="contents in memberCard.list " :key="contents">{{ contents.content }}</li>
                </ul>
                <div class="pricingtable-signup"><a class="btn btn-primary btn-lg" href="#">Sign Up</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">
            <h5>Simple Pricing Card</h5>
          </div>
          <div class="card-body pricing-content">
            <div class="row g-sm-4 g-3">
              <div class="col-lg-3 col-sm-6" v-for="simaleCard in simaleCards" :key="simaleCard">
                <div class="card text-center pricing-simple">
                  <div class="card-body">
                    <h3>{{ simaleCard.title }}</h3>
                    <h1>${{ simaleCard.price }}</h1>
                    <h6 class="mb-0">{{ simaleCard.text }}</h6>
                  </div><a class="btn btn-lg btn-primary btn-block" href="#">Purchase</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { pricing1, pricing2 } from '@/data/ecommerce/pricing'
export default {
  name: 'pricingView',
  data() {
    return {
      memberCards: pricing1,
      simaleCards: pricing2
    }
  }
}
</script>
