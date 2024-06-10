<template>
  <div class="col-xl-12">
    <div class="card">
      <div class="card-header">
        <h5 class="mb-0">
          <button class="btn btn-link" data-bs-target="#collapseicon1" :aria-expanded="active1 ? 'false' : 'true'"
            aria-controls="collapseicon1" @click="showOpen1">Categories</button>
        </h5>
      </div>
      <div class="collapse card-body px-0 " :class="active1 ? '' : 'show'" id="collapseicon1" aria-labelledby="collapseicon1"
        data-bs-parent="#accordion">
        <div class="categories">
          <div class="learning-header"><span class="f-w-600">Design</span></div>
          <ul>
            <li><a href="#">UI Design </a><span class="badge badge-primary pull-right">28</span></li>
            <li><a href="#">UX Design </a><span class="badge badge-primary pull-right">35</span></li>
            <li><a href="#">Interface Design </a><span class="badge badge-primary pull-right">17</span></li>
            <li><a href="#">User Experience </a><span class="badge badge-primary pull-right">26</span></li>
          </ul>
        </div>
        <div class="categories pt-0">
          <div class="learning-header"><span class="f-w-600">Development</span></div>
          <ul>
            <li><a href="#">Frontend Development</a><span class="badge badge-primary pull-right">48</span></li>
            <li><a href="#">Backend Development</a><span class="badge badge-primary pull-right">19</span></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="col-xl-12">
    <div class="card">
      <div class="card-header">
        <h5 class="mb-0">
          <button class="btn btn-link" data-bs-target="#collapseicon2" :aria-expanded="active2 ? 'false' : 'true'"
            aria-controls="collapseicon2" @click="showOpen2">Upcoming Courses</button>
        </h5>
      </div>
      <div class="collapse " :class="active2 ? '' : 'show'" id="collapseicon2" aria-labelledby="collapseicon2"
        data-bs-parent="#accordion">
        <div class="upcoming-course card-body">
          <div class="media">
            <div class="media-body"><span class="f-w-600">UX Development</span><span class="d-block">Course By <a
                  href="#">Development Team</a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star-half-o font-warning"></i></span></div>
            <div>
              <h5 class="mb-0 font-primary">18</h5><span class="d-block">Dec</span>
            </div>
          </div>
          <div class="media">
            <div class="media-body"><span class="f-w-600">Business Analyst</span><span class="d-block">Course By <a
                  href="#">Analyst Team</a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i></span></div>
            <div>
              <h5 class="mb-0 font-primary">28</h5><span class="d-block">Dec</span>
            </div>
          </div>
          <div class="media">
            <div class="media-body"><span class="f-w-600">Web Development</span><span class="d-block">Course By <a
                  href="#">Designer
                </a></span><span class="d-block"><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star font-warning"></i><i
                  class="fa fa-star font-warning"></i><i class="fa fa-star-o font-warning"></i></span></div>
            <div>
              <h5 class="mb-0 font-primary">5</h5><span class="d-block">Jan</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {

  methods: {
    showOpen1() {
      this.active1 = !this.active1
    },
    showOpen2() {
      this.active2 = !this.active2
    },
  },
  data() {
    return {
      active1: false,
      active2: false,
    }
  }
}
</script>