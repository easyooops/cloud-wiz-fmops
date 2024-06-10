<template>
  <section class="bg--white-400 py-100 ct-04 content-section division">
    <!-- POSTS WRAPPER -->
    <div class="posts-wrapper">
      <div class="container">
        <div class="main-title-two">
          <h2 class="s-50 w-700 text-center main-text">간편하게 클라우드 인프라를 구축</h2><br><br>
          <h3 class="s-25 w-400 text-center main-text">제공하는 코드로 간편하게 클라우드 인프라를 구축하세요</h3><br><br>
        </div>
        <div class="row d-flex align-items-center">
          <!-- IMAGE BLOCK -->
          <div class="col-md-6">
            <div class="img-block left-column wow fadeInRight">
              <img class="img-fluid" src="/assets/images/wiz/main_develop.png" alt="content-image" />
            </div>
          </div>
          <!-- TEXT BLOCK -->
          <div class="col-md-6">
            <div class="txt-block right-column wow fadeInLeft main-section-two-txt">
              <!-- CONTENT BOX #1 -->
              <div class="cbox-2 process-step">
                <!-- Icon -->
                <div class="ico-wrap">
                  <div class="cbox-2-ico bg--theme color--white">1</div>
                  <span class="cbox-2-line"></span>
                </div>
                <!-- Text -->
                <div class="cbox-2-txt">
                  <h5 class="s-22 w-700">코드로 클라우드 인프라 구축</h5>
                  <p>✅ 코드를 사용하여 클라우드 인프라를 구축하는 방법을 제공</p>
                  <p>✅ 사용자는 단순히 코드를 복사하여 클라우드 인프라를 구성</p>
                  <p>✅ 클라우드에 대한 지식이 부족해도 코드를 복사해 손쉽게 인프라를 구성</p>
                </div>
              </div>
              <!-- END CONTENT BOX #1 -->
              <!-- CONTENT BOX #2 -->
              <div class="cbox-2 process-step">
                <!-- Icon -->
                <div class="ico-wrap">
                  <div class="cbox-2-ico bg--theme color--white">2</div>
                  <span class="cbox-2-line"></span>
                </div>
                <!-- Text -->
                <div class="cbox-2-txt">
                  <h5 class="s-22 w-700">CI/CD 파이프라인을 코드로 구현</h5>
                  <p>✅ IaC 서비스는 CI/CD 파이프라인을 코드로 구현하는 기능을 제공</p>
                  <p>✅ 코드로 인프라를 관리하고 배포하는 자동화된 프로세스를 구축</p>
                </div>
              </div>
              <!-- END CONTENT BOX #2 -->
              <!-- CONTENT BOX #3 -->
              <div class="cbox-2 process-step">
                <!-- Icon -->
                <div class="ico-wrap">
                  <div class="cbox-2-ico bg--theme color--white">3</div>
                </div>
                <!-- Text -->
                <div class="cbox-2-txt">
                  <h5 class="s-22 w-700">테라폼 코드로 인프라 구성</h5>
                  <p>✅ 테라폼 코드를 사용하여 인프라를 구성하는 기능을 제공</p>
                  <p>✅ 테라폼 코드를 사용하면 유연하고 확장 가능한 인프라 구성을 구현</p>
                </div>
              </div>
              <!-- END CONTENT BOX #3 -->
            </div>
            <div class="fbox-wrapper">
              <div class="row row-cols-1 row-cols-xl-3">
                <div class="col">
                  <div class="fbox-2">
                    <v-btn prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/development/cli-guide">
                      <template v-slot:prepend>
                        <v-icon color="success"></v-icon>
                      </template>
                      Iac로 구축
                    </v-btn>
                  </div>
                </div>
                <div class="col">
                  <v-btn  prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/development/git-action">
                    <template v-slot:prepend>
                      <v-icon color="success"></v-icon>
                    </template>
                    CI/CD 구축
                  </v-btn>
                </div>
                <div class="col">
                  <v-btn prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/development/template">
                    <template v-slot:prepend>
                      <v-icon color="success"></v-icon>
                    </template>
                    테라폼으로 구축
                  </v-btn>
                </div>
              </div>
            </div>

          </div>
          <!-- END TEXT BLOCK -->
      </div>
    </div>
    <!-- END POSTS WRAPPER -->
    </div>
  </section>
</template>

<script setup lang="ts">

</script>