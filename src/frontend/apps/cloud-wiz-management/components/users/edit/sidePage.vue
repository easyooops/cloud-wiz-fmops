<template>
  <div class="col-xl-4">
    <div class="card">
      <div class="card-header ">
        <h2 class="card-title mb-0">My Profile</h2>
        <div class="card-options"><a class="card-options-collapse" href="javascript:void(0)"
            data-bs-toggle="card-collapse"><i class="fe fe-chevron-up"></i></a><a class="card-options-remove"
            href="javascript:void(0)" data-bs-toggle="card-remove"><i class="fe fe-x"></i></a></div>
      </div>
      <div class="card-body">
        <form>
          <div class="row mb-2">
            <div class="profile-title">
              <div class="media"><img class="img-70 rounded-circle" alt="" src="/images/user/7.jpg">
                <div class="media-body"><router-link to="/users/profile">
                    <h5 class="mb-1 ">MARK JECNO</h5>
                  </router-link>
                  <p>DESIGNER</p>
                </div>
              </div>
            </div>
          </div>
          <div class="mb-3">
            <h4 class="form-label">Bio</h4>
            <textarea class="form-control" rows="5">On the other hand, we denounce with righteous indignation</textarea>
          </div>
          <div class="mb-3">
            <label class="form-label">Email-Address</label>
            <input class="form-control" placeholder="your-email@domain.com">
          </div>
          <div class="mb-3">
            <label class="form-label">Password</label>
            <input class="form-control" type="password" value="password">
          </div>
          <div class="mb-3">
            <label class="form-label">Website</label>
            <input class="form-control" placeholder="http://Uplor .com">
          </div>
          <div class="form-footer">
            <button class="btn btn-primary btn-block">Save</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'sidePage'
}
</script>