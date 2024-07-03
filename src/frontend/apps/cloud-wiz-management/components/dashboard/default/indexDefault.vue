<template>
  <div>
    <Breadcrumbs main="Dashboard" title="default" />
    <div class="container-fluid">
      <div class="row widget-grid">
        <iframe
            :src="dashboardUrl"
            width="100%"
            height="800px"
            frameborder="0"
            ref="iframe"
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';

export default defineComponent({
  setup() {
    const dashboardUrl = ref(
        'https://p.datadoghq.com/sb/eb4d74c2-eb97-11ec-b30d-da7ad0900002-99e2e258795b206ee0f0bbb8fc40eef9?fromUser=false&refresh_mode=sliding&from_ts=1719988246141&to_ts=1719989146141&live=true'
    );
    const iframeRef = ref<HTMLIFrameElement | null>(null);
    let interval: ReturnType<typeof setInterval> | null = null;

    const reloadIframe = () => {
      if (iframeRef.value) {
        const tempSrc = iframeRef.value.src;
        iframeRef.value.src = '';
        iframeRef.value.src = tempSrc;
      }
    };

    onMounted(() => {
      interval = setInterval(reloadIframe, 60000); // 1분마다 새로고침
    });

    onUnmounted(() => {
      if (interval) {
        clearInterval(interval);
      }
    });

    return {
      dashboardUrl,
      iframeRef,
    };
  },
});
</script>

<style scoped>
iframe {
  border: 0;
  width: 100%;
  height: 1000px;
}
</style>
