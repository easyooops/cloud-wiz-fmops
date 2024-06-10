<template>
    <div class="product-filter pb-0 new-products">
        <div class="owl-carousel owl-theme" id="testimonial">
            <swiper :navigation="true" :slides-per-view="1" :space-between="20" :modules="modules" :loop="true">
                <swiper-slide>
                    <div class="item">
                        <div class="product-box row mt-2" v-for="(item, index) in swiper" :key="index">
                            <div class="product-img col-md-5"><img class="img-fluid img-100" :src="getImageUrl(item.image)"
                                    alt="" data-original-title="" title="">
                            </div>
                            <div class="product-details col-md-7 text-start"><span><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning"></i></span>
                                <p class="mb-0">{{ item.title }}</p>
                                <div class="product-price">${{ item.price }}</div>
                            </div>
                        </div>
                    </div>
                </swiper-slide>
                <swiper-slide>
                    <div class="item">
                        <div class="product-box row mt-2" v-for="(item, index) in swiper1">
                            <div class="product-img col-md-5"><img class="img-fluid img-100" :src="getImageUrl(item.image)"
                                    alt="" data-original-title="" title="">
                            </div>
                            <div class="product-details col-md-7 text-start"><span><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning me-1"></i><i
                                        class="fa fa-star font-warning"></i></span>
                                <p class="mb-0">{{ item.title }}</p>
                                <div class="product-price">${{ item.price }}</div>
                            </div>
                        </div>
                    </div>
                </swiper-slide>
            </swiper>
        </div>
    </div>
</template>
<script>
import { useProductStore } from '~~/store/product';
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import "swiper/css/navigation";
import { Navigation } from 'swiper/modules';
import imageMixin from "@/mixin/commen/imageMixin"
export default {
    name: 'filterPage',
    mixins: [imageMixin],
    data() {
        return {
            swiper: useProductStore().swiper,
            swiper1: useProductStore().swiper1
        }
    },
    components: {
        Swiper,
        SwiperSlide
    },
    computed: {
        price() {
            return useProductStore().price
        },
        filterProduct() {
            return useProductStore().filterProducts
        }
    },
    methods: {
        selectColor(event) {
            this.isActive = !this.isActive
            this.applyFilter.push(event.target.value)
            useProductStore().setTags(this.applyFilter)
        },

        addfilter() {
            useProductStore().setTags(this.applyFilter)

        },
        setchange() {
            useProductStore().priceFilter({ min: this.min, max: this.start })
        }
    },
    setup() {
        return {
            modules: [Navigation]
        }
    }
}
</script>  