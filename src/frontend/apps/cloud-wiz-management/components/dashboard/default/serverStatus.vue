<template>
    <h5>Server Status</h5>
    <div class="col-sm-12">
        <div class="card">
<!--            <div class="card-header">-->
<!--                <h5>Server Status</h5>-->
<!--                <span>All HTML headings, <code>&lt;h1&gt;</code> through <code>&lt;h6&gt;</code>, are available.</span>-->
<!--            </div>-->
            <div class="card-body typography">


                  <div class="center-wrapper">
<!--                    <div class="row justify-content-center">-->
                <div class="circle-alignment">

                    <div class="circle-center">
                        <div class="circle-wrapper">
                          <div class="success-status circle"></div>
                          <div class="icon">
                            <i class="fa fa-check"></i>
                          </div>
                        </div>
                        <p class="status-count">1</p>
                    </div>


                    <div class="circle-center">
                      <div class="circle-wrapper">
                        <div class="warning-status circle"></div>
                        <div class="icon">
                          <i class="fa fa-exclamation"></i>
                        </div>
                      </div>
                      <p class="status-count">2</p>
                    </div>




                    <div class="circle-center">
                      <div class="circle-wrapper">
                        <div class="error-status circle"></div>
                        <div class="icon">
                          <i class="fa fa-times"></i>
                        </div>
                      </div>
                      <p class="status-count">2</p>
                    </div>


                  </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>
// import heathStatus from './heathStatus.vue'
//
// export default {
//   components: {
//     heathStatus
//   }
// }
</script>



<style lang="scss">
/* ==========================================================================
  Current Status Mark
  =========================================================================== */
.circle-alignment {
  display: flex;
  justify-content: space-around; /* 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬, 필요한 경우에만 사용 */
  //gap: 20px; /* div 요소들 사이의 간격, 필요에 따라 조정 */
}

.circle-center {
  display: flex;
  justify-content: center;
}

.circle-wrapper {
  position: relative;
  width: 80px; // 원의 크기 설정 부분
  height: 80px; // 원의 크기 설정 부분
  float: left;
  margin: 10px;
}

.icon {
  position: absolute;
  color: #fff;
  font-size: 55px;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.circle {
  display: block;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  padding: 5.5px;
  background-clip: content-box;
  animation: spin 10s linear infinite;
}

.circle-wrapper:active .circle {
  animation: spin 2s linear infinite;
}

.success-status {
  background-color: #4BB543;
  border: 2.5px dashed #4BB543;
}

.error-status {
  background-color: #CA0B00;
  border: 2.5px dashed #CA0B00;
}

.warning-status {
  background-color: #F0D500;
  border: 2.5px dashed #F0D500;
}

@keyframes spin {
  100% {
    transform: rotateZ(360deg);
  }
}

.status-count {
  float: left;
  margin-top: 13px;
  margin-bottom: 13px;
  font-size: 45px;
  font-weight: 600;
}

.center-wrapper {
  //width: fit-content;
  margin: auto;
}

.center-wrapper2 .tab-list {
  width: fit-content;
  margin: auto;
}
</style>
    