<template>
    <div class="row">
              <div class="col-sm-12">
                <div class="card">
                  <div class="card-header ">
                    <h5>Hover Effect <span class="digits">6</span></h5>
                  </div>
                  <div class="card-body">
                    <div class="row my-gallery gallery" id="aniimated-thumbnials" itemscope="" data-pswp-uid="1">
                      <figure class="col-md-3 col-6 img-hover hover-6"  
                              v-for="(n,index) in gallery1"  :key="index" 
                               @click="() => showImg(index)"
                              itemprop="associatedMedia" itemscope="">
                          <div >
                              <img :src="('/images/big-lightgallry/'+n.image)" itemprop="thumbnail" alt="Image description" class="img-fluid"></div>
                      </figure>
                    </div>
                    <vue-easy-lightbox
                  :visible="visible"
                  :index="index"
                  :imgs="lightBoxImages" 
                  @hide="handleHide"
                    >
                  </vue-easy-lightbox>
                  </div>
                </div>
              </div>
            </div> 
</template>
<script>
export default {
     data(){
        return{
             lightBoxImages:[],
            visible: false,
            gallery1: [
          {
            image:'01.jpg'
          },
          {
            image:'02.jpg'
          },
          {
            image:'03.jpg'
          },
          {
            image:'04.jpg'
          },
        ],
        }
    },
      methods: {
      showImg (index) {
        this.index = index
        this.visible = true
      },
      handleHide () {
        this.visible = false
      },
    },
    mounted(){
        this.gallery1.forEach(item=>{
            this.lightBoxImages.push(('/images/big-lightgallry/'+item.image))
        })
    }
}
</script>