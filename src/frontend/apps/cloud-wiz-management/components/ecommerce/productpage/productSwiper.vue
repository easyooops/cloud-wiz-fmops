<template>
    <div class="col-xxl-4 col-md-6 box-col-12">
        <div class="card">
            <div class="card-body">
                <Swiper :slidesPerView="1" :loop="true" :thumbs="{ swiper: thumbsSwiper }"
                    :autoplay="{ delay: 3500, disableOnInteraction: false, }" :spaceBetween="30" :centeredSlides="true"
                    :modules="modules" dir="rtl" class="mySwiper">
                    <swiper-slide v-for="(product, index) in products.images" :key="index" class="item">
                        <img :src="getImgUrl(product)" :id="index" alt="index" style="    display: block;
                                                                                            width: 100%;
                                                                                            border-radius: 5px;" />
                    </swiper-slide>

                </swiper>
                <Swiper @swiper="setThumbsSwiper" :loop="true" :slidesPerView="3" :spaceBetween="3"
                    :watchSlidesProgress="true" :pagination="{
                        clickable: true,
                    }" :modules="modules" dir="rtl" class="Swiper">
                    <swiper-slide v-for="(product, index) in products.images" :key="index" class="item">
                        <img :src="getImgUrl(product)" alt="index" style="    display: block;
                                                                                            width: 100%;
                                                                                            border-radius: 5px;">
                    </swiper-slide>
                </swiper>

            </div>
        </div>
    </div>
</template>
<script>
import { ref } from 'vue';
import { Swiper, SwiperSlide } from "swiper/vue";
import productPage from "@/mixin/productPage"
import imageMixin from "@/mixin/commen/imageMixin"
import "swiper/css";
import { Autoplay, FreeMode, Navigation, Thumbs } from "swiper/modules";
export default {
    name: "productPage",
    mixins: [productPage, imageMixin],
    data() {
        return {
        }
    },
    components: {
        Swiper,
        SwiperSlide,
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
            return ('/images/' + path);
        },
    }
}
</script>