<template>
     <div class="col-md-12 text-start">
                <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">toastr with icon</h5>
                    </div>
                    <div class="card-body btn-showcase">
                      
                      <button class="btn btn-success " type="button" @click="success_with_icon" variant="success">Success</button>
                      
                      <button class="btn btn-info " type="button" @click="info_with_icon" variant="info">Info</button>

                      <button class="btn btn-danger " type="button" @click="error_with_icon" variant="danger">Error</button>

                      <button class="btn btn-info " type="button" @click="info_with_cancle" variant="info">Cancle</button>

                    </div>
                </div>
              </div>
</template>
<script>
export default {
    methods:{
         success_with_icon() {
          useNuxtApp().$showToast({msg:" New order has been placed ",type:"success",icon: 'fa fa-check'})
      },
      info_with_icon() {
        useNuxtApp().$showToast({msg:" New order has been placed ",type:"info",icon: 'fa fa-info'})
      },
      error_with_icon() {
        useNuxtApp().$showToast({msg:" New order has been placed ",type:"error",icon: 'fa fa-times'})
      },
       info_with_cancle() {
        useNuxtApp().$showToast({msg:" New order has been placed ",type:"success",position:'bottom-right'})
      }
    }
}
</script>