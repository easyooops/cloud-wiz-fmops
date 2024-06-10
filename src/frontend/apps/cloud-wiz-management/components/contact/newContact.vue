<template>
    <li class="nav-item">
        <button class="badge-light-primary btn-block btn-mail w-100" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"><vue-feather class="me-2" type="users"></vue-feather> New Contacts</button>
        <Teleport to="body">
          <div class="modal fade modal-bookmark" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title" id="exampleModalLabel">Add Contact</h3>
                  <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <form class="form-bookmark needs-validation" id="bookmark-form" novalidate>
                    <div class="row g-2">
                      <div class="mb-3 col-md-12 mt-0">
                        <label for="con-name">Name</label>
                        <div class="row">
                          <div class="col-sm-6">
                            <input class="form-control" id="con-name" type="text" v-model="name" required placeholder="First Name" autocomplete="off">
                          </div>
                          <div class="col-sm-6">   
                            <input class="form-control" id="con-last" type="text" v-model="lastName" required placeholder="Last Name" autocomplete="off">
                          </div>
                        </div>
                      </div>
                      <div class="mb-3 col-md-12 mt-0">
                        <label for="con-mail">Email Address</label>
                        <input class="form-control" id="con-mail" type="email" v-model="email" required autocomplete="off">
                      </div>
                      <div class="mb-3 col-md-12 my-0">
                        <label for="con-phone">Phone</label>
                        <div class="row">
                          <div class="col-sm-6">
                            <input class="form-control" id="con-phone" type="tel" v-model="mobile" required autocomplete="off">
                          </div>
                          <div class="col-sm-6">
                            <select class="form-control" id="con-select">
                              <option>Mobile</option>
                              <option>Work</option>
                              <option>Others</option>
                            </select>
                          </div>
                        </div>
                      </div>
                    </div>
                    <input id="index_var" type="hidden" value="5">
                    <button class="btn btn-secondary" type="button"  @click="submitContact()">Save</button>
                    <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel</button>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </Teleport>

      </li>
</template>
<script>
import data from '@/data/contact.json'

export default {
  data(){
    return{
    name: '',
    lastName:'',
    email: '',
    mobile:'',
    menu: data.data
  }
},
methods:{
  submitContact(){
    var arr={
      activeTab: "8",
      img: "user/5.jpg",
      name: this.name,
      lastName : this.lastName,
      email: this.email,
      gender: "male",
      active:false,
      mobile:this.mobile
    }
    this.menu.push(arr)
  }
}
}
</script>