<template>
    <div class="card">
        <div class="card-header">
            <h5>Shipped Orders</h5>
        </div>
        <div class="card-body">
            <div class="row g-sm-4 g-3">
                <div class="col-xxl-4 col-md-6" v-for="(items, index) in data2" :key="'b' + index">
                    <div class="prooduct-details-box">
                        <div class="media"><img class="align-self-center img-fluid img-60" :src="getImageUrl(items.src)"
                                alt="#">
                            <div class="media-body ms-3">
                                <div class="product-name">
                                    <h6><a href="#">{{ items.product }}</a></h6>
                                </div>
                                <div class="rating"><i class="fa fa-star"></i><i class="fa fa-star"></i><i
                                        class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                                <div class="price d-flex">
                                    <div class="text-muted me-2">Price</div>: 210$
                                </div>
                                <div class="avaiabilty">
                                    <div class="text-success">In stock</div>
                                </div><a class="btn btn-success btn-xs" href="#">Shipped</a>
                                <vue-feather class="close" type="x" @click="remove2(item)"></vue-feather>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
    
<script>
import { shipped } from '@/data/orderHistory'
import imageMixin from "@/mixin/commen/imageMixin"
export default {
    name: 'orderHistory',
    mixins: [imageMixin],
    data() {
        return {
            data: JSON.parse(JSON.stringify(shipped)),
            data2: JSON.parse(JSON.stringify(shipped)),
            data3: JSON.parse(JSON.stringify(shipped))
        }
    },
    methods: {
        remove(item) {
            this.data.splice(item, 1)
        },
        remove2(item) {
            this.data2.splice(item, 1)
        },
        remove3(item) {
            this.data3.splice(item, 1)
        }
    }
}
</script>