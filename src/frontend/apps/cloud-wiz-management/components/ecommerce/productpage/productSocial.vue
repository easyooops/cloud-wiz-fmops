<template>
    <div>
        <table class="product-page-width">
            <tbody>
                <tr>
                    <td> <b>Brand &nbsp;&nbsp;&nbsp;:</b></td>
                    <td>Pixelstrap</td>
                </tr>
                <tr>
                    <td> <b>Availability &nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b></td>
                    <td class="txt-success">In stock</td>
                </tr>
                <tr>
                    <td> <b>Seller &nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b></td>
                    <td>ABC</td>
                </tr>
                <tr>
                    <td> <b>Fabric &nbsp;&nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b></td>
                    <td>Cotton</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="col-md-6">
        <table>
            <tbody>
                <tr>
                    <td> <b>Seller &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;:
                            &nbsp;&nbsp;&nbsp;</b></td>
                    <td>ABC</td>
                </tr>
                <tr>
                    <td> <b>Fabric &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;: &nbsp;&nbsp;&nbsp;</b>
                    </td>
                    <td>Cotton </td>
                </tr>
            </tbody>
        </table>
    </div>
    <hr>
    <div class="row">
        <div class="col-md-4">
            <h4 class="product-title">share it</h4>
        </div>
        <div class="col-md-8">
            <div class="product-icon">
                <ul class="product-social">
                    <li class="d-inline-block"><a href="https://www.facebook.com" target="_blank"><i
                                class="fa fa-facebook"></i></a></li>
                    <li class="d-inline-block"><a href="https://www.google.com/" target="_blank"><i
                                class="fa fa-google-plus"></i></a></li>
                    <li class="d-inline-block"><a href="https://twitter.com/" target="_blank"><i
                                class="fa fa-twitter"></i></a></li>
                    <li class="d-inline-block"><a href="https://www.instagram.com/" target="_blank"><i
                                class="fa fa-instagram"> </i></a></li>
                    <li class="d-inline-block"><a href="https://rss.app/" target="_blank"><i class="fa fa-rss"></i></a>
                    </li>

                </ul>
                <form class="d-inline-block f-right"> </form>
            </div>
        </div>
    </div>
    <hr>
    <div class="row">
        <div class="col-md-4">
            <h6 class="product-title">Rate Now</h6>
        </div>
        <div class="col-md-8">
            <div class="d-flex">
                <ul class="rating d-flex">
                    <li v-for="i in 5" :key="i">
                        <vue-feather type="star" class="fill" :style="
                            i <= selectedStars
                                ? { color: 'yellow' }
                                : { color: 'black' }
                        " @click="filled(i)"></vue-feather>
                    </li>
                </ul><span>(250 review)</span>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            rating: 1,
            selectedStars: 0,
        }
    },
    methods: {
        filled(len) {
            this.selectedStars = len;
        },
    }
}
</script>