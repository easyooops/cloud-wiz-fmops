<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Hoverable Rows With Horizontal Border</h3><span>Hoverable row use a class <code>table-hover</code> and for
          Horizontal border use a class <code>.table-border-horizontal</code> , Solid border Use a
          class<code>.border-solid .table</code>class.</span>
      </div>
      <div class="table-responsive signal-table">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Status</th>
              <th scope="col">Signal Name </th>
              <th scope="col">Security</th>
              <th scope="col">Stage</th>
              <th scope="col">Schedule</th>
              <th scope="col">Team Lead</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in hover" :key="index">
              <th scope="row">{{ item.id }}</th>
              <td class="d-flex align-items-center"><span :class="item.font">{{ item.status }}</span></td>
              <td>{{ item.signalName }}</td>
              <td>{{ item.security }}</td>
              <td>{{ item.stage }}</td>
              <td>{{ item.schedule }} </td>
              <td>{{ item.teamLead }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Inverse Table with Primary background</h3><span>Use a class
          <code>.bg-info, .bg-success, .bg-warning and .bg-danger classes.</code> with light text on dark backgrounds
          inside table element.<br>To set the light background color use .bg-[color] class where [color] is the value of
          your selected color from stack color palette. So for teal color background class will be .bg-teal</span>
      </div>
      <div class="table-responsive">
        <table class="table table-striped bg-primary">
          <thead class="tbl-strip-thad-bdr">
            <tr>
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Company</th>
              <th scope="col">Credit Volume </th>
              <th scope="col">Username</th>
              <th scope="col">Role </th>
              <th scope="col">Country</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in bootstraplist" :key="index">
              <th scope="row">{{ item.id }}</th>
              <td>{{ item.firstName }}</td>
              <td>{{ item.lastName }}</td>
              <td>{{ item.company }} </td>
              <td>{{ item.credit }} </td>
              <td>{{ item.userName }} </td>
              <td>{{ item.role }}</td>
              <td>{{ item.country }}</td>
            </tr>
          </tbody>
        </table>
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
      hover: useBootstrapStore().hoverable,
      bootstraplist: useBootstrapStore().bootstrap
    }
  }
}
</script>     
