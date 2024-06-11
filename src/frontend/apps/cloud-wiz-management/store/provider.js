import { defineStore } from 'pinia';
import restApi from '@/utils/axios';

export const useProviderStore = defineStore({
    id: 'provider',
    state: () => ({
      providers: [],
      loading: false,
      error: null
    }),
    getters: {
      allProviders: (state) => state.providers,
      getProviderById: (state) => (id) => state.providers.find(provider => provider.provider_id === id)
    },
    actions: {
      async fetchProviders() {
        this.loading = true;
        this.error = null;
        try {
          const { get } = restApi();
          const response = await get('/provider/', null, { 'accept': 'application/json' });
          this.providers = response.data;
        } catch (error) {
          this.error = error;
        } finally {
          this.loading = false;
        }
      },
      async fetchProvidersByType(type) {
        this.loading = true;
        this.error = null;
        try {
          const { get } = restApi();
          const response = await get(`/provider/?type=${type}`, null, { 'accept': 'application/json' });
          this.providers = response.data;
        } catch (error) {
          this.error = error;
        } finally {
          this.loading = false;
        }
      },
      async createCredential(credentialData) {
          this.loading = true;
          this.error = null;
          try {
              const { post } = restApi();
              await post('/credential/', credentialData);
          } catch (error) {
              throw error;
          } finally {
              this.loading = false;
          }
      }
    }
  });
