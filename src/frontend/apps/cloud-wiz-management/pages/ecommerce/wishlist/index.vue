<template>
  <Breadcrumbs main="Ecommerce" title="WishList" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>Wishlist</h5>
          </div>
          <div class="card-body">
            <div class="row g-sm-4 g-3">
              <div class="col-xl-4 col-md-6" v-for="(item, index) in menu" :key="index">
                <div class="prooduct-details-box">
                  <div class="media"><img class="align-self-center img-fluid img-60" :src="getImgUrl(item.img)" alt="#">
                    <div class="media-body ms-3">
                      <div class="product-name">
                        <h6><router-link :to="'/ecommerce/product/page/' + item.id">{{ item.product }}</router-link></h6>
                      </div>
                      <div class="rating" v-for="index in menu.n" :key="index">
                        <i class="fa fa-star"></i>
                      </div>
                      <div class="price d-flex">
                        <div class="text-muted me-2">Price</div>: {{ item.price }}
                      </div>
                      <div class="avaiabilty">
                        <div class="text-success">In stock</div>
                      </div><router-link class="btn btn-primary btn-xs" to="/ecommerce/cart">Move to Cart</router-link>
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import order from '@/data/wishlist.json'

export default {
  name: 'wishlistView',
  data() {
    return {
      menu: order.data
    }
  },
  methods: {
    getImgUrl(path) {
      return ("/images/" + path);
    },
  }

}
</script>
