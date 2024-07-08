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
        'https://p.datadoghq.com/sb/eb4d74c2-eb97-11ec-b30d-da7ad0900002-c478ac9bf6eff219365e965a7b367621'
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
      interval = setInterval(reloadIframe, 60000);
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
