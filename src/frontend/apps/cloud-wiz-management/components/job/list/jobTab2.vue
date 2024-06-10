<template>
  <div class="card">
    <div class="card-header" id="headingThree">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-start collapsed" type="button" data-bs-target="#collapseThree"
          :aria-expanded="active2 ? 'false' : 'true'" aria-controls="collapseThree" @click="showOpen2">Job Title</button>
      </h2>
    </div>
    <div class="collapse" :class="active2 ? '' : 'show'" id="collapseThree" aria-labelledby="headingThree"
      data-bs-parent="#accordionExample">
      <div class="card-body animate-chk">
        <label class="d-block" for="chk-ani11">
          <input class="checkbox_animated" id="chk-ani11" type="checkbox"> UI/Ux designer(25)
        </label>
        <label class="d-block" for="chk-ani12">
          <input class="checkbox_animated" id="chk-ani12" type="checkbox"> Graphic designer(10)
        </label>
        <label class="d-block" for="chk-ani13">
          <input class="checkbox_animated" id="chk-ani13" type="checkbox"> Front end designer(15)
        </label>
        <label class="d-block" for="chk-ani14">
          <input class="checkbox_animated" id="chk-ani14" type="checkbox"> PHP developer(42)
        </label>
        <label class="d-block mb-0" for="chk-ani15">
          <input class="checkbox_animated" id="chk-ani15" type="checkbox"> React Developer(5)
        </label>
      </div>
      <button class="btn btn-block btn-primary text-center" type="button">All Job Title</button>
    </div>
  </div>
  <div class="card">
    <div class="card-header" id="headingFour">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-start collapsed" type="button" data-bs-target="#collapseFour"
          :aria-expanded="active3 ? 'false' : 'true'" aria-controls="collapseFour" @click="showOpen3">Industry</button>
      </h2>
    </div>
    <div class="collapse" :class="active3 ? '' : 'show'" id="collapseFour" aria-labelledby="headingFour"
      data-bs-parent="#accordionExample">
      <div class="card-body animate-chk">
        <label class="d-block" for="chk-ani16">
          <input class="checkbox_animated" id="chk-ani16" type="checkbox"> Computer Software(14)
        </label>
        <label class="d-block" for="chk-ani17">
          <input class="checkbox_animated" id="chk-ani17" type="checkbox"> IT Engineer(10)
        </label>
        <label class="d-block" for="chk-ani18">
          <input class="checkbox_animated" id="chk-ani18" type="checkbox"> Service industry(20)
        </label>
        <label class="d-block" for="chk-ani19">
          <input class="checkbox_animated" id="chk-ani19" type="checkbox"> Accounting(34)
        </label>
        <label class="d-block mb-0" for="chk-ani20">
          <input class="checkbox_animated" id="chk-ani20" type="checkbox"> Financial Services(5)
        </label>
      </div>
      <button class="btn btn-block btn-primary text-center" type="button">All Industries</button>
    </div>
  </div>
  <jobTab3 />
</template>
<script>
import jobTab3 from "./jobTab3.vue"
export default {
  components: {
    jobTab3
  },
  methods: {
    showOpen2() {
      this.active2 = !this.active2
    },
    showOpen3() {
      this.active3 = !this.active3
    },
    showOpen4() {
      this.active4 = !this.active4
    },
  },
  data() {
    return {
      active2: false, active3: false, active4: false
    }
  }
}
</script>