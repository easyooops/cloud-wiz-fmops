<template>
    <Breadcrumbs main="Learning" title="Learning List" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-xl-9 xl-60 order-xl-0 order-1 box-col-12">
                <div class="row">
                    <div class="col-xl-12" v-for="(course, index) in specialcourses" :key="'special' + index">
                        <div class="card">
                            <div class="blog-box blog-list row">
                                <div class="col-sm-5"><img class="img-fluid sm-100-w" :src="getImgUrl(course.image)" alt="">
                                </div>
                                <div class="col-sm-7">
                                    <div class="blog-details">
                                        <div class="blog-date"><span v-text="course.dd"></span> {{ course.mm }} {{ course.yy
                                        }}</div>
                                        <h6 v-text="course.title"></h6>
                                        <div class="blog-bottom-content">
                                            <ul class="blog-social">
                                                <li v-text="' by: ' + course.author"></li>
                                                <li class="digits" v-text="course.hits + ' Hits'"></li>
                                            </ul>
                                            <hr>
                                            <p class="mt-0" v-text="course.descr"></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-xl-4 xl-50 col-sm-6 box-col-6" v-for="(course, index) in normalcourses"
                        :key="'normal' + index">
                        <div class="card">
                            <div class="blog-box blog-grid text-center product-box">
                                <div class="product-img"><img class="img-fluid top-radius-blog"
                                        :src="getImgUrl(course.image)" alt="">
                                    <div class="product-hover">
                                        <ul>
                                            <li>

                                                <nuxt-link to="/learning/details/1"><i class="icon-link"></i> </nuxt-link>

                                            </li>
                                            <li><i class="icon-import"></i></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="blog-details-main">
                                    <ul class="blog-social">
                                        <li>{{ course.dd }}{{ course.mm }}{{ course.yy }}</li>
                                        <li>by: {{ course.author }}</li>
                                        <li>{{ course.hits }} Hits</li>
                                    </ul>
                                    <hr>
                                    <h6 class="blog-bottom-details">{{ course.descr }}</h6>

                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>

            <learningtab />

        </div>
    </div>
</template>

<script>
import learningtab from "@/components/learning/list/learningTab.vue"

import { useCourseStore } from "~~/store/courses";

export default {
    components: {
        learningtab
    },
    computed: {
        specialcourses() {
            return useCourseStore().specialcourses
        },
        normalcourses() {
            return useCourseStore().normalcourses
        }
    },
    methods: {
        getImgUrl(filename) {
            return ('/images/faq/' + filename)
        },

    }
}
</script>
