<template>
  <Breadcrumbs title="Job List" main="Job Search" />
  <div class="container-fluid">
    <div class="row">
      <jobtab />
      <div class="col-xl-9 xl-60 text-start box-col-12">

        <div class="card" v-for="(job, index) in jobslist" :key="index"
          :class="{ 'ribbon-vertical-left-wrapper': job.priority == 1 }">
          <div v-if="job.priority == 1" class="ribbon ribbon-bookmark ribbon-vertical-left ribbon-secondary"><i
              class="icofont icofont-love"></i></div>
          <div class="job-search">
            <div class="card-body">
              <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(job.image)" alt="">
                <div class="media-body">
                  <h6 class="f-w-600">

                    <nuxt-link :to="`/job/details/${job.id}`">{{ job.title }}</nuxt-link>

                    <span class="pull-right" v-if="job.date" v-text="job.date"></span>
                    <span class="badge badge-primary pull-right" v-else>New</span>
                  </h6>
                  <p>{{ job.city }}<span class="ms-1" v-html="stars(job.stars)"></span></p>
                </div>
              </div>
              <p v-text="job.description"></p>
            </div>
          </div>
        </div>

        <div class="job-pagination">
          <nav aria-label="Page navigation example">
            <ul class="pagination pagination-primary">
              <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
              <li class="page-item active"><a class="page-link" href="#">1</a></li>
              <li class="page-item"><a class="page-link" href="#">2</a></li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item"><a class="page-link" href="#">Next</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'pinia';
import jobtab from "@/components/job/list/jobTab.vue"
import { useJobStore } from '~~/store/jobs';
export default {
  components: {
    jobtab
  },
  computed: {
    ...mapState(useJobStore, {
      jobslist: 'jobs',
    })
  },

  methods: {
    getImgUrl(filename) {
      return ('/images/job-search/' + filename)
    },
    stars(count) {
      var stars = '';

      for (var i = 0; i < 5; i++) {
        if (count > i) {
          stars = stars + '<i class="fa fa-star font-warning"></i>';
        } else {
          stars = stars + '<i class="fa fa-star font-warning-o"></i>';
        }
      }

      return stars;
    }
  }
}
</script>