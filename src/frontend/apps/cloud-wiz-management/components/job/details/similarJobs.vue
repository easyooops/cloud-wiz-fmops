<template>
    <div class="header-faq">
        <h6 class="mb-0 f-w-600">Similar jobs</h6>
    </div>
    <div class="row">
        <div class="col-xl-6 box-col-12 xl-100" v-for="(j, index) in jobslist" :key="index">
            <div class="card">
                <div class="job-search">
                    <div class="card-body">
                        <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(j.image)" alt="">
                            <div class="media-body">
                                <h6 class="f-w-600">

                                    <nuxt-link :to="`/job/details/${j.id}`">{{ j.title }}</nuxt-link>

                                    <span class="pull-right" v-if="j.date" v-text="j.date"></span>
                                    <span class="badge badge-primary pull-right" v-else>New</span>
                                </h6>
                                <p>{{ j.company }} <span>{{ j.city }}, {{ j.country }} </span><span class="ms-1"
                                        v-html="stars(j.stars)"></span></p>
                            </div>
                        </div>
                        <p v-html="j.description"></p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

import { mapState } from 'pinia';
import { useJobStore } from '~~/store/jobs';
export default {
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
