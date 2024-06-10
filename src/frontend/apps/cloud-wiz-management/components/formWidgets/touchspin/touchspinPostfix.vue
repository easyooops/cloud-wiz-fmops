<template>
     <div class="col-sm-12 col-md-6 text-start">
                  <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">Touchspin with Postfix</h5><span>Add <code>data-bts-postfix="POSTFIX_VALUE"</code> attribute to input to add postfix to touchspin input group.</span>
                    </div>
                    <div class="card-body">
                      <fieldset>
                        <div class="input-group">
                             <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num3--" ><i class="fa fa-minus"></i></button>
                          <input class="touchspin form-control" type="text" v-model="num3">
                          <span class="input-group-text">%</span>
                          <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num3++" ><i class="fa fa-plus"></i></button>
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
             num3:40,
        }
    },
     watch:{
      num3:function(newValue){
        if(newValue >= 100) {
          this.num3 = 100;
        } else if(newValue <= 0) {
          this.num3 = 0;
        }
      },
     }
}
</script>