<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Custom Table Color With Hover And Stripped</h3><span>Use class
          <code>table-hover, table-striped table-*table-info,table-success,table-success,table-info,table-danger,table-primary,table-secondary,table-light,table-active</code>
          inside table element.</span>
      </div>
      <div class="table-responsive">
        <table class="table table-striped bg-primary hover">
          <thead class="tbl-strip-thad-bdr">
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Film Title</th>
              <th scope="col">Released</th>
              <th scope="col">Studio</th>
              <th scope="col">Budget </th>
              <th scope="col">Domestic Gross</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in tableData2" :key="index">
              <th scope="row">{{ item.id }}</th>
              <td>{{ item.film }} </td>
              <td>{{ item.released }} </td>
              <td>{{ item.studio }} </td>
              <td>{{ item.budget }}</td>
              <td>{{ item.domestic }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Dashed Border </h3><span>Dashed border use class <code>.table-dashed</code> , for Dotted border use
          class<code>.table-dotted</code>, for Double border use class<code>.table-Double</code></span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-dashed">
              <thead>
                <tr>
                  <th scope="col">Id </th>
                  <th scope="col">Classname</th>
                  <th scope="col">Type</th>
                  <th scope="col">Hours</th>
                  <th scope="col">Trainer</th>
                  <th scope="col">Spots</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in tableData" :key="index">
                  <th scope="row">{{ item.id }}</th>
                  <td>{{ item.className }}</td>
                  <td>{{ item.type }}</td>
                  <td>{{ item.hours }} </td>
                  <td>{{ item.trainer }} </td>
                  <td>{{ item.spot }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import { useBootstrapStore } from "@/store/bootstrap"
import imageMixin from "@/mixin/commen/imageMixin"
export default {
  mixins: [imageMixin],
  data() {
    return {
      tableData: useBootstrapStore().tableData,
      tableData2: useBootstrapStore().tableData2
    }
  }
}
</script>  