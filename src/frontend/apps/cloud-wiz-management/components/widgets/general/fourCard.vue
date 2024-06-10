<template>
    <div class="col-sm-6 col-xl-3 col-lg-6 box-col-6" v-for="puechaseSales in puechaseSalesDetails" :key="puechaseSales">
        <div class="row">
            <div class="col-xl-12">
                <div class="card widget-1">
                    <div class="card-body">
                        <div class="widget-content">
                            <div :class="puechaseSales.widgetClass">
                                <div class="bg-round">
                                    <svg class="svg-fill">
                                        <use :xlink:href="getImgURL(puechaseSales.svgIcon1)"></use>
                                    </svg>
                                    <svg class="half-circle svg-fill">
                                        <use :xlink:href="getImgURL(puechaseSales.svgIcon2)"></use>
                                    </svg>
                                </div>
                            </div>
                            <div>
                                <h4>{{ puechaseSales.number }}</h4>
                                <span class="f-light">
                                    {{ puechaseSales.title }}
                                </span>
                            </div>
                        </div>
                        <div :class="puechaseSales.growthClass">
                            <i :class="puechaseSales.iconClass"></i><span>{{ puechaseSales.growthNumber }}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import {
    puechaseSalesDetails,

} from "@/data/widgets/general.json"
export default {
    data() {
        return {
            puechaseSalesDetails: puechaseSalesDetails,

        }
    },
    methods: {
        getImgURL(path) {
            return '/svg/icon-sprite.svg/' + `#${path}`
        }
    },
}
</script>
  