<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Cart</h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <emptyCart />
                    <div class="order-history table-responsive wishlist" v-if="cart.length">
                        <table class="table table-bordered">
                            <thead>
                                <tr>
                                    <th>Prdouct</th>
                                    <th>Prdouct Name</th>
                                    <th>Price</th>
                                    <th>Quantity</th>
                                    <th>Action</th>
                                    <th>Total</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(item, index) in cart" :key="index">
                                    <td><img class="img-fluid img-40" :src='getImageUrl(item.images[0])' alt="#"></td>
                                    <td>
                                        <div class="product-name"><router-link :to="'/ecommerce/product/page/' + item.id">
                                                <h6>{{ item.name }}</h6>
                                            </router-link></div>
                                    </td>
                                    <td>${{ item.price }}</td>
                                    <td>
                                        <fieldset class="qty-box">
                                            <div class="input-group bootstrap-touchspin">
                                                <button class="btn btn-primary btn-square bootstrap-touchspin-down"
                                                    v-on:click="decrement(item)" type="button">
                                                    <i class="fa fa-minus"></i></button>
                                                <input class="touchspin text-center form-control" v-model="item.quantity"
                                                    name="item.quantity" type="text">
                                                <button class="btn btn-primary btn-square bootstrap-touchspin-up"
                                                    v-on:click="increment(item)" type="button">
                                                    <i class="fa fa-plus"></i></button>
                                            </div>
                                        </fieldset>
                                    </td>
                                    <td><a href="javascript:void(0)" @click='removeProduct(item)'><vue-feather
                                                type="x-circle"></vue-feather></a></td>
                                    <td>${{ item.price * item.quantity }}</td>
                                </tr>
                                <tr>
                                    <td colspan="4">
                                        <div class="input-group">
                                            <input class="form-control me-2" type="text" placeholder="Enter coupan code"><a
                                                class="btn btn-primary" href="#">Apply</a>
                                        </div>
                                    </td>
                                    <td class="total-amount">
                                        <h6 class="m-0 text-end"><span class="f-w-600">Total Price :</span></h6>
                                    </td>
                                    <td><span>${{ getAmount }} </span></td>
                                </tr>
                                <tr>
                                    <td class="text-end" colspan="5">
                                        <router-link :to="'/ecommerce/product'"
                                            class="btn btn-secondary cart-btn-transform">continue shopping</router-link>
                                    </td>
                                    <td>
                                        <router-link :to="'/ecommerce/checkout'" class="btn btn-success cart-btn-transform">
                                            check out</router-link>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from "pinia";
import { useProductStore } from '~~/store/product';
import emptyCart from "./emptyCart.vue"
import imageMixin from "@/mixin/commen/imageMixin"
export default {
    mixins: [imageMixin],
    data() {
        return { counter: 1, };
    },
    components: { emptyCart },
    computed: {
        ...mapState(useProductStore, {
            cart: 'cart', getAmount() { return (this.totalAmount = useProductStore().getTotalAmount); },
        }),
    },
    methods: {
        removeProduct: function (product) {
            useProductStore().removeProduct(product)
        },
        increment(product, qty = 1) {
            useProductStore().updateCartQuantity({
                product: product, qty: qty,
            })
        },
        decrement(product, qty = -1) {
            useProductStore().updateCartQuantity({
                product: product, qty: qty,
            })
        },
    },
    mounted() {
        let a = []
        if (a.length == 0) { }
    }
};
</script>