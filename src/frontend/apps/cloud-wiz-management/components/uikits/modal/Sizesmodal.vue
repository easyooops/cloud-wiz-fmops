<template>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5>Sizes modal</h5>
            </div>
            <div class="card-body btn-showcase">

                <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                    data-bs-target=".bd-example-modal-lg">Large modal</button>
                <div class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel"
                    aria-hidden="true">
                    <Largemodal />
                </div>

                <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                    data-bs-target=".bd-example-modal-sm">Small modal</button>
                <div class="modal fade bd-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel"
                    aria-hidden="true">
                    <smallModel />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Largemodal from "../modal/Largemodal.vue"
import smallModel from "../modal/smallModel.vue"
export default {
    components: {
        Largemodal,
        smallModel,
    }
}
</script>