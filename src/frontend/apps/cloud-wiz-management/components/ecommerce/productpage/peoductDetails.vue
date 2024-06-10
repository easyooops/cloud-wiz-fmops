<template>
    <div class="col-xxl-5 box-col-6 order-xxl-0 order-1">
        <div class="card">
            <div class="card-body">
                <div class="product-page-details">
                    <h3>{{ products.name }}</h3>
                </div>
                <div class="product-price">${{ products.price }}
                    <del>${{ products.discountPrice }} </del>
                </div>
                <ul class="product-color">
                    <li class="bg-primary"> </li>
                    <li class="bg-secondary"></li>
                    <li class="bg-success"></li>
                    <li class="bg-warning"></li>
                    <li class="bg-danger"></li>
                </ul>
                <hr>
                <p>Rock Paper Scissors Various Dots Half Sleeves Girl’s Regular Fit T-Shirt I 100% Cotton T Shirt with Half
                    Sleeve Round Neck I Regular Wear Solid Kids Tees and Black Sleeve.</p>
                <hr>
                <productSocial />
                <hr>
                <div class="m-t-15 btn-showcase"><router-link class="btn btn-primary" to="/ecommerce/cart" title=""> <i
                            class="fa fa-shopping-basket me-1"></i>Add To Cart</router-link>
                    <router-link class="btn btn-success" to="/ecommerce/checkout" title=""> <i
                            class="fa fa-shopping-cart me-1"></i>Buy Now</router-link>
                    <router-link class="btn btn-secondary" to="/ecommerce/wishlist"> <i class="fa fa-heart me-1"></i>Add To
                        WishList</router-link>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
import { ref } from 'vue';
import { Swiper, SwiperSlide } from "swiper/vue";
import productPage from "@/mixin/productPage"
import imageMixin from "@/mixin/commen/imageMixin"
import productSocial from "./productSocial.vue"
import "swiper/css";
import { Autoplay, FreeMode, Navigation, Thumbs } from "swiper/modules";
export default {
    name: "productPage",
    mixins: [productPage, imageMixin],
    components: {
        Swiper, SwiperSlide, productSocial
    },
    setup() {
        const thumbsSwiper = ref(null)
        const setThumbsSwiper = (swiper) => {
            thumbsSwiper.value = swiper;
        }
        return {
            modules: [Autoplay, Navigation, FreeMode, Thumbs], thumbsSwiper,
            setThumbsSwiper,
        };
    },
    methods: {
        filled(len) {
            this.selectedStars = len;
        },
        addToCart: function (product, qty) {
            product.quantity = qty ? qty : 1;
            useProductStore().addToCart(product)
        },
        getImgUrl(path) {
            return ('/images/ecommerce/' + path);
        },
    }
}
</script>