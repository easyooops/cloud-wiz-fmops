import { defineStore } from 'pinia';
import restApi from '@/utils/axios';

export const useAgentStore = defineStore({
  id: 'agent',
  state: () => ({
    agents: [],
    loading: false,
    error: null
  }),
  getters: {
    allAgents: (state) => state.agents
  },
  actions: {
    async createAgent(agentData) {
      this.loading = true;
      this.error = null;
      try {
        const { post } = restApi();
        await post('/agents', agentData);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async fetchAgents() {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get('/agents');
        this.agents = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async deleteAgent(agentId) {
      this.loading = true;
      this.error = null;
      try {
        const { del } = restApi();
        await del(`/agents/${agentId}`);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    }
  }
});
