<template>
  <!-- POSTS WRAPPER -->
  <section class="bg--white-400 py-100 ct-04 content-section division">
    <div class="container">
      <!-- SECTION CONTENT (ROW) -->
      <div class="main-title-two">
        <h2 class="s-50 w-700 text-center main-text">클라우드 컨설팅을 빠르게</h2><br><br>
        <h3 class="s-25 w-400 text-center main-text">원하는 컨설팅 방식에 따라 One-Click, Wiz봇 컨설팅을 받으실 수 있습니다</h3><br><br>
      </div>
      <div class="row d-flex align-items-center">
        <!-- IMAGE BLOCK -->
        <div class="col-md-6">
          <div class="img-block left-column wow fadeInRight">
            <img class="img-fluid" src="/assets/images/wiz/wiz_main.png" alt="content-image" />
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
                <h5 class="s-22 w-700">OneClick 컨설팅</h5>
                <p>✅ 클라우드에 대한 지식이 부족한 사람들도 손쉽게 컨설팅을 진행</p>
                <p>✅ 사용자는 간단한 클릭만으로 컨설팅을 신청</p>
                <p>✅ 사용자가 제공한 정보를 기반으로, 최적의 컨설팅 결과를 제공</p>
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
                <h5 class="s-22 w-700">Wiz 봇 컨설팅</h5>
                <p>✅ Wiz 봇은 AI 챗봇으로, 디테일한 컨설팅을 제공</p>
                <p>✅ 사용자는 Wiz봇과의 대화를 통해 클라우드에 대한 컨설팅을 진행</p>
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
                <h5 class="s-22 w-700">맞춤형 전문 컨설팅 서비스</h5>
                <p>✅ 클라우드 컨설팅 서비스는 사용자의 요구와 상황에 맞춰 맞춤형으로 제공</p>
                <p>✅ 사용자의 비즈니스 목표와 요구 사항을 고려해 클라우드 전략을 제시</p>
              </div>
            </div>
            <!-- END CONTENT BOX #3 -->
          </div>
          <div class="fbox-wrapper">
            <div class="row row-cols-1 row-cols-md-2">
              <div class="col">
                <v-btn prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/consulting/one-click">
                  <template v-slot:prepend>
                    <v-icon color="success"></v-icon>
                  </template>
                  OneClick 컨설팅
                </v-btn>
              </div>
              <div class="col">
                <v-btn prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/consulting/chat">
                  <template v-slot:prepend>
                    <v-icon color="success"></v-icon>
                  </template>
                  WizBot 컨설팅
                </v-btn>
              </div>
            </div>
          </div>
        </div>
        <!-- END TEXT BLOCK -->
      </div>
      <!-- END SECTION CONTENT (ROW) -->
    </div>
    <!-- End container -->
  </section>
</template>

<script setup lang="ts">

</script>