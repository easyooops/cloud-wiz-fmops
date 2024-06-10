<template>
    <div class="row">
        <div class="col-lg-4 col-md-6" v-for="(item, index) in menu" :key="index">
            <div class="project-box"><span class="badge" :class="item.class">{{ item.badge }}</span>
                <h6>{{ item.title }}</h6>
                <div class="d-flex mb-3"><img class="img-20 me-2 rounded-circle" :src="item.img" alt=""
                        data-original-title="" title="">
                    <div class="flex-grow-1 project-box-item">
                        <p>{{ item.sites }}</p>
                    </div>
                </div>
                <p>{{ item.desc }}</p>
                <div class="row details">
                    <div class="col-6"><span>Issues </span></div>
                    <div class="col-6 font-primary">{{ item.issue }} </div>
                    <div class="col-6"> <span>Resolved</span></div>
                    <div class="col-6 font-primary">{{ item.resolved }}</div>
                    <div class="col-6"> <span>Comment</span></div>
                    <div class="col-6 font-primary">{{ item.comment }}</div>
                </div>
                <div class="customers">
                    <ul>
                        <li class="d-inline-block"><img class="img-30 rounded-circle" :src="item.customers_img1" alt=""
                                data-original-title="" title=""></li>
                        <li class="d-inline-block"><img class="img-30 rounded-circle" :src="item.customers_img2" alt=""
                                data-original-title="" title=""></li>
                        <li class="d-inline-block"><img class="img-30 rounded-circle" :src="item.customers_img3" alt=""
                                data-original-title="" title=""></li>
                        <li class="d-inline-block ms-2">
                            <p class="f-12">+{{ item.like }} More</p>
                        </li>
                    </ul>
                </div>
                <div class="project-status mt-4">
                    <div class="d-flex mb-0">
                        <p>{{ item.progress }}% </p>
                        <div class="flex-grow-1 text-end"><span>Done</span></div>
                    </div>
                    <div class="progress" style="height: 5px">
                        <div class="progress-bar-animated  progress-bar-striped" :class="item.class" role="progressbar"
                            :style="{ 'width': item.width }" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import { All } from '@/data/projectlist/data'
export default {
    name: 'allPage',
    data() {
        return {
            menu: All
        }
    }
}
</script>