<template>
    <div>
      <Breadcrumbs main="" title="File Manager" />
      <div class="container-fluid">
        <div class="row">
            <div class="col-xl-3 box-col-6 pe-0">
                <div class="md-sidebar"><a class="btn btn-primary md-sidebar-toggle" href="javascript:void(0)" @click="collapse()">file filter</a>
                    <div class="md-sidebar-aside job-left-aside custom-scrollbar" :class="filtered?'open':''">
                        <fileFilterCardVue />
                    </div>
                </div>
            </div>
            <allFilesCardVue />
        </div>
    </div>
    </div>
  </template>
  <script>
import allFilesCardVue from './allFilesCard.vue'
import fileFilterCardVue from './fileFilterCard.vue'
  export default {
    components:{
      allFilesCardVue,
      fileFilterCardVue
    }
   
  }
  </script>