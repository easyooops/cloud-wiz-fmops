<template>
    <Breadcrumbs main="Animation" title="Scroll" />

    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h3>Scroll Reveal Example</h3>
                    </div>
                    <div class="card-body">
                        <div class="row gallery my-gallery" id="aniimated-thumbnials" itemscope="">
                            <figure class="reveal col-xl-3 col-sm-6 box-col-33" v-for="(item, index) in img" :key="index">
                                <ClientOnly>
                                    <img v-animate-onscroll.repeat="{ down: 'animated zoomInUp', up: 'animated rotateOut' }"
                                        class="img-thumbnail" @click="() => showImg(index)" :src="getImgUrl(item.image)"
                                        itemprop="thumbnail" alt="Image description">
                                </ClientOnly>
                                <!-- <figcaption itemprop="caption description">Image caption {{index+1}}</figcaption> -->
                            </figure>
                        </div>
                        <vue-easy-lightbox :visible="visible" :index="index" :imgs="lightBoxImages" @hide="handleHide">
                        </vue-easy-lightbox>
                    </div>
                </div>
                <scrollReveal />
            </div>
        </div>
    </div>
</template>
<script>
import scrollReveal from "@/components/animation/scroll/scrollReveal.vue"
export default {
    components: { scrollReveal },
    data() {
        return {
            lightBoxImages: [],
            visible: false,
            index: '',
            img: [{ image: "01.jpg" },
            { image: "02.jpg" },
            { image: "03.jpg" },
            { image: "04.jpg" },
            { image: "05.jpg" },
            { image: "06.jpg" },
            { image: "07.jpg" },
            { image: "08.jpg" },
            { image: "09.jpg" },
            { image: "010.jpg" },
            { image: "011.jpg" },
            { image: "012.jpg" },
            { image: "013.jpg" },
            { image: "014.jpg" },
            { image: "015.jpg" },
            { image: "016.jpg" },
            { image: "01.jpg" },
            { image: "02.jpg" },
            { image: "03.jpg" },
            { image: "04.jpg" },
            { image: "05.jpg" },
            { image: "010.jpg" },
            { image: "011.jpg" },
            { image: "012.jpg" },
            ]
        }
    },
    methods: {
        showImg(index) {
            this.index = index
            this.visible = true
        },
        handleHide() {
            this.visible = false
        },
        getImgUrl(path) {
            return ('/images/lightgallry/' + path)
        }
    },
    mounted() {
        this.img.forEach(item => {
            this.lightBoxImages.push(('/images/lightgallry/' + item.image))
        })
    }
}
</script>
