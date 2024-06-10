<template>
    <div class="col-sm-12 col-md-6 text-start">
                  <div class="card">
                    <div class="card-header">
 <h5 class="card-title">Touchspin mousewheel Disable</h5><span>Add <code>.touchspin-stop-mousewheel</code> class to diable mousewheel.</span>
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
               
    <div class="col-sm-12 col-md-6 text-start">
                  <div class="card">
                    <div class="card-header">
<h5 class="card-title">Small Horizontal Touchspin</h5><span>Add <code>.input-group-sm</code> class to input-group.</span>
                    </div>
                    <div class="card-body">
                      <fieldset>
                        <div class="input-group">
                           <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num9--" ><i class="fa fa-minus"></i></button>

                          <input class="touchspin form-control" type="text" v-model="num9">

                          <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num9++" ><i class="fa fa-plus"></i></button>
                           
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
             num9:60
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
      num9:function(newValue){
        if(newValue >= 100) {
          this.num9 = 100;
        } else if(newValue <= 0) {
          this.num9 = 0;
        }
      },
     }
}
</script>