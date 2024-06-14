<template>
    <div>
      <Breadcrumbs main="" title="Agent Create" />
      <div class="container-fluid">
        <div class="row">
            <mainAgent />
        </div>
    </div>
    </div>
  </template>
  <script>
import mainAgent from './mainAgent.vue'
  export default {
    components:{
        mainAgent,
    }
   
  }
  </script>