<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Basic Table With Border Bottom Color</h3><span>Use a class<code>table</code> to any table, and
          <code>.border-bottom-*</code>class for Border bottom color</span>
      </div>
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr class="border-bottom-primary">
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Username</th>
              <th scope="col">Designation</th>
              <th scope="col">Company</th>
              <th scope="col">Language</th>
              <th scope="col">Country</th>
            </tr>
          </thead>
          <tbody>
            <tr :class="item.borderColor" v-for="(item, index) in bootstraplist" :key="index">
              <th scope="row">{{ item.id }}</th>
              <td> <img class="img-30 me-2" :src="getImageUrl(item.img)" alt="profile">{{ item.firstName }}</td>
              <td>{{ item.lastName }}</td>
              <td>{{ item.userName }}</td>
              <td>{{ item.role }}</td>
              <td>{{ item.company }}</td>
              <td> <span class="badge " :class="item.badgeClass">{{ item.language }}</span></td>
              <td>{{ item.country }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Inverse Table</h3><span>Use a class <code>table-inverse</code> inside table element.</span>
      </div>
      <div class="table-responsive">
        <table class="table table-inverse">
          <thead>
            <tr class="border-bottom-light">
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Office</th>
              <th scope="col">Position</th>
              <th scope="col">Salary</th>
              <th scope="col">Join Date </th>
              <th scope="col">Age</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in inverselist" :key="index">
              <th scope="row">{{ item.id }}</th>
              <td>{{ item.firstName }}</td>
              <td>{{ item.lastName }}</td>
              <td>{{ item.office }}</td>
              <td>{{ item.role }}</td>
              <td>{{ item.salary }}</td>
              <td>{{ item.join }} </td>
              <td>{{ item.age }} </td>
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
      bootstraplist: useBootstrapStore().bootstrap,
      inverselist: useBootstrapStore().inverse
    }
  }
}
</script>