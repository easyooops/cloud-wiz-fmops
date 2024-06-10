<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Responsive Tables With Light Background</h3><span>A <code>.table-responsive , .table-light</code> inside table
          element.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-light">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Task</th>
                  <th scope="col">Email</th>
                  <th scope="col">Phone</th>
                  <th scope="col">Assign</th>
                  <th scope="col">Date</th>
                  <th scope="col">Price </th>
                  <th scope="col">Status</th>
                  <th scope="col">Progress</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in Responsive" :key="index">
                  <th scope="row">{{ item.id }}</th>
                  <td>{{ item.task }} </td>
                  <td>{{ item.email }}</td>
                  <td>{{ item.phone }}</td>
                  <td>{{ item.assing }} </td>
                  <td>{{ item.date }}</td>
                  <td>{{ item.price }} </td>
                  <td :class="item.class">{{ item.status }}</td>
                  <td>{{ item.progress }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Sizing Tables</h3><span>Example of Extra large table, Add<code>.table-xl</code> class to
          the<code>.table</code> , Large table Add <code> .table-lg</code> , Default table Add <code>.table-de</code> ,
          Small table Add <code>.table-sm </code>, Extra Small table Add <code>.table-xs</code>to create a table.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-lg">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Employee Name</th>
                  <th scope="col">Date</th>
                  <th scope="col">Status</th>
                  <th scope="col">Hours</th>
                  <th scope="col">Performance</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in sizing" :key="index">
                  <th scope="row">{{ item.id }}</th>
                  <td>{{ item.Name }}</td>
                  <td>{{ item.Date }}</td>
                  <td :class="item.statusClass">{{ item.Status }}</td>
                  <td>{{ item.hours }}</td>
                  <td>{{ item.performance }}</td>
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
      sizing: useBootstrapStore().sizingTablesXl,
      Responsive: useBootstrapStore().Responsive
    }
  }
}
</script>  