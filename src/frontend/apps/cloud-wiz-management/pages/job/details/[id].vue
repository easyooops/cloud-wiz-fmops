<template>
    <BreadCrumbs title="Job Details" main="Job Search" />
    <div class="container-fluid">
        <div class="row">
            <jobtab />
            <div class="col-xl-9 xl-60 text-start box-col-12">
                <div class="card">
                    <div class="job-search">
                        <div class="card-body">
                            <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(jobs.image)" alt="">
                                <div class="media-body">
                                    <h6 class="f-w-600">
                                        <nuxt-link :to="`/job/details/${jobs.id}`">{{ jobs.title }}</nuxt-link>
                                        <span class="pull-right">
                                            <nuxt-link :to='`/job/apply/${jobs.id}`'
                                                class="btn btn-primary">Apply</nuxt-link>
                                        </span>
                                    </h6>
                                    <p>{{ jobs.company }}, <span>{{ jobs.country }}</span><span class="ms-1"
                                            v-html="stars(jobs.stars)"></span></p>
                                </div>
                            </div>
                            <div class="job-description">
                                <h6>Job Description</h6>
                                <p v-html="jobs.description"></p>
                            </div>
                            <div class="job-description">
                                <h6>Responsibilities</h6>
                                <ul>
                                    <li v-for="(r, index) in jobs.resp" :key="index" v-text="r.title"></li>
                                </ul>
                            </div>
                            <div class="job-description">
                                <h6>Requirements</h6>
                                <ul>
                                    <li v-for="(rq, index) in jobs.reqs" :key="index" v-text="rq.title"></li>
                                </ul>
                            </div>
                            <div class="job-description">
                                <h6>Required Skills</h6>
                                <ul>
                                    <li>Proficient understanding of web markup, including HTML5, CSS3</li>
                                    <li v-for="(ski, index) in jobs.skills" :key="index" v-text="ski.title"></li>
                                </ul>
                            </div>
                            <div class="job-description">
                                <button class="btn btn-primary m-r-10" type="button"><span><i
                                            class="fa fa-check"></i></span> Save this job</button>
                                <button class="btn btn-primary " type="button"><span><i class="fa fa-share-alt"></i></span>
                                    Share</button>
                            </div>
                        </div>
                    </div>
                </div>
                <similarJobs />
            </div>
        </div>
    </div>
</template>
<script>
import { mapState } from 'pinia';
import { useJobStore } from '~~/store/jobs';
import jobtab from "@/components/job/list/jobTab.vue"
import similarJobs from "@/components/job/details/similarJobs.vue"
export default {
    components: { jobtab, similarJobs },
    props: ['id'],
    computed: {
        ...mapState(useJobStore, {
            jobslist: 'jobs',
        }),
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
    },

}
</script>