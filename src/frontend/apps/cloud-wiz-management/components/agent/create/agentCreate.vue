<template>
    <div class="col-xl-12 col-md-12 box-col-12">
        <div class="file-content">
            <div class="card shadow">
                <div class="card-header" style="background-color: #ffffff;">
                    <div class="media">
                        <div class="media-body text-end">
                            <button class="btn btn-outline-danger ms-2" @click="deleteStorage()">
                                <vue-feather type="trash-2" class="text-top"></vue-feather> Delete Agent
                            </button>
                        </div>
                    </div>
                </div>
                <!-- Model -->
                <div class="card-body" style="background-color: #f5f5f5;">
                    <div class="col-sm-12">
                        <div class="card">
                            <div class="card-header">
                                <h3>LLMs/Chat Model</h3>
                            </div>
                            <div class="card-body">
                                <div class="form theme-form">
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentName">Agent Name</label>
                                                <input v-model="agentName" class="form-control" type="text" id="agentName" placeholder="Agent Name *" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentDescription">Agent Description</label>
                                                <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description *">
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentDescription">Foundation Model</label>
                                                <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description *">
                                            </div>
                                        </div>
                                    </div>                                    
                                </div>
                            </div>
                        </div>  
                    </div>
                </div>
                <!-- Embedding -->
                <div class="card-body" style="background-color: #f5f5f5; margin-top: -40px;">
                    <div class="col-sm-12">
                        <div class="card">
                            <div class="card-header">
                                <h3>Embedding</h3>
                            </div>
                            <div class="card-body">
                                <div class="form theme-form">
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentName">Storage</label>
                                                <input v-model="agentName" class="form-control" type="text" id="agentName" placeholder="Agent Name *" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentDescription">Vector DB</label>
                                                <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description *">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>  
                    </div>
                </div>                   
                <!-- Processing -->
                <div class="card-body" style="background-color: #f5f5f5; margin-top: -40px;">
                    <div class="col-sm-12">
                        <div class="card">
                            <div class="card-header">
                                <h3>Processing</h3>
                            </div>
                            <div class="card-body">
                                <div class="form theme-form">
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentName">Pre-Processing</label>
                                                <input v-model="agentName" class="form-control" type="text" id="agentName" placeholder="Agent Name *" required>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="row">
                                        <div class="col">
                                            <div class="mb-3">
                                                <label for="agentDescription">Post-Processing</label>
                                                <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description *">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>  
                    </div>
                </div>  

            </div>
        </div>
    </div>
</template>
  
  <script>
  import { ref } from 'vue';
  import { useAgentStore } from '@/store/agent';
  import { useRouter } from 'vue-router';
  
  export default {
    name: 'CreateAgent',
    setup() {
      const agentStore = useAgentStore();
      const router = useRouter();
      const agentName = ref('');
      const agentDescription = ref('');
      const isLoading = ref(false);
      const errorMessage = ref(null);
      const successMessage = ref(null);
      const userId = ref('3fa85f64-5717-4562-b3fc-2c963f66afa6');
  
      const createAgent = async () => {
        isLoading.value = true;
        errorMessage.value = null;
        successMessage.value = null;
  
        try {
          await agentStore.createAgent({
            user_id: userId.value,
            agent_name: agentName.value,
            description: agentDescription.value,
            creator_id: userId.value,
            updater_id: userId.value
          });
          successMessage.value = 'Agent created successfully.';
          router.push('/agent/list');
        } catch (error) {
          errorMessage.value = 'An error occurred while creating the agent.';
        } finally {
          isLoading.value = false;
        }
      };
  
      return {
        agentName,
        agentDescription,
        isLoading,
        errorMessage,
        successMessage,
        createAgent
      };
    }
  };
  </script>
  