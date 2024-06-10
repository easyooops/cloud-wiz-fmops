<template>
  <section id="hero-15" class="bg--scroll hero-section">
      <div class="container">
          <div class="row d-flex align-items-center">
              <!-- HERO TEXT -->
              <div class="col-md-6">
                  <div class="hero-15-txt wow fadeInRight">
                      <!-- Title -->
                      <h2 class="s-55 w-700">Innovate with Our LLM Cloud Platform</h2>
                      <!-- Text -->
                      <p class="p-lg">Experience an innovative cloud solution that allows you to easily create chains and seamlessly apply customized agents across various industries</p>
                      <!-- Button -->
                      <a :href="baseUrl" class="btn r-04 btn--theme hover--tra-black">Get started for free</a>
                      <p class="p-sm btn-txt ico-15"><span class="flaticon-check"></span> No credit card needed, free 14-day trial</p>
                  </div>
              </div>
              <!-- END HERO TEXT -->
              <!-- HERO IMAGE -->
              <div class="col-md-6">
                  <div class="hero-15-img text-center wow fadeInLeft">
                      <img class="img-fluid" src="/assets/images/hero-15-img.png" alt="hero-image" />
                  </div>
              </div>
          </div>
          <!-- End row -->
      </div>
      <!-- End container -->
  </section>
</template>

<script setup lang="ts">

import { ref, onMounted, onBeforeUnmount, watch } from 'vue'

const baseUrl = import.meta.env.VITE_MANAGEMENT_URL || '/';

// const scrollSections = ref([])
// const currentSectionIndex = ref(0)
//
// const scrollToSection = (index) => {
//   if (index >= 0 && index < scrollSections.value.length) {
//     let totalOffset = 0;
//
//     // 현재 섹션까지의 높이 누적 계산
//     for (let i = 0; i < index; i++) {
//       totalOffset += scrollSections.value[i].offsetHeight;
//     }
//
//     window.scrollTo({ top: totalOffset, behavior: 'smooth' });
//     console.log('이동');
//   }
// }
//
// const handleScroll = () => {
//   const windowHeight = window.innerHeight
//
//   // 현재 보이는 섹션 감지
//   for (let i = 0 ; i < scrollSections.value.length ; i++) {
//     const section = scrollSections.value[i]
//     const sectionTop = section.getBoundingClientRect().top
//
//     if (sectionTop >= 0 && sectionTop < windowHeight / 2) {
//       currentSectionIndex.value = i
//       break
//     }
//   }
// }


// onMounted(() => {
//   scrollSections.value = Array.from(document.querySelectorAll('._scrollto'))
//   window.addEventListener('scroll', handleScroll)
// })
//
// onBeforeUnmount(() => {
//   window.removeEventListener('scroll', handleScroll)
// })

// watch(currentSectionIndex, (newIndex) => {
//   // 현재 섹션이 변경될 때마다 해당 섹션으로 스크롤
//   scrollToSection(newIndex)
//   console.log(newIndex)
// })



</script>
