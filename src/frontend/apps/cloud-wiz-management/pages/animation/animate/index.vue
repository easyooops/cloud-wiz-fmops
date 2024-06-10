<template>
  <Breadcrumbs main="Animation" title="Animate" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-body">
            <div class="row">
              <div class="col-xl-6 col-md-8 offset-xl-3 offset-md-2">
                <div id="animation-box" :class="show == enterAnimation ? enterClass : ''">
                  <div class="card">
                    <div class="animate-widget">
                      <div><img class="img-fluid" src="/images/banner/3.jpg" alt=""></div>
                      <div class="text-center p-25">
                        <p class="text-muted mb-0">Denouncing pleasure and praising pain was born and I will give you a
                          complete account of the system, and expound the actual teachings</p>
                      </div>
                    </div>
                  </div>
                </div>
                <form class="theme-form text-center">
                  <div class="mb-3">
                    <select class="form-select input input--dropdown js-animations"
                      @change="selectAnimate(enterAnimation)" v-model="enterAnimation">
                      <option v-for="(anim, index) in animationList" :value="anim" :key="index">{{ anim }}</option>
                    </select>
                  </div>
                  <button class="btn btn-primary" @click.prevent="selectAnimated(enterAnimation)">Animate it</button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h3>How to use it?</h3><span>All you have to do is to add animation name class attribute to html element, like
              :<code>Fade</code></span>
          </div>
          <div class="card-body options">
            <div v-for="index in animationList" :key="index">{{ index }}</div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import animationMixin from "@/mixin/commen/animationMixin"
export default {
  mixins: [animationMixin]

}
</script>