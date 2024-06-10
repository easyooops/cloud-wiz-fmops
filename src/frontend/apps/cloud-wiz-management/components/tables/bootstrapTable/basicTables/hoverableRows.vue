<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Caption</h3><span>A <code>&lt;caption&gt;</code> functions like a heading for a table. It helps users with
          screen readers to find a table and understand what it’s about and decide if they want to read it.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table">
              <caption>List of users</caption>
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Employee Name </th>
                  <th scope="col">Email</th>
                  <th scope="col">Experience</th>
                  <th scope="col">Sex</th>
                  <th scope="col">Contact No. </th>
                  <th scope="col">Age</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in table" :key="index">
                  <th scope="row">{{ item.id }}</th>
                  <td>{{ item.name }} </td>
                  <td>{{ item.email }} </td>
                  <td>{{ item.exp }} </td>
                  <td>{{ item.sex }} </td>
                  <td>{{ item.contact }}</td>
                  <td>{{ item.age }} </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-header">
        <h3>Table head options</h3><span>Similar to tables , use the modifier classes<code>.table-[color]</code> to make
          <code>thead</code>appear in any color.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table">
              <thead class="table-dark">
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">First Name</th>
                  <th scope="col">Last Name</th>
                  <th scope="col">Username</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in table" :key="index">
                  <th scope="row">{{ item.id }}</th>
                  <td>{{ item.firstName }}</td>
                  <td>{{ item.lastName }}</td>
                  <td>{{ item.username }}</td>
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
export default {
  data() {
    return {
      table: useBootstrapStore().table
    }
  }
}
</script>