<template>
    <div class="col-sm-12 empty-cart-cls text-center" v-if="!cart.length">
        <img :src="getImgUrl('ecommerce/icon-empty-cart.png')" class="img-fluid mb-4" />
        <h3><strong>Your Cart is Empty</strong></h3>
        <h4>Add something to make me happy :)</h4>
        <router-link :to="'/ecommerce/product'" class="btn btn-primary cart-btn-transform m-t-15">continue
            shopping</router-link>
    </div>
</template>
<script>

import { mapState } from "pinia";
import { useProductStore } from '~~/store/product';
export default {
    components: {},
    data() {
        return {
            counter: 1,
        };
    },
    computed: {
        ...mapState(useProductStore, {
            cart: 'cart',
            getAmount() {
                return (this.totalAmount =
                    useProductStore().getTotalAmount);
            },
        }),
    },
    methods: {
        getImgUrl(path) {
            return ("/images/" + path);
        },
        removeProduct: function (product) {
            useProductStore().removeProduct(product)
        },
        increment(product, qty = 1) {

            useProductStore().updateCartQuantity({
                product: product,
                qty: qty,
            })
        },
        decrement(product, qty = -1) {

            useProductStore().updateCartQuantity({
                product: product,
                qty: qty,
            })
        },
    },
    mounted() {
        let a = []
        if (a.length == 0) {
        }
    }
};
</script>