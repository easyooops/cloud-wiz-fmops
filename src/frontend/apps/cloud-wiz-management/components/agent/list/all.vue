<template>
    <div class="row">
        <div class="col-lg-4 col-md-6" v-for="(item, index) in menu" :key="index">
            <div class="project-box"><span class="badge" :class="item.class">{{ item.badge }}</span>
                <h6>{{ item.title }}</h6>
                <p>{{ item.desc }}</p>
                <div class="row details">
                    <div class="col-6"><span>Created </span></div>
                    <div class="col-6 font-primary">{{ item.created }} </div>
                    <div class="col-6"> <span>Updated</span></div>
                    <div class="col-6 font-primary">{{ item.updated }}</div>
                    <div class="col-6"> <span>Request</span></div>
                    <div class="col-6 font-primary">{{ item.request }}</div>                                        
                    <div class="col-6"> <span>Token</span></div>
                    <div class="col-6 font-primary">{{ item.token }}</div>
                    <div class="col-6"> <span>Cost</span></div>
                    <div class="col-6 font-primary">{{ item.cost }}</div>                    
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
                            <p class="f-12">+{{ item.chain }} Chain</p>
                        </li>
                    </ul>
                </div>
                <div class="project-status mt-4">
                    <div class="d-flex mb-0">
                        <p>{{ item.progress }}% </p>
                        <div class="flex-grow-1 text-end"><span>Expiry</span></div>
                    </div>
                    <div class="progress" style="height: 5px">
                        <div class="progress-bar-animated  progress-bar-striped" :class="item.class" role="progressbar"
                            :style="{ 'width': item.width }" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>
                <div>
                    <button data-bs-toggle="modal" data-bs-target="#agent-modal" class="btn btn-primary plus-popup mt-3">
                        API
                    </button>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
import { All } from '@/data/agent/data'
export default {
    name: 'all',
    data() {
        return {
            menu: All
        }
    }
}
</script>