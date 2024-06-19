import { defineStore } from 'pinia';
import restApi from '@/utils/axios';

export const useAgentStore = defineStore({
  id: 'agent',
  state: () => ({
    agents: [],
    agent: null,
    loading: false,
    error: null,
  }),
  getters: {
    allAgents: (state) => state.agents,
    getAgentById: (state) => (id) => state.agents.find(agent => agent.agent_id === id),
  },
  actions: {
    async fetchAgents() {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get('/agent/', { 'accept': 'application/json' });
        this.agents = response.data;
      } catch (error) {
        this.error = error;
      } finally {
        this.loading = false;
      }
    },
    async fetchAgentById(agentId) {
      this.loading = true;
      this.error = null;
      try {
        const { get } = restApi();
        const response = await get(`/agent/${agentId}`, { 'accept': 'application/json' });
        this.agent = response.data;
        if (!this.agent) {
          throw new Error('Agent not found');
        }
      } catch (error) {
        this.error = error;
        router.push('/agent/list');
      } finally {
        this.loading = false;
      }
    },
    async createAgent(agentData) {
      this.loading = true;
      this.error = null;
      try {
        const { post } = restApi();
        await post('/agent/', agentData);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async updateAgent(agentData) {
      this.loading = true;
      this.error = null;
      try {
        const { put } = restApi();
        await put(`/agent/${agentData.agent_id}`, agentData);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
    async deleteAgent(agentId) {
      this.loading = true;
      this.error = null;
      try {
        const { del } = restApi();
        await del(`/agent/${agentId}`);
      } catch (error) {
        throw error;
      } finally {
        this.loading = false;
      }
    },
  },
});
