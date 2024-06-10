<template>
  <Breadcrumbs title="Masonry Gallery With Desc" main="Gallery" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>MASONRY GALLERY WITH DESCRIPTION</h5>
          </div>
          <div class="card-body">
            <MasonryWall class="my-gallery row grid gallery-with-description mb-1" :items="imagearray" :padding="16"
              :column-width="300" :gap="15">
              <template #default="{ item }" class="grid-item col-xl-3 col-sm-6 isotopeSelector item">

                <img :src="item.imagepath" @click="() => showImg(item)" alt="Image description" class="img-thumbnail" />

                <div class="caption">
                  <h4>Portfolio Title</h4>
                  <p>Here is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                    industry's standard dummy.</p>
                </div>
              </template>
            </MasonryWall>
            <vue-easy-lightbox :visible="visible" :index="index" :imgs="lightBoxImages" @hide="handleHide">
            </vue-easy-lightbox>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import MasonryWall from '@yeger/vue-masonry-wall'

export default {
  components: {
    MasonryWall
  },
  data() {
    return {
      lightBoxImages: [],
      visible: false,
      index: '',
      imagearray: [
        { imagepath: ('/images/masonry/1.jpg') },
        { imagepath: ('/images/masonry/2.jpg') },
        { imagepath: ('/images/masonry/3.jpg') },
        { imagepath: ('/images/masonry/4.jpg') },
        { imagepath: ('/images/masonry/5.jpg') },
        { imagepath: ('/images/masonry/6.jpg') },
        { imagepath: ('/images/masonry/7.jpg') },
        { imagepath: ('/images/masonry/8.jpg') },
        { imagepath: ('/images/masonry/9.jpg') },
        { imagepath: ('/images/masonry/10.jpg') },
        { imagepath: ('/images/masonry/11.jpg') },
        { imagepath: ('/images/masonry/12.jpg') },
        { imagepath: ('/images/masonry/14.jpg') },
        { imagepath: ('/images/masonry/15.jpg') },
        { imagepath: ('/images/masonry/13.jpg') }
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
    this.imagearray.forEach(item => {
      this.lightBoxImages.push(item.imagepath)
    })
  }
}
</script>