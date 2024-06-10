<template>
  <div>
    <Breadcrumbs main="Icons" title="Feather Icons" />

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5 class="m-b-0">Feather Icons</h5>
            </div>
            <div class="card-body">
              <div class="row icon-lists feather-icons">
                <div class="col-12 col-sm-6 col-xl-4" v-for="(icon, index) in feather_icons" :key="index"
                  v-on:click="icon_bar(icon.abbrivation)">
                  <div class="media">
                    <vue-feather :type="icon.abbrivation"></vue-feather>
                    <div class="media-body align-self-center">
                      <h6 class="mt-0" v-text="icon.name"></h6>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="icon-hover-bottom p-fixed fa-fa-icon-show-div" :class="{ 'opecity-0': !icon_bar_status }"
      :style="[icon_bar_status ? { 'display': 'block' } : { 'display': 'none' }]">
      <div class="container-fluid">
        <div class="row">
          <div class="icon-popup">
            <div class="close-icon" v-on:click="close_icon_bar"><i class="icofont icofont-close"></i></div>
            <div class="icon-first">
              <vue-feather class="fa-2x" :type="select_icon.class"></vue-feather>
            </div>
            <div class="icon-class">
              <label class="icon-title">Class</label><span v-text="select_icon.class"></span>
            </div>
            <div class="icon-last icon-last">
              <label class="icon-title">Markup</label>
              <div class="form-inline">
                <div class="form-group">
                  <input class="inp-val form-control m-r-10" type="text" ref="text" :value="select_icon.tag"
                    readonly="readonly">
                  <button class="btn btn-primary notification" v-on:click="copy_icon">Copy text</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import iconMixin from "@/mixin/commen/iconMixin"
export default {
  mixins: [iconMixin],
  data() {
    return {
      customAnimation: {
        enter: "animated bounce",
        exit: "animated bounce",
      },
      icon_bar_status: false,
      select_icon: {
        class: 'home',
        tag: 'home'
      },
    };
  },
  methods: {
    icon_bar(icon) {
      this.select_icon.class = icon;
      this.select_icon.tag = '<vue-feather type="' + icon + '"></vue-feather>';
      this.icon_bar_status = true;
    },
    close_icon_bar() {
      this.icon_bar_status = false;
    },
    copy_icon() {
      this.$refs.text.select();
      document.execCommand('copy');
      useNuxtApp().$showToast({ msg: " Code Copied to clipboard ", type: "success", position: 'bottom-left' })
    }
  }
};
</script>
<style lang="scss" scoped>
@import "@/assets/scss/vendors/animate.scss";
</style>