<template>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5>Varying modal content</h5>
            </div>
            <div class="card-body btn-showcase">
                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModalfat"
                    data-whatever="@mdo">Open modal for @mdo</button>
                <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModalmdo"
                    data-whatever="@fat">Open modal for @fat</button>
                <button class="btn btn-primary" type="button" data-bs-toggle="modal"
                    data-bs-target="#exampleModalgetbootstrap" data-whatever="@getbootstrap">Open modal for
                    @getbootstrap</button>
                <div class="modal fade" id="exampleModalfat" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                    aria-hidden="true">
                    <Modalfat />
                </div>
                <div class="modal fade" id="exampleModalmdo" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                    aria-hidden="true">
                    <Modalmdo />
                </div>
                <div class="modal fade" id="exampleModalgetbootstrap" tabindex="-1" role="dialog"
                    aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <Modalgetbootstrap />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import Modalmdo from "../modal/Modalmdo.vue"
import Modalfat from "../modal/Modalfat.vue"
import Modalgetbootstrap from "../modal/Modalgetbootstrap.vue"
export default {
    components: {
        Modalmdo,
        Modalfat,
        Modalgetbootstrap,
    }
}
</script>