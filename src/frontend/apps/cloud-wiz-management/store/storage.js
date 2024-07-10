import { defineStore } from 'pinia';
import restApi from '@/utils/axios';

export const useStorageStore = defineStore({
  id: 'storage',
  state: () => ({
    storages: [],
    storageDetail: null,
    loading: false,
    error: null
  }),
  getters: {
    allStorages: (state) => state.storages,
    getStorageById: (state) => (id) => state.storages.find(storage => storage.id === id)
  },
  actions: {
    async fetchAllStorages() {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get('/store/');
        this.storages = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchStorageById({ userId }) {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get(`/store/?user_id=${userId}`, null);
        this.storages = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async createStorage(storageData) {
      this.loading = true;
      this.error = null;
      try {
        const { post } = restApi();
        await post('/store/', storageData);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async updateStorage(storageData) {
      this.loading = true;
      this.error = null;
      try {
        const { put } = restApi();
        await put(`/store/${storageData.id}`, storageData);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async deleteStorage(storageId) {
      this.loading = true;
      this.error = null;
      try {
        const { del } = restApi();
        await del(`/store/${storageId}`);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async uploadFile(file, storeName) {
      this.loading = true;
      this.error = null;
      try {
        const formData = new FormData();
        formData.append('file', file);
        
        const { post } = restApi();
        await post(`/store/${storeName}/upload`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async fetchFiles(storeName) {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get(`/store/${storeName}/files`, {
          headers: {
            'accept': 'application/json'
          }
        });
        return response.data;
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async deleteFile(storeName, fileKey) {
      this.loading = true;
      this.error = null;
      try {
        const { del } = restApi();
        await del(`/store/${storeName}/files/${fileKey}`);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    
  }
});