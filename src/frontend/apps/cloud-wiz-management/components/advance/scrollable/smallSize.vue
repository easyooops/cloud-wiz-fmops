<template>
  <div class="col-sm-6 text-start">
    <div class="card">
      <div class="card-header">
        <h5>Small Size Scroll</h5>
      </div>
      <div class="card-body">
        <div class="scroll-bar-wrap">

          <perfect-scrollbar class="scrollbar-margins large-margin scroll-demo p-0" v-once :settings="settings">
            <img src="/images/banner/3.jpg" alt="girl" width="800" height="600">
          </perfect-scrollbar>

        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      settings: {
        maxScrollbarLength: 60
      },
    }
  }
}
</script>
<style scoped>
.ps {
  height: 300px;
}
</style>