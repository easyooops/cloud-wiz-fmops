<template>
    <div class="col-sm-12 col-xl-6 xl-100">
        <div class="card">
          <div class="card-header">
            <h3>Tabs bottom left Align</h3>
          </div>
          <div class="card-body">
            <div class="tab-content" id="bottom-tabContent">
              <div class="tab-pane fade show active" id="bottom-home" role="tabpanel" aria-labelledby="bottom-home-tab">
                <p class="m-b-30">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
              </div>
              <div class="tab-pane fade" id="bottom-profile" role="tabpanel" aria-labelledby="profile-bottom-tab">
                <p class="m-b-30">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
              </div>
              <div class="tab-pane fade" id="bottom-contact" role="tabpanel" aria-labelledby="contact-bottom-tab">
                <p class="m-b-30">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
              </div>
            </div>
            <ul class="nav nav-tabs nav-bottom" id="bottom-tab" role="tablist">
              <li class="nav-item"><a class="nav-link active" id="bottom-home-tab" data-bs-toggle="tab" href="#bottom-home" role="tab" aria-controls="bottom-home" aria-selected="true"><i class="icofont icofont-ui-home"></i>Home</a></li>
              <li class="nav-item"><a class="nav-link" id="profile-bottom-tab" data-bs-toggle="tab" href="#bottom-profile" role="tab" aria-controls="profile-icon" aria-selected="false"><i class="icofont icofont-man-in-glasses"></i>Profile</a></li>
              <li class="nav-item"><a class="nav-link" id="contact-bottom-tab" data-bs-toggle="tab" href="#bottom-contact" role="tab" aria-controls="contact-icon" aria-selected="false"><i class="icofont icofont-contacts"></i>Contact</a></li>
            </ul>
          </div>
        </div>
      </div>
</template>
<script>
export default {
    
}
</script>