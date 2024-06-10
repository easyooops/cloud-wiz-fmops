<template>
  <breadCrumbs title="Checkout" main="Ecommerce" title1="Checkout" />
  <div class="container-fluid">
    <div class="card">
      <div class="card-header">
        <h3>Billing Details</h3>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-xl-6 col-sm-12">
            <form>
              <div class="row">
                <div class="mb-3 col-sm-6">
                  <label for="inputEmail4">First Name</label>
                  <input class="form-control" id="inputEmail" type="email">
                </div>
                <div class="mb-3 col-sm-6">
                  <label for="inputPassword4">Last Name</label>
                  <input class="form-control" id="input" type="text">
                </div>
              </div>
              <div class="row">
                <div class="mb-3 col-sm-6">
                  <label for="phonenumber">Phone</label>
                  <input class="form-control" id="phonenumber" type="number">
                </div>
                <div class="mb-3 col-sm-6">
                  <label for="inputPassword7">Email Address</label>
                  <input class="form-control" id="inputPassword7" type="email">
                </div>
              </div>
              <div class="mb-3">
                <label for="inputState">Country</label>
                <select class="form-control" id="inputState">
                  <option selected="">Choose@.</option>
                  <option>@.</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="inputAddress5">Address</label>
                <input class="form-control" id="inputAddress5" type="text">
              </div>
              <div class="mb-3">
                <label for="inputCity">Town/City</label>
                <input class="form-control" id="inputCity" type="text">
              </div>
              <div class="mb-3">
                <label for="inputAddress2">State/Country</label>
                <input class="form-control" id="inputAddress2" type="text">
              </div>
              <div class="mb-3">
                <label for="inputAddress6">Postal Code</label>
                <input class="form-control" id="inputAddress6" type="number">
              </div>
              <div class="mb-3">
                <div class="form-check">
                  <input class="form-check-input" id="gridCheck" type="checkbox">
                  <label class="form-check-label" for="gridCheck">Check me out</label>
                </div>
              </div>
            </form>
          </div>
          <div class="col-xl-6 col-sm-12">
            <div class="checkout-details">
              <div class="order-box">
                <div class="title-box">
                  <div class="checkbox-title">
                    <h2 class="mb-0">Product </h2><span>Total</span>
                  </div>
                </div>
                <ul class="qty" v-if="cart.length">
                  <li v-for="(item, index) in cart" :key="index">
                    {{ item.name }} × {{ item.quantity }}
                    <span>${{ item.price * item.quantity }}</span>
                  </li>
                </ul>
                <ul class="qty" v-if="!cart.length">
                  <li v-if="!cart.length">There are no products in cart</li>
                </ul>
                <ul class="sub-total">
                  <li>Subtotal <span class="count">${{ getAmount }}</span></li>
                  <li class="shipping-class">Shipping
                    <div class="shopping-checkout-option">
                      <label class="d-block" for="chk-ani">
                        <input class="checkbox_animated" id="chk-ani" type="checkbox" checked="">Option 1
                      </label>
                      <label class="d-block" for="chk-ani1">
                        <input class="checkbox_animated" id="chk-ani1" type="checkbox">Option 2
                      </label>
                    </div>
                  </li>
                </ul>
                <ul class="sub-total total">
                  <li>Total <span class="count">${{ getAmount }}</span></li>
                </ul>
                <div class="animate-chk" v-if="cart.length">
                  <div class="row">
                    <div class="col">
                      <label class="d-block" for="edo-ani1">
                        <input class="radio_animated" id="edo-ani1" value="stripe" v-model="selectedPayment" type="radio"
                          name="rdo-ani" data-original-title="">Stripe
                      </label>
                      <label class="d-block" for="edo-ani2">
                        <input class="radio_anima ted" id="edo-ani2" value="paypal" v-model="selectedPayment" type="radio"
                          name="rdo-ani" data-original-title="" title="">PayPal
                      </label>
                    </div>
                  </div>
                </div>
                <div id="paypal-button-container" :class="[{ 'd-none': selectedPayment != 'paypal' }]"></div>
                <div class="order-place" v-if="selectedPayment === 'stripe' && cart.length"><button
                    class="btn btn-primary" @click="payWithStripe">Place Order </button></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'pinia';
import { useProductStore } from '~~/store/product';
export default {
  name: 'checkoutView',
  data() {
    return {
      activeAmount: "0", totalAmount: 0,
      user: { firstName: '', lastName: '', phone: '', email: '', address: '', city: '', state: '', pincode: '' },
      submitted: false, payment: false, complete: false, selectedPayment: 'stripe'
    }
  },
  created() { this.activeAmount = 60; },
  computed: {
    ...mapState(useProductStore, {
      cart: 'cart',
      getAmount() {
        return (this.totalAmount = useProductStore().getTotalAmount
        );
      }
    }),
  },
  methods: {
    payWithStripe() {
      this.payment = false
      var handler = (window).StripeCheckout.configure({
      });
      handler.open({
        name: 'Cuba ',
        description: 'Your Choice Theme',
        amount: this.totalAmount * 100
      });
    },
  },
  mounted() {
    window.paypal.Buttons({
    }).render('#paypal-button-container')
  }
}
</script>