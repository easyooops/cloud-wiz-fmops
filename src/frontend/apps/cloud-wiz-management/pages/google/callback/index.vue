<template>
  <div>
    <h1>Processing Google Drive Authentication...</h1>
  </div>
</template>

<script>
export default {
  name: 'GoogleDriveCallback',
  async mounted() {
    const urlParams = new URLSearchParams(window.location.search);
    const code = urlParams.get('code');

    if (!code) {
      console.error('Authorization code not found');
      window.close();
      return;
    }

    if (window.opener) {
      window.opener.postMessage({ code }, window.location.origin);
      setTimeout(() => window.close(), 100);
    } else {
      console.error('No opener window found');
    }
  }
};
</script>