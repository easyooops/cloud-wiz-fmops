<template>
  <Breadcrumbs title="Blog Details" main="Blog" />
  <div class="container-fluid ">
    <div class="row">
      <div class="col-xl-6 set-col-12 box-col-12">
        <div class="card">
          <div class="blog-box blog-shadow"><img class="img-fluid bg-img-cover" src="/images/blog/blog.jpg" alt="">
            <div class="blog-details">
              <p>25 July 2023</p>
              <h4>A huge part of it is the incomparable beauty you can encounter every day.</h4>
              <ul class="blog-social">
                <li><i class="icofont icofont-user"></i>Mark Jecno</li>
                <li><i class="icofont icofont-thumbs-up"></i>02 Hits</li>
                <li><i class="icofont icofont-ui-chat"></i>598 Comments</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <detail />
      <detail1 />
    </div>
  </div>
</template>
<script>
import detail from "@/components/blog/details/detailPage.vue"
import detail1 from "@/components/blog/details/detail1Page.vue"
export default {
  components: {
    detail,
    detail1
  }
}
</script>