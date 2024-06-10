<template>
  <div class="col-md-6 col-xxl-3 box-col-6" v-for="(item,index) in items" :key="index">
    <div class="card">
      <div class="blog-box blog-grid text-center">
        <div class="blog-wrraper"><a href="blog-single.html"><img class="img-fluid top-radius-blog" :src="getImageUrl(item.image)" alt=""></a></div>
        <div class="blog-details-main">
          <ul class="blog-social">
            <li>9 April 2023</li>
            <li>by: Admin</li>
            <li>0 Hits</li>
          </ul>
          <hr>
          <h6 class="blog-bottom-details">A garden where plants that flower are grown and displayed in floral garden.</h6>
        </div>
      </div>
    </div>
  </div>
  
              
</template>
<script>
export default {
  data(){
    return{
      items:[{id:1, title:"Perspiciatis unde omnis.", desc:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.", image:"blog-5.jpg"},
      {id:1, title:"Perspiciatis unde omnis.", desc:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.", image:"blog-6.jpg"},
      {id:1, title:"Perspiciatis unde omnis.", desc:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.", image:"blog-5.jpg"},
      {id:1, title:"Perspiciatis unde omnis.", desc:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.", image:"blog-6.jpg"},
      ]
    }
  },
  methods: {
    getImageUrl(path) {
      return ("/images/blog/" + path);
    },
  },
}
</script>