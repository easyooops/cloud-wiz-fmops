<template>
  <div class="col-lg-12 ">
    <div class="header-faq">
      <h5 class="mb-0">Quick Questions are answered</h5>
    </div>
    <div class="row default-according style-1 faq-accordion" id="accordionoc">
      <div class="col-xl-8 xl-60 col-lg-6 col-md-7">
        <div class="card">
          <div class="card-header">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon"
                aria-expanded="false" aria-controls="collapseicon" :class="[isActive ? 'active' : '', 'collapsible']"
                v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> Integrating WordPress with Your
                Website?</button>
            </h5>
          </div>
          <div class="collapse" id="collapseicon" aria-labelledby="collapseicon" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
              <p>How you approach this process will depend on which web host you use. For example, a lot of hosting
                providers use cPanel, which includes an option to set up subdomains with just a few clicks.</p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon2"
                aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']"
                v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress Site Maintenance ?</button>
            </h5>
          </div>
          <div class="collapse" id="collapseicon2" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
              <p>We’ve just published a detailed on how to backup your WordPress website, however, if you’re in a hurry,
                here’s a quick solution.</p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon3"
                aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']"
                v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>Meta Tags in WordPress ?</button>
            </h5>
          </div>
          <div class="collapse" id="collapseicon3" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
              <p>Manually adding meta tags in WordPress is relatively simple. For this demo, we’ll use the example from
                the WordPress Codex. Imagine you’re Harriet Smith, a veterinarian who blogs about their animal stories on
                WordPress.</p>
            </div>
          </div>
        </div>
        <div class="card">
          <div class="card-header">
            <h5 class="mb-0">
              <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon4"
                aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']"
                v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress in Your Language ?</button>
            </h5>
          </div>
          <div class="collapse" id="collapseicon4" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
              <p>As of version 4.0, you can have WordPress automatically install the language of your choice during the
                installation process.</p>
            </div>
          </div>
        </div>
        <intellectualProperty />
        <faq2 />
      </div>
      <navigation />
    </div>
  </div>
</template>
<script>
import faq2 from "./faq2Page.vue"
import navigation from "./navigationPage.vue"
import intellectualProperty from "./intellectualProperty.vue"
export default {
  components: { faq2, navigation, intellectualProperty },
  data() {
    return {
      isActive: false,
      lorem: "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
    }
  },
  methods: {
    toggle() {
      this.isActive = !this.isActive
    },
  }
}
</script>