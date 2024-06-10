<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Basic Modal</h5>
            </div>
            <div class="card-body btn-showcase">

                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-original-title="test"
                    data-bs-target="#exampleModal">Simple</button>
                <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                    aria-hidden="true">
                    <Simple />
                </div>

                <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                    data-bs-target="#exampleModalLong">Scrolling long content</button>
                <div class="modal fade" id="exampleModalLong" tabindex="-1" role="dialog"
                    aria-labelledby="exampleModalLongTitle" aria-hidden="true">
                    <Scrollinglongcontent />
                </div>

                <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                    data-bs-target="#exampleModalCenter">Vertically centered</button>
                <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog"
                    aria-labelledby="exampleModalCenter" aria-hidden="true">
                    <Verticallycentered />
                </div>

                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#tooltipmodal">Tooltips
                    and popovers</button>
                <div class="modal fade" id="tooltipmodal" tabindex="-1" role="dialog" aria-labelledby="tooltipmodal"
                    aria-hidden="true">
                    <Tooltipsandpopovers />
                </div>

                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#grid-modal">Using the
                    grid</button>
                <div class="modal fade" id="grid-modal" tabindex="-1" role="dialog" aria-labelledby="grid-modal"
                    aria-hidden="true">
                    <Usingthegrid />
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>

import Simple from "../modal/Simple.vue"
import Scrollinglongcontent from "../modal/Scrollinglongcontent.vue"
import Verticallycentered from "../modal/Verticallycentered.vue";
import Tooltipsandpopovers from "../modal/Tooltipsandpopovers.vue"
import Usingthegrid from "../modal/Usingthegrid.vue"

export default {
    components: {
        Simple,
        Scrollinglongcontent,
        Verticallycentered,
        Tooltipsandpopovers,
        Usingthegrid
    }
}
</script>
    