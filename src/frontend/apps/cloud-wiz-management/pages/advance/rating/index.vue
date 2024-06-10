<template>
  <Breadcrumbs title="Rating" main="Bonus UI" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header">
            <h3><span>1/10</span> Rating</h3>
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
            <h3>Movie Rating</h3>
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
            <h3>Square Rating</h3>
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
            <h3>Pill Rating</h3>
          </div>
          <div class="card-body">
            <div class="rating-container">
              <vue3-star-ratings v-model="rating"></vue3-star-ratings>
              <pre class="mb-0 rating-pre">Rating {{ rating }}</pre>
            </div>
          </div>
        </div>
      </div>
      <ratingView />
    </div>
  </div>
</template>
<script>
import ratingView from "@/components/advance/rating/ratingView.vue"
export default {
  components: {
    ratingView
  },
  data() {
    return {
      rating: "0",
      disabled: false
    }
  },
  methods: {
  }
}
</script>