import { defineStore } from 'pinia';
import restApi from '@/utils/axios';

export const useProviderStore = defineStore({
    id: 'provider',
    state: () => ({
      providers: [],
      credential: [],
      credentials: [],
      models:[],
      loading: false,
      error: null
    }),
    getters: {
      allProviders: (state) => state.providers,
      getProviderById: (state) => (id) => state.providers.find(provider => provider.provider_id === id)
    },
    actions: {
      async fetchCredential({ userId }) {
        this.loading = true;
        this.error = null;
        try {
          const { get } = restApi();
          const response = await get(`/credential/?user_id=${userId}`);
          this.credentials = response.data;
        } catch (error) {
          this.error = error;
        } finally {
          this.loading = false;
        }
      },
      async fetchCredentialById(credentialId) {
        this.loading = true;
        this.error = null;
        try {
            const { get } = restApi();
            const response = await get(`/credential/${credentialId}`);
            this.credential = response.data;
            if (!this.credential) {
                throw new Error('Credential not found');
            }
        } catch (error) {
            this.error = error;
            router.push('/provider/list');
        } finally {         
            this.loading = false;
        }
      }, 
      async fetchProviders() {
        this.loading = true;
        this.error = null;
        try {
          const { get } = restApi();
          const response = await get('/provider/', null);
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
          const response = await get(`/provider/?type=${type}`, null);
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
      },
      async exchangeCodeForTokens(code) {
          try {
              const { get } = restApi();
              const response = await get(`/auth/google/callback?code=${code}`);
              return response.data;
          } catch (error) {
              throw error;
          }
      },
      async createGoogleCredential(code, userId, providerId, providerName) {
          this.loading = true;
          this.error = null;
          try {
              const tokens = await this.exchangeCodeForTokens(code);
              const credentialData = {
                  user_id: userId,
                  provider_id: providerId,
                  credential_name: providerName,
                  access_token: tokens.access_token,
                  refresh_token: tokens.refresh_token,
                  creator_id: userId,
                  updater_id: userId,
              };
              await this.createCredential(credentialData);
          } catch (error) {
              throw error;
          } finally {
              this.loading = false;
          }
      },

      async updateCredential(credentialData) {
        this.loading = true;
        this.error = null;
        try {
            const { put } = restApi();
            await put(`/credential/${credentialData.credential_id}`, credentialData);
        } catch (error) {
            throw error;
        } finally {
            this.loading = false;
        }
      },
      async deleteCredential(credentialId) {
        this.loading = true;
        this.error = null;
        try {
          const { del } = restApi();
          await del(`/credential/${credentialId}`);
        } catch (error) {
          throw error;
        } finally {
          this.loading = false;
        }
      },
      async fetchModels() {
        this.loading = true;
        this.error = null;
        try {
          const { get } = restApi();
          const response = await get('/model/', null);
          this.models = response.data;
        } catch (error) {
          this.error = error;
        } finally {
          this.loading = false;
        }
      },                 
    }  
  });
