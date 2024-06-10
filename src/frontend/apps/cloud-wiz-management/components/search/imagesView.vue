<template>
  <div>

    <h6 class="mb-2">About 12,120 results (0.50 seconds)</h6>
    <div class="my-gallery row gallery-with-description" id="aniimated-thumbnials" itemscope="">
      <div v-for="(src, index) in imgs" :key="index" class="col-xl-3 col-sm-6 mb-4" @click="() => showImg(index)">
        <img :src="('/images/big-lightgallry/' + src.image)" alt="Image description" class="img-fluid" />
        <div class="caption">
          <h4> {{ src.title }}</h4>
          <p>{{ src.descr }}</p>
        </div>
      </div>
    </div>
    <vue-easy-lightbox :visible="visible" :imgs="lightBoxImages" @hide="handleHide">
    </vue-easy-lightbox>

  </div>
</template>
<script>
export default {
  data() {
    return {
      lightBoxImages: [],
      visible: false,
      imgs: [
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '01.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '02.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '03.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '04.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '05.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '011.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '010.jpg'
        },
        {
          title: 'Portfolio Title',
          descr: 'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
          image: '08.jpg'
        }
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
      this.lightBoxImages.push(('/images/big-lightgallry/' + item.image))
    })
  }
};
</script>
