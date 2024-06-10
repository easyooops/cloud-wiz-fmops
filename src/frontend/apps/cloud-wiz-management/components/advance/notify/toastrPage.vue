<template>
     <div class="col-md-12 text-start">
                <div class="card">
                    <div class="card-header">
                      <h5 class="card-title">toastr</h5>
                    </div>
                    <div class="card-body btn-showcase">
                      
                      <button class="btn btn-success " type="button" @click="success" variant="success">Success</button>
                      
                      <button class="btn btn-info " type="button" @click="info" variant="info">Info</button>

                      <button class="btn btn-danger " type="button" @click="error" variant="danger">Error</button>

                    </div>
                </div>
              </div>
</template>
<script>
export default {
    methods:{
        success() {
                useNuxtApp().$showToast({msg:" New order has been placed ",type:"success"})
      },
      info() {
        useNuxtApp().$showToast({msg:" New order has been placed ",type:"info"})
      },
      error() {
        useNuxtApp().$showToast({msg:" New order has been placed ",type:"error"})
      },
    }
}
</script>