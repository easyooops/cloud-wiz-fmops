<template>
  <Breadcrumbs title="Blog Single" main="Blog" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="blog-single">
          <div class="blog-box blog-details"><img class="img-fluid w-100" src="/images/blog/blog-single.jpg"
              alt="blog-main">
            <div class="blog-details">
              <ul class="blog-social">
                <li>25 July 2023</li>
                <li><i class="icofont icofont-user"></i>Mark <span>Jecno </span></li>
                <li><i class="icofont icofont-thumbs-up"></i>02<span>Hits</span></li>
                <li><i class="icofont icofont-ui-chat"></i>598 Comments</li>
              </ul>
              <h4>
                The Harpeth rises in the westernmost part of Rutherford County, just to the east of the community of
                College Grove in eastern Williamson County.
              </h4>
              <div class="single-blog-content-top">
                <p>From the east coast to the west, each river has its own beauty and character. Each river has its own
                  story. Take a look at some America’s best rivers and some of the rivers we’re working to protect. And
                  learn some facts about your favorite rivers. The Harpeth River and its tributaries are home to rich
                  freshwater biodiversity, including more than 50 species of fish and 30 species of mussels</p>
                <p>The Harpeth River flows through the heart of downtown Franklin, the 14th fastest growing city in the
                  United States, and traverses Williamson County, one of the fastest growing counties in Tennessee. This
                  rapid development has already caused harm to the river from adding treated sewage, increasing stormwater
                  runoff, and withdrawing water.The river’s impairment is caused by dangerously low levels of dissolved
                  oxygen driven by high concentrations of nutrients – particularly phosphorus – that fuel oxygen-hungry
                  algal blooms that can lead to toxic conditions.</p>
              </div>
            </div>
          </div>
          <comment />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import comment from "@/components/blog/single/commentPage.vue"
export default {
  components: {
    comment
  }
}
</script>