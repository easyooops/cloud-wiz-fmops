<template>
    <Breadcrumbs title="Job Apply" main="Job Search" />
    <div class="container-fluid">
        <div class="row">
            <jobtab />
            <div class="col-xl-9 xl-60 text-start box-col-12">
                <div class="card">
                    <div class="job-search">
                        <div class="card-body pb-0">
                            <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(jobs.image)" alt="">
                                <div class="media-body">
                                    <h6 class="f-w-600">
                                        <nuxt-link :to="`/job/details/${jobs.id}`">{{ jobs.title }}</nuxt-link>

                                        <span class="pull-right"><button class="btn btn-primary" type="button"><span><i
                                                        class="fa fa-check text-white"></i></span> Save this
                                                job</button></span>
                                    </h6>
                                    <p>{{ jobs.company }}, <span>{{ jobs.country }}</span><span class="ms-1"
                                            v-html="stars(jobs.stars)"></span></p>
                                </div>
                            </div>
                            <div class="job-description">
                                <personal />
                                <education />
                                <experience />
                                <upload />
                            </div>
                        </div>
                        <div class="card-footer">
                            <button class="btn btn-primary m-r-10" type="submit">Submit</button>
                            <nuxt-link class="btn btn-light" :to="`/job/details/${jobs.id}`">Cancel</nuxt-link>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'pinia';
// import router from '@/router';
import { useJobStore } from '~~/store/jobs';

import jobtab from "@/components/job/list/jobTab.vue"
import Personal from "@/components/job/apply/personal/personalPage.vue"
import education from "@/components/job/apply/educationPage.vue"
import experience from "@/components/job/apply/experiencePage.vue"
import upload from "@/components/job/apply/uploadPage.vue"
export default {
    components: {
        jobtab,
        Personal,
        education,
        experience,
        upload
    },
    computed: {
        jobs() {
            return useJobStore().jobs.find(job => {
                if (parseInt(useRoute().params.id) === job.id)
                    return job;
            })
        }
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
