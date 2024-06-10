<template>
  <div class="col-xl-3 xl-40 box-col-12">
    <div class="md-sidebar">
      <a class="btn btn-primary email-aside-toggle md-sidebar-toggle" @click="isOpen">Job filter</a>
      <div class="md-sidebar-aside job-sidebar" :class="open ? 'open' : ''">
        <div class="default-according style-1 faq-accordion job-accordion">
          <div class="accordion" id="accordionExample">
            <jobfilter />
            <jobtab2 />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import jobtab2 from "./jobTab2.vue"
import jobfilter from "./jobfilter.vue"
export default {
  components: {
    jobtab2, jobfilter
  },
  methods: {
    isOpen() {
      this.open = !this.open
    },
    showOpen() {
      this.active = !this.active
    },
    showOpen1() {
      this.active1 = !this.active1
    },
  },
  data() {
    return {
      open: false,
      active: false,
      active1: false,
    }
  }
}
</script>