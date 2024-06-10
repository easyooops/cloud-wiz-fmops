<template>
    <div class="card">
        <div class="card-header">
            <h5>Datatable order history</h5>
        </div>
        <div class="card-body">
            <div class="order-history table-responsive">
                <table class="table table-bordernone display" id="basic-1">
                    <thead>
                        <tr>
                            <th scope="col">Prdouct</th>
                            <th scope="col">Prdouct name</th>
                            <th scope="col">Size</th>
                            <th scope="col">Color</th>
                            <th scope="col">Article number</th>
                            <th scope="col">Units</th>
                            <th scope="col">Price</th>
                            <th scope="col"><i class="fa fa-angle-down"></i></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="history in historys" :key="history">
                            <td><img class="img-fluid img-30" :src="getImageUrl(history.img)" alt="#"></td>
                            <td>
                                <div class="product-name"><a href="#">{{ history.product }}</a>
                                    <div class="order-process"><span class="order-process-circle"></span>{{
                                        history.prdouctstatus }}</div>
                                </div>
                            </td>
                            <td>{{ history.size }}</td>
                            <td>{{ history.color }}</td>
                            <td>{{ history.articlenumber }}</td>
                            <td>{{ history.units }}</td>
                            <td>{{ history.price }}</td>
                            <td>
                                <vue-feather type="more-vertical"></vue-feather>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
    
<script>
import data from "@/data/orederhistory.json"
import imageMixin from "@/mixin/commen/imageMixin"
export default {
    mixins: [imageMixin],
    data() {
        return {
            historys: data.data
        }
    },
}
</script>
    