<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="table-responsive signal-table">
        <table class="table table-hover s-15">
          <colgroup>
            <col width="10%" />
            <col width="17%" />
            <col width="*" />
          </colgroup>
          <thead>
            <tr>
              <th scope="col">Level</th>
              <th scope="col">Date</th>
              <th scope="col">Sucject</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in statusHistory" :key="index" :class="{'error-row': item.level === 'Error'}">
              <td class="align-items-center"><span :class="item.font"><b>{{ item.level }}</b></span></td>
              <td>{{ item.date }}</td>
              <td>{{ item.subject }}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <br/>
      <nav aria-label="Page navigation example">
        <ul class="pagination pagination-primary justify-content-center ">
          <li class="page-item"><a class="page-link" href="javascript:void(0)" aria-label="Previous"><span aria-hidden="true">«</span><span class="sr-only">Previous</span></a></li>
          <li class="page-item"><a class="page-link" href="javascript:void(0)">1</a></li>
          <li class="page-item"><a class="page-link" href="javascript:void(0)">2</a></li>
          <li class="page-item"><a class="page-link" href="javascript:void(0)">3</a></li>
          <li class="page-item"><a class="page-link" href="javascript:void(0)" aria-label="Next"><span aria-hidden="true">»</span><span class="sr-only">Next</span></a></li>
        </ul>
      </nav>
    </div>
  </div>
</template>
<script>

import { useBootstrapStore } from "~/store//bootstrap"
import imageMixin from "~/mixin/commen/imageMixin"
export default {
  mixins: [imageMixin],
  data() {
    return {
      statusHistory: useBootstrapStore().statusHistory,
      bootstraplist: useBootstrapStore().bootstrap
    }
  }
}
</script>
<style>

.error-row {
  --bs-table-bg: #ff00001c;
}

</style>
