<template>
  <div class="card">
    <div class="card-header">
      <h3>Basic Example</h3>
    </div>
    <div class="card-body">
      <div class="owl-carousel owl-theme" id="owl-carousel-1">
        <swiper autoHeight: true :slidesPerView="5" :space-between="20" :pagination="{
          clickable: true,
        }" :modules="modules" :breakpoints="swiperOptions.breakpoints">
          <swiper-slide v-for="(item, index) in menu" :key="index">
            <div class="item"><img :src="getImgUrl(item.value)" alt="" class="img-fluid"></div>
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h3>Responsive Example</h3>
    </div>
    <div class="card-body">
      <div class="owl-carousel owl-theme" id="owl-carousel-2">
        <swiper autoHeight: true :slides-per-view="3" :space-between="20" :pagination="{
          clickable: true,
        }" :modules="modules" :breakpoints="swiperOptions1.breakpoints">
          <swiper-slide v-for="(item, index) in menu" :key="index">
            <div class="item"><img :src="getImgUrl(item.value)" alt="" class="img-fluid"></div>
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h3>Center Example</h3>
    </div>
    <div class="card-body">
      <div class="owl-carousel owl-theme" id="owl-carousel-3">
        <swiper autoHeight: true :slides-per-view="3" :space-between="20" :pagination="{
          clickable: true,
        }" :modules="modules" :breakpoints="swiperOptions1.breakpoints">
          <swiper-slide v-for="(item, index) in menu" :key="index">
            <div class="item"><img :src="getImgUrl(item.value)" alt="" class="img-fluid"></div>
          </swiper-slide>
        </swiper>
      </div>
    </div>
  </div>
</template>
<script>
import { Swiper, SwiperSlide } from "swiper/vue";
import "swiper/css";
import "swiper/css/pagination";
import { owlData } from '@/data/uikits/data'
import { Pagination } from "swiper/modules";
export default {
  components: {
    Swiper, SwiperSlide,
  },
  data() {
    return {
      menu: owlData,
      swiperOptions: {
        breakpoints: {
          1000: {
            slidesPerView: 5
          },
          600: {
            slidesPerView: 3
          },
          0: {
            slidesPerView: 1
          }
        }
      },
      swiperOptions1: {
        breakpoints: {
          1000: {
            slidesPerView: 3
          },
          767: {
            slidesPerView: 2
          },
          0: {
            slidesPerView: 1
          }
        }
      }
    }
  },
  setup() {
    return {
      modules: [Pagination],
    };
  },
  methods: {
    getImgUrl(path) {
      return ('/images/' + path)
    }
  }
}
</script>