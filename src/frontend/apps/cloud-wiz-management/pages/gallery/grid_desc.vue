<template>
  <Breadcrumbs title="Gallery Grid With Description" main="Gallery" />
  <div class="container-fluid">

    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>IMAGE GALLERY WITH DESCRIPTION</h5>
          </div>
          <div class="my-gallery card-body row gallery-with-description" itemscope="">

            <figure v-for="(src, index) in imgs" :key="index" class="col-xl-3 col-sm-6" @click="() => showImg(index)">
              <img :src="('/images/big-lightgallry/' + src.image)" alt="Image description" class="img-thumbnail" />
              <div class="caption">
                <h4>Portfolio Title</h4>
                <p>is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
                  standard dummy.</p>
              </div>

            </figure>
          </div>
          <vue-easy-lightbox :visible="visible" :index="index" :imgs="lightBoxImages" @hide="handleHide">
          </vue-easy-lightbox>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      lightBoxImages: [],
      visible: false,
      index: '',
      imgs: [
        {
          image: '01.jpg',
          title: 'Image caption  1',
        },
        {
          image: '02.jpg'
        },
        {
          image: '03.jpg'
        },
        {
          image: '04.jpg'
        },
        {
          image: '05.jpg'
        },
        {
          image: '011.jpg'
        },
        {
          image: '010.jpg'
        },
        {
          image: '08.jpg'
        },
        {
          image: '013.jpg'
        },
        {
          image: '014.jpg'
        },
        {
          image: '015.jpg'
        },
        {
          image: '016.jpg'
        },
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
      this.lightBoxImages.push(
        ('/images/big-lightgallry/' + item.image),
      )
    })

  }
}
</script>