<template>
  <div class="col-sm-12 box-col-12">
    <div class="card">
      <div class="card-header">
        <h5>MASONRY GALLERY</h5>
      </div>
      <div class="card-body photoswipe-pb-responsive" itemprop="associatedMedia" itemscope>
        <MasonryWall class="masonry-container isotopeContainer row my-gallery grid gallery mb-1" :items="imagearray"
          :padding="16" :column-width="300" :gap="15">
          <template #default="{ item }" class="col-md-3 col-sm-6 isotopeSelector grid-item item">
            <img @click="() => showImg(item)" :src="item.imagepath" alt="Image description" class="img-thumbnail" />
          </template>
        </MasonryWall>
        <vue-easy-lightbox :visible="visible" :index="index" :imgs="lightBoxImages" @hide="handleHide">
        </vue-easy-lightbox>
      </div>
    </div>
  </div>
</template>
<script>
import MasonryWall from '@yeger/vue-masonry-wall'
export default {
  components: { MasonryWall },
  data() {
    return {
      lightBoxImages: [], visible: false, index: '',
      imagearray: [
        { id: 1, imagepath: ('/images/masonry/1.jpg') },
        { id: 2, imagepath: ('/images/masonry/2.jpg') },
        { id: 3, imagepath: ('/images/masonry/3.jpg') },
        { id: 4, imagepath: ('/images/masonry/4.jpg') },
        { id: 5, imagepath: ('/images/masonry/5.jpg') },
        { id: 6, imagepath: ('/images/masonry/6.jpg') },
        { id: 7, imagepath: ('/images/masonry/8.jpg') },
        { id: 8, imagepath: ('/images/masonry/9.jpg') },
        { id: 9, imagepath: ('/images/masonry/10.jpg') },
        { id: 10, imagepath: ('/images/masonry/11.jpg') },
        { id: 11, imagepath: ('/images/masonry/12.jpg') },
        { id: 12, imagepath: ('/images/masonry/14.jpg') },
        { id: 13, imagepath: ('/images/masonry/15.jpg') },
        { id: 14, imagepath: ('/images/masonry/13.jpg') }
      ]
    };
  },
  methods: {
    showImg(index) {
      let Index = this.imagearray.indexOf(index)
      this.index = Index
      this.visible = true
    },
    handleHide() {
      this.visible = false
    },
  },
  mounted() {
    if (typeof this.$redrawVueMasonry === 'function') {
      this.$redrawVueMasonry();
    }
    this.imagearray.forEach(item => {
      this.lightBoxImages.push(item.imagepath)
    })
  },
}
</script>