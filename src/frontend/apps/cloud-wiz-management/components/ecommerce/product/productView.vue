<template>
    <div class="product-wrapper-grid" :class="listViewEnable ? 'list-view' : ''">
        <div class="row">
            <div :class="[name ? 'col-xl-6 col-sm-6' : col3 ? 'col-xl-4 col-sm-4' : col4 ? 'col-xl-3 col-sm-3' : col6 ? 'col-xl-2' : listViewEnable ? 'col-xl-6 col-sm-6 col-xl-12' : '']"
                v-for="(product, index) in filterPage" :key="index">
                <div class="card">
                    <div class="product-box">
                        <div class="product-img">
                            <div class="ribbon ribbon-danger" v-if="product.sale">Sale</div>
                            <img class="img-fluid" :src="getImgUrl(product.images[0])" alt />
                            <div class="product-hover">
                                <ul>
                                    <router-link :to="'/ecommerce/cart'">
                                        <li @click="addToCart(product)">
                                            <i class="icon-shopping-cart"> </i>
                                        </li>
                                    </router-link>
                                    <li @click="quickView(product)" data-bs-toggle="modal"
                                        data-bs-target="#exampleModalCenter">
                                        <i class="icon-eye"> </i>
                                    </li>
                                    <li>
                                        <button class="btn" type="button"><i class="icofont icofont-law-alt-2"></i></button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="product-details">
                            <div class="rating"><i class="fa fa-star"></i><i class="fa fa-star"></i><i
                                    class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i></div>
                            <router-link :to="'/ecommerce/productPage/' + product.id">
                                <h4>{{ product.name }}</h4>
                            </router-link>
                            <p>{{ product.note }}</p>
                            <div class="product-price">
                                ${{ product.price }}
                                <del>${{ product.discountPrice }}</del>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenter"
        aria-hidden="true">
        <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <div class="product-box row">
                        <div class="product-img col-lg-6">
                            <img class="img-fluid" :src="getImgUrl(modalShow ? quickViewProduct.img : 'ecommerce/01.jpg')"
                                alt="">
                        </div>
                        <div class="product-details col-lg-6 text-start">
                            <h4>{{ quickViewProduct.name }}</h4>
                            <div class="product-price">${{ quickViewProduct.price }}
                                <del>{{ quickViewProduct.salePrice }}</del>
                            </div>
                            <div class="product-view">
                                <h6 class="f-w-600">Product Details</h6>
                                <p class="mb-0">{{ quickViewProduct.discription }}</p>
                            </div>
                            <div class="product-size">
                                <ul class="d-flex my-3">
                                    <li>
                                        <button class="btn btn-outline-light" type="button">M</button>
                                    </li>
                                    <li>
                                        <button class="btn btn-outline-light ms-1" type="button">L</button>
                                    </li>
                                    <li>
                                        <button class="btn btn-outline-light ms-1" type="button">Xl</button>
                                    </li>
                                </ul>
                            </div>
                            <div class="product-qnty">
                                <h6 class="f-w-600">Quantity</h6>
                                <fieldset>
                                    <div class="input-group bootstrap-touchspin mb-3">
                                        <button class=" btn btn-primary btn-square bootstrap-touchspin-down " type="button"
                                            data-bs-original-title="" title="" @click="decrement()">
                                            <i class="fa fa-minus"></i></button>
                                        <input class="touchspin1 text-center" v-model="counter" name="quantity"
                                            type="text" />
                                        <button class="btn btn-primary btn-square bootstrap-touchspin-up" type="button"
                                            data-bs-original-title="" title="" @click="increment()">
                                            <i class="fa fa-plus"></i>
                                        </button>
                                    </div>
                                </fieldset>
                                <div class="addcart-btn">
                                    <router-link to="/ecommerce/cart" class="btn btn-primary" data-bs-dismiss="modal"
                                        @click="addToCart(quickViewProduct, counter)">Add to Cart</router-link>
                                    <router-link :to="'/ecommerce/productPage'" class="btn btn-primary ms-2"
                                        data-bs-dismiss="modal">View Details</router-link>
                                </div>
                            </div>
                        </div>
                    </div>
                    <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import product from "@/mixin/commen/product"

export default {
    name: 'productView',
    mixins: [product],
}
</script>  