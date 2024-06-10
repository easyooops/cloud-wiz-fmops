<template>
    <div class="col-sm-12 col-md-6 text-start">
                  <div class="card">
                    <div class="card-header">
<h5 class="card-title">Min Max Value of Touchspin</h5><span>Use <code>data-bts-min="VALUE" data-bts-max="VALUE"</code> attribute to input to set min and max value of touchspin input.</span>
                    </div>
                    <div class="card-body">
                      <fieldset>
                        <div class="input-group">
                           <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num5--" ><i class="fa fa-minus"></i></button>

                          <input class="touchspin form-control" type="text" v-model="num5">

                          <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num5++" ><i class="fa fa-plus"></i></button>
                           
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
             num5:40,
        }
    },
     watch:{
      num5:function(newValue){
        if(newValue >= 100) {
          this.num5 = 100;
        } else if(newValue <= 0) {
          this.num5 = 0;
        }
      },
     }
}
</script>