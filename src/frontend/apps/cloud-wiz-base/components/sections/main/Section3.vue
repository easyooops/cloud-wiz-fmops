<template>
  <section class="pt-100 ct-04 content-section division main-section-three">
    <div class="container">
      <!-- SECTION CONTENT (ROW) -->
      <div class="main-title-two">
        <h2 class="s-50 w-700 text-center main-text">클라우드 관리를 편하게</h2><br><br>
        <h3 class="s-25 w-400 text-center main-text">간단한 클라우드 계정등록으로 리소스들을 관리할 수 있게 도와드립니다</h3><br><br>
      </div>
      <div class="row d-flex align-items-center">
        <!-- TEXT BLOCK -->
        <div class="col-md-6 order-last order-md-2">
          <div class="txt-block left-column wow fadeInRight">
            <!-- CONTENT BOX #1 -->
            <div class="cbox-2 process-step">
              <!-- Icon -->
              <div class="ico-wrap">
                <div class="cbox-2-ico bg--theme color--white">1</div>
                <span class="cbox-2-line"></span>
              </div>
              <!-- Text -->
              <div class="cbox-2-txt">
                <h5 class="s-22 w-700">Dashboard를 통한 신속한 리소스 모니터링</h5>
                <p>✅ 실시간 리소스의 상태를 모니터링해 문제를 빠르게 대응할 수 있습니다</p>
                <p>✅ 직관적인 화면을 통해 사용중인 리소스의 정보를 쉽게 파악할 수 있습니다</p>
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
                <h5 class="s-22 w-700">효율적인 자원 관리와 최적화</h5>
                <p>✅ 리소스의 사용량과 비용을 실시간으로 확인할 수 있습니다</p>
                <p>✅ 리소스의 사용 패턴을 분석해 최적화된 자원 할당 방안을 제시합니다</p>
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
                <h5 class="s-22 w-700">알림을 통한 신속한 대응</h5>
                <p class="mb-0">✅ 리소스 과부하 등 이상 상황이 발생하면 알림을 받아 조치할 수 있습니다</p>
                <p class="mb-0">✅ 빠른 대응을 통해 시스템의 가용성과 안정성을 높일 수 있습니다</p>
              </div>
            </div>
            <!-- END CONTENT BOX #3 -->
            <div class="dash-btn" >
              <v-btn prepend-icon="mdi-check-circle" variant="tonal" size="x-large" NuxtLink to="/dashboard">
                <template v-slot:prepend>
                  <v-icon color="success"></v-icon>
                </template>
                Dashboard 바로가기
              </v-btn>
            </div>
          </div>
        </div>
        <!-- END TEXT BLOCK -->
        <!-- IMAGE BLOCK -->
        <div class="col-md-6 order-first order-md-2">
          <div class="img-block wow fadeInLeft">
            <img class="img-fluid" src="/assets/images/tablet-01.png" alt="content-image" />
          </div>
        </div>
      </div>
      <!-- END SECTION CONTENT (ROW) -->
    </div>
    <!-- End container -->
  </section>

</template>

<script setup lang="ts">

</script>