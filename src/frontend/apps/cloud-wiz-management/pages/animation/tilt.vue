<template>
  <Breadcrumbs main="Animation" title="Tilt" />

  <div class="container-fluid">
    <div class="row tilt-showcase">
      <div class="col-sm-12">
        <div class="card text-center">
          <div class="card-header">
            <h5>Parallax hover tilt effect </h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-6 offset-md-3">
                <pre :style="infoStyle"></pre>
                <div>
                  <img ref="target" :style="cardStyle" class="img-fluid img-thumbnail js-tilt"
                    src="/images/lightgallry/02.jpg" data-tilt-perspective="300" data-tilt-speed="400" data-tilt-max="5"
                    alt="">
                </div>

                <div>
                  <h6 class="sub-title mt-4 mb-0">The most basic usage:</h6>
                  <ul>
                    <li>
                      <div class="line"><code><span> &lt;script src="tilt.jquery.js"&gt;&lt;/script&gt;</span></code>
                      </div>
                    </li>
                    <li>
                      <div class="line">Mark your elements
                        with<code><span> &lt;span data-tilt"&gt;&lt;/span&gt;</span></code></div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>


<script setup>

import { useMediaQuery, useParallax, useMouseInElement } from '@vueuse/core'
import { computed, reactive, ref } from 'vue';
// import type { CSSProperties } from 'vue';
const target = ref(null)
const target1 = ref(null)

const isMobile = useMediaQuery('(max-width: 700px)')
const parallax = reactive(useParallax(target))
const parallax1 = reactive(useParallax(target1))
//  useMouseInElement({ handleOutside: false });
const infoStyle = computed(() => ({
  opacity: 0.4,
  //   top: '20px',
  //   left: '40px',
  position: isMobile.value ? 'inherit' : 'absolute',
}))
const cardStyle = computed(() => ({
  transition: '.1s ease-out all',
  transform: `rotateX(${parallax.roll * 50}deg) rotateY(${parallax.tilt * 50
    }deg)`,
}));
const cardStyle1 = computed(() => ({
  transition: '.1s ease-out all',
  transform: `rotateX(${parallax1.tilt * 50}deg) rotateY(${parallax1.roll * 50
    }deg)`,
}))


</script>

