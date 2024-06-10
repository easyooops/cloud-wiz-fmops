<template>
    <div class="card">
        <div class="card-header" id="headingFive">
            <h2 class="mb-0">
                <button class="btn btn-link btn-block text-start collapsed" type="button" data-bs-target="#collapseFive"
                    :aria-expanded="active4 ? 'false' : 'true'" aria-controls="collapseFive" @click="showOpen4">Specific
                    skills</button>
            </h2>
        </div>
        <div class="collapse" :class="active4 ? '' : 'show'" id="collapseFive" aria-labelledby="headingFive"
            data-bs-parent="#accordionExample">
            <div class="card-body animate-chk">
                <label class="d-block" for="chk-ani21">
                    <input class="checkbox_animated" id="chk-ani21" type="checkbox"> HTML,scss & sass
                </label>
                <label class="d-block" for="chk-ani22">
                    <input class="checkbox_animated" id="chk-ani22" type="checkbox"> Javascript
                </label>
                <label class="d-block" for="chk-ani23">
                    <input class="checkbox_animated" id="chk-ani23" type="checkbox"> Node.js
                </label>
                <label class="d-block" for="chk-ani24">
                    <input class="checkbox_animated" id="chk-ani24" type="checkbox"> Gulp & Pug
                </label>
                <label class="d-block mb-0" for="chk-ani25">
                    <input class="checkbox_animated" id="chk-ani25" type="checkbox"> Angular.js
                </label>
            </div>
            <button class="btn btn-block btn-primary text-center" type="button">All Skills </button>
        </div>
    </div>
</template>
<script>

export default {
    methods: {

        showOpen4() {
            this.active4 = !this.active4
        },
    },
    data() {
        return {
            active4: false
        }
    }
}
</script>