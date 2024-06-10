<template>
  <div class="col-md-12 text-start">
    <div class="card">
      <div class="card-header">
        <h5 class="card-title">toastr with position</h5>
      </div>
      <div class="card-body btn-showcase">

        <button class="btn btn-primary" type="button" @click="top_right" variant="primary">Top Right</button>

        <button class="btn btn-primary" type="button" @click="top_left" variant="primary">Top Left</button>

        <button class="btn btn-primary" type="button" @click="top_center" variant="primary">Top Center</button>

        <button class="btn btn-primary" type="button" @click="bottom_right" variant="primary">Bottom Right</button>

        <button class="btn btn-primary" type="button" @click="bottom_left" variant="primary">Bottom Left</button>

        <button class="btn btn-primary" type="button" @click="bottom_center" variant="primary">Bottom Center</button>

        <button class="btn btn-primary" type="button" @click="full_width" variant="primary">Full Width</button>

      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    full_width() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success" })

    },
    top_right() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success" })

    },
    top_left() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success", position: 'top-left' })

    },
    top_center() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success", position: 'top-center' })

    },
    bottom_right() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success", position: 'bottom-right' })

    },
    bottom_left() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success", position: 'bottom-left' })

    },
    bottom_center() {
      useNuxtApp().$showToast({ msg: " New order has been placed ", type: "success", position: 'bottom-center' })

    },
  }
}
</script>