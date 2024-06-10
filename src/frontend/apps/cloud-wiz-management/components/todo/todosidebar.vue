<template>
  <div class="col-xl-3 xl-30 box-col-12">
    <div class="email-sidebar md-sidebar"><a class="btn btn-primary email-aside-toggle md-sidebar-toggle"
        @click="collapseFilter()">To Do filter</a>
      <div class="email-left-aside md-sidebar-aside" :class="filtered ? 'open' : ''">
        <div class="card">
          <div class="card-body">
            <div class="email-app-sidebar left-bookmark custom-scrollbar">
              <div class="d-flex align-items-center">
                <div class="media-size-email"><img class="me-3 img-40 rounded-circle" src="/images/user/user.png" alt="">
                </div>
                <div class="flex-grow-1">
                  <h6 class="f-w-600">Mark Jecno</h6>
                  <p>Markjecno@gmail.com</p>
                </div>
              </div>
              <ul class="nav main-menu">
                <li class="nav-item">
                  <newTodo />
                </li>
                <li class="nav-item"> <a href="javascript:void(0)"><span class="iconbg badge-light-primary"><vue-feather
                        type="file-plus"></vue-feather></span><span class="title ms-2">All Task</span></a></li>
                <li class="nav-item"><a href="javascript:void(0)"><span class="iconbg badge-light-success"><vue-feather
                        type="check-circle"></vue-feather></span><span class="title ms-2">Completed</span><span
                      class="badge rounded-pill badge-success">3</span></a></li>
                <li class="nav-item"><a href="javascript:void(0)"><span class="iconbg badge-light-danger"><vue-feather
                        type="cast"></vue-feather></span><span class="title ms-2">Pending</span><span
                      class="badge rounded-pill badge-danger">2</span></a></li>
                <li class="nav-item"><a href="javascript:void(0)"><span class="iconbg badge-light-info"><vue-feather
                        type="activity"></vue-feather></span><span class="title ms-2">In Process</span><span
                      class="badge rounded-pill badge-primary">2</span></a></li>
                <li class="nav-item"><a href="javascript:void(0)"><span class="iconbg badge-light-danger"> <vue-feather
                        type="trash"></vue-feather></span><span class="title ms-2">Trash</span></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import newTodo from "./newTodo.vue"
export default {
  components: {
    newTodo
  },
  data() {
    return {
      filtered: false,
    };
  },
  methods: {
    collapseFilter() {
      this.filtered = !this.filtered;
    },
  }
}
</script>