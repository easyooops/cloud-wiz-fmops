<template>
  <Breadcrumbs main="Animation" title="WOW" />

  <div class="card">
    <div class="card-header">
      <h5>WOW Example Animation</h5>
    </div>
    <div class="card-body">
      <ClientOnly>
        <div v-masonry class="row gallery grid my-gallery" id="aniimated-thumbnials">
          <figure v-masonry-tile class="grid-item col-sm-4 col-md-3" v-for="(src, index) in imgs" :key="index"
            @click="() => showImg(index)">
            <aos-vue :animation="src.animation">
              <a>
                <img :src="('/images/masonry/' + src.image)" alt="Image description" class="img-thumbnail" />
              </a>
            </aos-vue>

          </figure>
        </div>
      </ClientOnly>
      <vue-easy-lightbox :visible="visible" :imgs="lightBoxImages" @hide="handleHide">
      </vue-easy-lightbox>
    </div>
  </div>
  <setupWow />
</template>
<script>
import setupWow from "@/components/animation/wow/setupWow.vue"
export default {
  components: { setupWow },
  data() {
    return {
      lightBoxImages: [],
      lightBoxTitle: [],
      visible: false,
      imgs: [
        { image: '1.jpg', animation: "fade-down" },
        { image: '2.jpg', animation: "zoom-out-down" },
        { image: '3.jpg', animation: "flip-down" },
        { image: '4.jpg', animation: "fade-up" },
        { image: '5.jpg', animation: "flip-down" },
        { image: '6.jpg', animation: "fade-up" },
        { image: '7.jpg', animation: "flip-down" },
        { image: '8.jpg', animation: "fade-up" },
        { image: '9.jpg', animation: "flip-down" },
        { image: '10.jpg', animation: "fade-up" },
        { image: '11.jpg', animation: "flip-down" },
        { image: '12.jpg', animation: "fade-up" },
        { image: '14.jpg', animation: "flip-down" },
        { image: '15.jpg', animation: "flip-left" },
        { image: '13.jpg', animation: "flip-down" },
        { image: '4.jpg', animation: "zoom-out" },
        { image: '5.jpg', animation: "flip-right" },
        { image: '6.jpg', animation: "zoom-out" },
        { image: '7.jpg', animation: "zoom-out-up" },
        { image: '8.jpg', animation: "zoom-out-down" },
        { image: '9.jpg', animation: "flip-down" },
        { image: '10.jpg', animation: "slide-up" },
        { image: '9.jpg', animation: "flip-down" },
        { image: '10.jpg', animation: "fade-up" },
        { image: '11.jpg', animation: "flip-down" },
        { image: '12.jpg', animation: "fade-up" },
        { image: '14.jpg', animation: "flip-down" },
        { image: '15.jpg', animation: "flip-left" },
        { image: '13.jpg', animation: "flip-down" },
        { image: '4.jpg', animation: "zoom-out" },
        { image: '5.jpg', animation: "flip-right" },
        { image: '6.jpg', animation: "zoom-out" },
        { image: '7.jpg', animation: "zoom-out-up" }
      ]
    }
  },
  methods: {
    showImg(index) {
      this.index = index
      this.visible = true
    },
    handleHide() {
      this.visible = false
    },
  },
  mounted() {
    this.imgs.forEach(item => {
      this.lightBoxImages.push(('/images/masonry/' + item.image))
      this.lightBoxTitle.push(item.title)
    })
  }
};
</script>