<template>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h3>Reversed Rating</h3>
            </div>
            <div class="card-body">
                <div class="rating-container">
                    <vue3-star-ratings v-model="rating"></vue3-star-ratings>
                    <pre class="mb-0 rating-pre">Rating {{ rating }}</pre>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h3>Star Rating</h3>
            </div>
            <div class="card-body">
                <div class="rating-container">
                    <vue3-star-ratings v-model="rating"></vue3-star-ratings>
                    <pre class="mb-0 rating-pre">Rating {{ rating }}</pre>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h3>Horizontal Rating</h3>
            </div>
            <div class="card-body height-equal">
                <div class="rating-container">
                    <vue3-star-ratings v-model="rating"></vue3-star-ratings>
                    <pre class="mb-0 rating-pre">Rating {{ rating }}</pre>
                </div>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card height-equal">
            <div class="card-header">
                <h3>Star Rating</h3>
            </div>
            <div class="card-body height-equal">
                <div class="rating-container">
                    <div class="star-ratings">
                        <div class="stars stars-example-fontawesome-o">
                            <vue3-star-ratings v-model="rating"></vue3-star-ratings>
                            <pre class="mb-0 rating-pre">Rating {{ rating }}</pre> <span class="title current-rating">Current
                                rating: <span class="value"></span></span><span class="title your-rating hidden">Your
                                rating:{{ rating }} <span class="value"></span><a class="clear-rating"
                                    href="javascript:void(0)"><i class="fa fa-times-circle"></i></a></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {

    data() {
        return {
            rating: "0",
            disabled: false
        }
    },

    mounted() {

    },
    methods: {
        currentRatingText() {

        }
    }
}
</script>