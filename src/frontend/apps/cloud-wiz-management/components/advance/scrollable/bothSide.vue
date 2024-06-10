<template>
  <div class="col-sm-6 text-start">
    <div class="card">
      <div class="card-header">
        <h5>Both Side Scroll</h5>
      </div>
      <div class="card-body">
        <div class="scroll-bar-wrap">
          <perfect-scrollbar class="both-side-scroll scroll-demo p-0" v-once :settings="settings3">
            <div><img src="/images/banner/1.jpg" alt="girl" width="800" height="600"></div>
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
      settings3: {
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