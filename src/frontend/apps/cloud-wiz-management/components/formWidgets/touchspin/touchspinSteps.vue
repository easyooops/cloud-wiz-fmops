<template>
    <div class="col-sm-12 col-md-6 text-start">
                  <div class="card">
                    <div class="card-header">
<h5 class="card-title">Touchspin steps</h5><span>Add <code>data-bts-step="VALUE"</code> attribute for increament and decrement steps to touchspin input group.</span>
                    </div>
                    <div class="card-body">
                      <fieldset>
                        <div class="input-group">
                           <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num7--" ><i class="fa fa-minus"></i></button>

                          <input class="touchspin form-control" type="text" v-model="num7">

                          <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num7++" ><i class="fa fa-plus"></i></button>
                           
                        </div>
                      </fieldset>
                    </div>
                  </div>
                </div>
</template>
<script>
export default {
    data(){
        return{
             num7:40,
        }
    },
     watch:{
      num7:function(newValue){
        if(newValue >= 100) {
          this.num7 = 100;
        } else if(newValue <= 0) {
          this.num7 = 0;
        }
      },
     }
}
</script>