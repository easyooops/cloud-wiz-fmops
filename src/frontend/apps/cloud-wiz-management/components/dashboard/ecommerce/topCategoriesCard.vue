<template>
    <div class="card">
        <div class="card-header card-no-border">
            <h5>Top Categories</h5>
        </div>
        <div class="card-body pt-0">
            <ul class="categories-list">
                <li class="d-flex" v-for="category in topcategories" :key="category">
                    <div class="bg-light">
                        <img :src="getImgURL(category.image)" alt="vector burger" />
                    </div>
                    <div>
                        <h6 class="mb-0">
                            <a>
                                <NuxtLink to="/ecommerce/product">{{ category.name }}</NuxtLink>
                            </a>
                        </h6>
                        <span class="f-light f-12 f-w-500">({{ category.orders }})</span>
                    </div>
                </li>
            </ul>
            <div class="recent-activity notification">
                <h5>Recent Activity</h5>
                <ul>
                    <li class="d-flex">
                        <div class="activity-dot-primary"></div>
                        <div class="w-100 ms-3">
                            <p class="d-flex justify-content-between mb-2">
                                <span class="date-content light-background">8th March, 2022
                                </span>
                            </p>
                            <h6>
                                Added New Items<span class="dot-notification"></span>
                            </h6>
                            <span class="f-light">If you have it, you can make anything look good.</span>
                            <div class="recent-images">
                                <ul>
                                    <li v-for="product in products" :key="product">
                                        <div class="recent-img-wrap">
                                            <img :src="getImgURL(product.image)" alt="chair" />
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </li>
                    <li class="d-flex" v-for="activity in activities" :key="activity">
                        <div :class="activity.class"></div>
                        <div class="w-100 ms-3">
                            <p class="d-flex justify-content-between mb-2">
                                <span class="date-content light-background">{{ activity.date }}</span>
                            </p>
                            <h6>
                                {{ activity.title }}<span class="dot-notification"></span>
                            </h6>
                            <span>{{ activity.decription }}</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    topcategories,
    activities,
    products
} from "@/data/dashboard/ecommerce.json"
export default {
    data() {
        return {
            topcategories: topcategories,
            activities: activities,
            products: products
        }
    },
    methods: {
        getImgURL(path) {
            return '/images/dashboard-2/' + path
        }
    }
}
</script>
    