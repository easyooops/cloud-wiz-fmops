<template>
    <li><a href="javascript:void(0)" @click="history()">History</a>
    <div id="right-history" :class="active ? 'show':''">
        <div class="modal-header p-l-20 p-r-20">
          <h4 class="modal-title w-100">Contact History<span class="pull-right"><a class="closehistory" href="javascript:void(0)"><i class="icofont icofont-close" @click="history()" ></i></a></span></h4>
        </div>
        <div class="history-details">
          <div class="text-center"><i class="icofont icofont-ui-edit"></i>
            <p>Contact has not been modified yet.</p>
          </div>
          <div class="d-flex"><i class="icofont icofont-star me-3"></i>
            <div class="flex-grow-1 mt-0">
              <h6 class="mt-0">Contact Created</h6>
              <p class="mb-0">Contact is created via mail</p><span class="f-12">Sep 10, 2019 4:00</span>
            </div>
          </div>
        </div>
      </div>
    </li>
</template>
<script>
export default{
    name: 'historyPage',
    data(){
        return{
            active:false
        }
    },
    methods:{
        history(){
            this.active=!this.active
        }
    }
}
</script>