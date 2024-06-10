<template>
  <div class="col-xl-6 xl-100 col-lg-12 box-col-12">
    <div class="card">
      <div class="card-header">
        <h3 class="pull-left">Material tab</h3>
      </div>
      <div class="card-body">
        <div class="tabbed-card">
          <ul class="pull-right nav nav-tabs border-tab nav-primary" id="top-tab" role="tablist">
            <li class="nav-item" v-on:click="changetab('timeline')"><a class="nav-link" :class="{ 'show active': showtab == 'timeline' }" id="top-home-tab" data-bs-toggle="tab" href="#top-home" role="tab" aria-controls="top-home" aria-selected="false">Home</a></li>
            <li class="nav-item" v-on:click="changetab('about')"><a class="nav-link" :class="{ 'show active': showtab == 'about' }" id="profile-top-tab" data-bs-toggle="tab" href="#top-profile" role="tab" aria-controls="top-profile" aria-selected="true">Profile</a></li>
            <li class="nav-item" v-on:click="changetab('friends')"><a class="nav-link" :class="{ 'show active': showtab == 'friends' }" id="contact-top-tab" data-bs-toggle="tab" href="#top-contact" role="tab" aria-controls="top-contact" aria-selected="false">Contact</a></li>
          </ul>
          <div class="tab-content" id="top-tabContent">
            <div class="tab-pane fade" :class="{'show active': showtab == 'timeline' }" id="top-home" role="tabpanel" aria-labelledby="top-home-tab">
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
            </div>
            <div class="tab-pane fade " :class="{'show active': showtab == 'about' }" id="top-profile" role="tabpanel" aria-labelledby="profile-top-tab">
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
            </div>
            <div class="tab-pane fade" :class="{'show active': showtab == 'friends' }" id="top-contact" role="tabpanel" aria-labelledby="contact-top-tab">
              <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>
<script>
export default {
    data(){
        return{
            showtab:'timeline',
        }
    },
    methods:{
          changetab(tab) {
        this.showtab = tab;
      }
    }
};
</script>