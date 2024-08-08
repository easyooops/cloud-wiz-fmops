<template>
  <div>
    <h1>Processing Google Drive Authentication...</h1>
    <!-- Optional: Loading spinner or progress indicator -->
  </div>
</template>

<script>
import { useProviderStore } from '@/store/provider';

export default {
  name: 'GoogleDriveCallback',
  async mounted() {
    const providerStore = useProviderStore();

    try {
      const headers = useRequestHeaders(['cookie'])
      const { data: token } = await useFetch('/api/token', { headers })

      const credentialData = {
        user_id: sessionStorage.getItem('userId'),
        provider_id: sessionStorage.getItem('selectedProvider'),
        credential_name: sessionStorage.getItem('providerName'),
        access_token: token.value.access_token,
        refresh_token: token.value.refresh_token,
        creator_id: sessionStorage.getItem('userId'),
        updater_id: sessionStorage.getItem('userId'),
      };

      await providerStore.createCredential(credentialData);

      sessionStorage.removeItem('userId');
      sessionStorage.removeItem('selectedProvider');
      sessionStorage.removeItem('providerName');
      this.$router.push('/provider/list');
    } catch (error) {
      this.$router.push('/provider/list');
    }
  }
};
</script>
