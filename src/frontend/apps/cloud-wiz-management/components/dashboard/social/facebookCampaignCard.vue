<template>
    <div class="col-lg-12 col-sm-6">
        <div class="card follower-wrap">
            <div class="card-header card-no-border">
                <h5 class="mb-1">Facebook Campaign</h5>
                <div class="d-inline-block badge badge-light-success rounded-pill">
                    Active
                </div>
            </div>
            <div class="card-body pt-0 papernote-wrap">
                <ul class="campaign-list">
                    <li>
                        <div class="campaign-box">
                            <h5 class="mb-1">1,897</h5>
                            <span class="f-light">Followers today</span>
                        </div>
                    </li>
                    <li>
                        <div class="campaign-box">
                            <h5 class="mb-1">50,000</h5>
                            <span class="f-light">Followers goals</span>
                        </div>
                    </li>
                </ul>
                <div class="customers">
                    <ul>
                        <li class="d-inline-block" v-for="item in users" :key="item">
                            <img class="img-40 rounded-circle" :src="getImgURL(item.image)" alt="user" />
                        </li>
                        <li class="d-inline-block">
                            <div class="light-card">
                                <span class="f-w-500">+5</span>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

    
    
<script>
import {
    socialDashboard
} from "@/data/comon";
import {
    users
} from "@/data/dashboard/social.json"

export default {
    data() {
        return {
            socialDashboard: socialDashboard,
            users: users
        };
    },
    methods: {
        getImgURL(path) {
            return '/images/dashboard/' + path
        }
    }
};
</script>
