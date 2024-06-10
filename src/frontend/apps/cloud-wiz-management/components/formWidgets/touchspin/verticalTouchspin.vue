<template>
  <div class="col-sm-12 col-md-6 text-start">
    <div class="card">
      <div class="card-header">
        <h5 class="card-title">vertical Touchspin</h5>
        <span
          >Add <code>.touchspin-vertical</code> class for vertical touchspin
          input group.</span
        >
      </div>
      <div class="card-body">
        <fieldset>
          <div class="touchspin-vertical-tab">
            <div class="input-group bootstrap-touchspin">
              <input
                class="touchspin-vertical form-control"
                type="text"
                v-model="num2"
              />
              <span class="input-group-btn-vertical">
                <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num2--" > <i class="fa fa-angle-up"></i></button>
                 <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num2++" ><i class="fa fa-angle-down"></i></button>
                </span>
            </div>
          </div>
        </fieldset>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      num2: 55,
    };
  },
   watch:{
      num2:function(newValue){
        if(newValue >= 100) {
          this.num2 = 100;
        } else if(newValue <= 0) {
          this.num2 = 0;
        }
      },
     }
};
</script>