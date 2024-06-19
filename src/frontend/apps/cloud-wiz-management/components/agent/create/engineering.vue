<template>
    <div class="card mb-0">
        <div class="chat">
            <div class="card-header d-flex">
                <div class="about">
                    <ul>
                        <li class="list-inline-item"><i class="fa fa-chain"></i></li>
                        <li class="list-inline-item"><h5>Engineering</h5></li>
                    </ul>
                </div>
                <div class="row">
                    <div class="col">
                        <button @click="saveAgent" class="btn btn-primary me-2">Save</button>
                        <button @click="deleteAgent" class="btn btn-danger me-2">Delete</button>
                        <router-link to="/agent/list" class="btn btn-secondary">Back to List</router-link>
                    </div>
                </div>                  
                <!-- <ul class="list-inline float-start float-sm-end chat-menu-icons">
                    <li class="list-inline-item">
                        <a href="#" @click="saveAgent"><i class="fa fa-save"></i></a>
                    </li>
                    <li class="list-inline-item">
                        <a href="/agent/list"><i class="fa fa-list"></i></a>
                    </li>
                </ul>       -->
            </div>
        </div>

        <div class="card-body p-0">
        <div class="row list-persons" id="addcon">
            <div class="col-xl-3 xl-50 col-md-5">
                <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                    <a class="contact-tab-0 nav-link" :class="this.activeTab == item.activeTab ? 'active show' : ''"
                        id="v-pills-user-tab" data-bs-toggle="pill" @click="activeDiv(item.activeTab)"
                        href="#v-pills-user" role="tab" aria-controls="v-pills-user" aria-selected="true"
                        v-for="(item, index) in menu" :key="index">
                        <div class="media">
                            <li class="list-inline-item"><i :class="item.class"></i></li>
                            <div class="media-body">
                                <h6> <span class="first_name_0">{{ item.menu }}</span></h6>
                                <p class="email_add_0">{{ item.description }}</p>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
            <div class="col-xl-9 xl-50 col-md-7">
                <div class="tab-content" id="v-pills-tabContent" :style="!this.display ? { display: 'none' } : ''">
                    <div class="tab-pane contact-tab-0 tab-content-child fade show"
                        :class="item.activeTab === this.activeTab ? 'active' : ''" id="v-pills-user" role="tabpanel"
                        aria-labelledby="v-pills-user-tab" v-for="(item, index) in menu" :key="index">

                        <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
                        <div v-if="successMessage" class="alert alert-success mt-3">{{ successMessage }}</div>   

                        <!-- Foundation Model -->
                        <div class="card-body" v-if="'0'==this.activeTab">
                            <div class="form theme-form">
                                <div class="card">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <label for="agentName">Agent Name *</label>
                                            <input v-model="agentName" class="form-control" type="text" id="agentName" placeholder="Agent Name *" required>
                                        </div>
                                        <div class="mb-3">
                                            <label for="agentDescription">Agent Description</label>
                                            <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description">
                                        </div>
                                    </div>
                                </div>                                    

                                <div class="card">
                                    <div class="card-body">                                    
                                        <div class="row">
                                            <div class="col-xl-4 mb-3">
                                                <div class="col-form-label">Model Type *</div>
                                                <select class="form-select form-control-primary" v-model="modelType">
                                                    <option value="C">Chat</option>
                                                    <option value="T">Text</option>
                                                    <option value="I">Image</option>
                                                </select>
                                            </div>
                                            <div class="col-xl-4 mb-3">
                                                <div class="col-form-label">Provider *</div>
                                                <select class="form-select form-control-primary" v-model="selectedProvider">
                                                    <option value="" disabled hidden>Select Provider</option>
                                                    <option v-for="provider in filteredProviders" :key="provider.provider_id" :value="provider.provider_id">{{ provider.credential_name }}</option>
                                                </select>
                                            </div> 
                                            <div class="col-xl-4 mb-3">
                                                <div class="col-form-label">Foundation Model *</div>
                                                <select class="form-select form-control-primary" v-model="selectedFoundationModel">
                                                    <option value="" disabled hidden>Select Foundation Model</option>
                                                    <option v-for="model in filteredModels" :key="model.model_id" :value="model.model_id">{{ model.model_name }}</option>
                                                </select>
                                            </div>                                             
                                        </div>                                
                                    </div>
                                </div> 

                                <div class="card">
                                    <div class="card-body">
                                        <div class="form-group row mb-5">
                                            <label class="col-md-2 col-form-label sm-left-text" for="temperature">Temperature *</label>
                                            <div class="col-md-9">
                                                <VueSlider v-model="temperature.value" :data="temperature.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'"></VueSlider>
                                            </div>
                                        </div>
                                        <div class="form-group row mb-5">
                                            <label class="col-md-2 col-form-label sm-left-text" for="topP">Top P *</label>
                                            <div class="col-md-9">
                                                <VueSlider v-model="topP.value" :data="topP.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'"></VueSlider>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="card">
                                    <div class="card-body"> 
                                        <div class="mb-3">
                                            <fieldset>
                                                <label class="col-md-2 col-form-label sm-left-text" for="requestToken">Request Token Limit</label>
                                                <div class="input-group col-md-9">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="decrementRequestToken"><i class="fa fa-minus"></i></button>
                                                    <input class="touchspin form-control" type="text" v-model="requestToken">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-up" @click="incrementRequestToken"><i class="fa fa-plus"></i></button>
                                                </div>
                                            </fieldset>
                                        </div>
                                        <div class="mb-3">
                                            <label for="responseToken">Response Token Limit</label>
                                            <fieldset>
                                                <div class="input-group">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="decrementResponseToken"><i class="fa fa-minus"></i></button>
                                                    <input class="touchspin form-control" type="text" v-model="responseToken">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-up" @click="incrementResponseToken"><i class="fa fa-plus"></i></button>
                                                </div>
                                            </fieldset>
                                        </div>
                                    </div>
                                </div>
                                                                      
                            </div>
                        </div>

                        <!-- Embedding -->
                        <div class="card-body" v-if="'1'==item.activeTab">
                            <div class="form theme-form">

                                <div class="card">
                                    <div class="card-body">  
                                        <div class="media mb-3">
                                            <label class="col-form-label m-r-10">Embedding Enable</label>
                                            <div class="media-body text-end">
                                                <label class="switch">
                                                    <input type="checkbox" v-model="embeddingEnabled"><span class="switch-state"></span>
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !embeddingEnabled }">
                                    <div class="card-body">
                                        <div class="row">
                                            <div class="col-xl-6 mb-3">
                                                <div class="col-form-label">Embedding Provider *</div>
                                                <select class="form-select form-control-primary" v-model="selectedEmbeddingProvider">
                                                    <option value="" disabled hidden>Select Embedding Provider</option>
                                                    <option v-for="provider in filteredEmbeddingProviders" :key="provider.provider_id" :value="provider.provider_id">{{ provider.credential_name }}</option>
                                                </select>
                                            </div> 
                                            <div class="col-xl-6 mb-3">
                                                <div class="col-form-label">Embedding Model *</div>
                                                <select class="form-select form-control-primary" v-model="selectedEmbeddingModel">
                                                    <option value="" disabled hidden>Select Embedding Model</option>
                                                    <option v-for="model in filteredEmbeddingModels" :key="model.model_id" :value="model.model_id">{{ model.model_name }}</option>
                                                </select>
                                            </div>                                             
                                        </div>                                        
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !embeddingEnabled }">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <div class="col-form-label">Storage *</div>
                                            <select class="form-select form-control-primary" v-model="selectedStorageProvider">
                                                <option value="" disabled hidden>Select Storage Provider</option>
                                                <option v-for="provider in filteredStorageProviders" :key="provider.provider_id" :value="provider.provider_id">{{ provider.credential_name }}</option>
                                            </select>
                                        </div>
                                        <div v-if="isS3ProviderSelected" class="mb-3">
                                            <div class="col-form-label">Object</div>
                                            <select class="form-select form-control-primary" v-model="selectedObject">
                                                <option value="" disabled hidden>Selete Object</option>
                                                <option v-for="object in filteredObjects" :key="object.store_id" :value="object.store_id">{{ object.store_name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !embeddingEnabled }">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <div class="col-form-label">Vector DB</div>
                                            <select class="form-select form-control-primary" v-model="selectedVectorDB">
                                                <option value="" disabled hidden>FAISS</option>
                                                <option v-for="provider in filteredVectorDBProviders" :key="provider.provider_id" :value="provider.provider_id">{{ provider.credential_name }}</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                            
                            </div>
                        </div>
                        
                        <!-- Processing -->
                        <div class="card-body" v-if="'2' == item.activeTab">
                            <div class="form theme-form">
                                <div class="card">
                                    <div class="card-body">
                                        <div class="media mb-3">
                                            <label class="col-form-label m-r-10">Processing Enable</label>
                                            <div class="media-body text-end">
                                                <label class="switch">
                                                    <input type="checkbox" v-model="processingEnabled"><span class="switch-state"></span>
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !processingEnabled }">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <div class="col-form-label">Pre-Processing</div>
                                            <select class="form-select form-control-primary" v-model="selectedPreProcessing" :disabled="!processingEnabled">
                                                <option value="" disabled hidden>Select One Value Only</option>
                                                <option value="task I">task I</option>
                                                <option value="task II">task II</option>
                                                <option value="template I">template I</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !processingEnabled }">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <div class="col-form-label">Post-Processing</div>
                                            <select class="form-select form-control-primary" v-model="selectedPostProcessing" :disabled="!processingEnabled">
                                                <option value="" disabled hidden>Select One Value Only</option>
                                                <option value="task I">task I</option>
                                                <option value="task II">task II</option>
                                                <option value="template I">template I</option>
                                            </select>
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
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import { useContactStore } from '~~/store/contact'
import { useAgentStore } from '@/store/agent';
import { useProviderStore } from '@/store/provider';
import { useStorageStore } from '@/store/storage';
import { mapState, mapActions } from 'pinia';
import { useRouter } from 'vue-router';

export default {
    name: 'EngineeringSetup',
    components: {
        VueSlider,
    },
    data() {
        return {
            router: {},
            num1: 5000,
            temperature: {
                value: 0.7,
                data: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
            },
            topP: {
                value: 0.9,
                data: [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1],
            },
            agentName: '',
            agentDescription: '',
            selectedFoundationModel: '',
            requestToken: 5000,
            responseToken: 5000,
            selectedEmbeddingProvider: '',
            selectedEmbeddingModel: '',
            selectedProvider: '',
            selectedStorageProvider: '',
            selectedObject: '',
            selectedVectorDB: '',
            selectedPreProcessing: '',
            selectedPostProcessing: '',
            embeddingEnabled: false,
            processingEnabled: false,
            data: {
                "data": [
                    {
                        "activeTab": "0",
                        "class": "fa fa-code-fork",
                        "menu": "Foundation Model *",
                        "description": "Language Models (LLMs) serve as the foundation for chat systems, understanding and generating human-like text.",
                    },
                    {
                        "activeTab": "1",
                        "class": "fa fa-database",
                        "menu": "Embedding",
                        "description": "Embeddings capture semantic meaning of text for efficient retrieval in retrieval-augmented generation (RAG) models.",
                    },
                    {
                        "activeTab": "2",
                        "class": "fa fa-cogs",
                        "menu": "Processing",
                        "description": "Processing involves preparing input data for models (preprocessing) and handling model outputs (postprocessing) for effective communication or analysis.",
                    },
                ],
            },
            modelType: 'C',
            agentId: '',
            agentData: {},            
            errorMessage: '',
            successMessage: '',
            userId: '3fa85f64-5717-4562-b3fc-2c963f66afa6'
        }
    },
    computed: {
        display() {
            return useContactStore().display
        },
        activeTab() {
            return useContactStore().activeTab
        },
        menu() {
            return this.data.data
        },
        ...mapState(useProviderStore, ['credential', 'models']),
        ...mapState(useStorageStore, ['storages']),  
        ...mapState(useAgentStore, ['agent']),
        filteredProviders() {
            return this.credential.filter(provider => provider.provider_type === "M");
        },
        filteredModels() {
            return this.models.filter(model => model.model_type === this.modelType && model.provider_id == this.selectedProvider);
        },
        filteredEmbeddingProviders() {
            return this.credential.filter(provider => provider.provider_type === "M");
        },
        filteredEmbeddingModels() {
            return this.models.filter(model => model.model_type === "E" && model.provider_id == this.selectedEmbeddingProvider);
        },
        filteredStorageProviders() {
            return this.credential.filter(provider => provider.provider_type === "S");
        },
        filteredObjects() {
            return this.storages;
        },
        isS3ProviderSelected() {
            const selectedProvider = this.credential.find(provider => provider.provider_id === this.selectedStorageProvider);
            return selectedProvider && selectedProvider.credential_name.includes('S3');
        },
        filteredVectorDBProviders() {
            return this.credential.filter(provider => provider.provider_type === "V");
        },               
    },
    watch: {
        requestToken(newValue) {
            if (newValue > 5000) this.requestToken = 5000
            else if (newValue < 0) this.requestToken = 0
        },
        responseToken(newValue) {
            if (newValue > 5000) this.responseToken = 5000
            else if (newValue < 0) this.responseToken = 0
        },
        selectedProvider(newProviderId) {
            if (this.models.length > 0) {
                const filteredModels = this.models.filter(model => model.model_type === this.modelType && model.provider_id == newProviderId);
                if (filteredModels.length > 0) {
                    this.selectedFoundationModel = filteredModels[0].model_id;
                }
            }
        },
        modelType(newModelType) {
            if (this.models.length > 0) {
                const filteredModels = this.models.filter(model => model.model_type === newModelType && model.provider_id == this.selectedProvider);
                if (filteredModels.length > 0) {
                    this.selectedFoundationModel = filteredModels[0].model_id;
                }
            }
        },
        selectedEmbeddingProvider(newProviderId) {
            if (this.models.length > 0) {
                const filteredEmbeddingModels = this.models.filter(model => model.model_type === "E" && model.provider_id == newProviderId);
                if (filteredEmbeddingModels.length > 0) {
                    this.selectedEmbeddingModel = filteredEmbeddingModels[0].model_id;
                }
            }
        }

    },
    methods: {
        ...mapActions(useProviderStore, ['fetchCredential', 'fetchModels']),
        ...mapActions(useStorageStore, ['fetchAllStorages']),
        ...mapActions(useAgentStore, ['fetchAgentById']),
        activeDiv(item) {
            useContactStore().active(item)
        },
        incrementRequestToken() {
            if (this.requestToken < 5000) this.requestToken++
        },
        decrementRequestToken() {
            if (this.requestToken > 0) this.requestToken--
        },
        incrementResponseToken() {
            if (this.responseToken < 5000) this.responseToken++
        },
        decrementResponseToken() {
            if (this.responseToken > 0) this.responseToken--
        },
        async fetchAgentData() {
            this.agentId = String(this.router.currentRoute.query.agentId);
            if (this.agentId) {
                try {
                    await useAgentStore().fetchAgentById(this.agentId);
                    const agentInfo = useAgentStore().agent; 
                    this.agentData = agentInfo;
                    this.agentName = agentInfo.agent_name;
                    this.agentDescription = agentInfo.agent_description;
                    this.modelType = agentInfo.fm_provider_type;
                    this.selectedProvider = agentInfo.fm_provider_id;
                    this.selectedFoundationModel = agentInfo.fm_model_id;
                    this.temperature.value = agentInfo.fm_temperature;
                    this.topP.value = agentInfo.fm_top_p;
                    this.requestToken = agentInfo.fm_request_token_limit;
                    this.responseToken = agentInfo.fm_response_token_limit;
                    this.embeddingEnabled = agentInfo.embedding_enabled;
                    this.selectedEmbeddingProvider = agentInfo.embedding_provider_id;
                    this.selectedEmbeddingModel = agentInfo.embedding_model_id;
                    this.selectedStorageProvider = agentInfo.storage_provider_id;
                    this.selectedObject = agentInfo.storage_object_id;
                    this.selectedVectorDB = agentInfo.vector_db_provider_id;
                    this.processingEnabled = agentInfo.processing_enabled;
                    this.selectedPreProcessing = agentInfo.pre_processing_id;
                    this.selectedPostProcessing = agentInfo.post_processing_id;                    
                } catch (error) {
                    console.error('Error fetching agent data:', error);
                }
            }
        },
        async deleteAgent() {

            this.errorMessage = '';
            this.successMessage = '';

            try {
                await useAgentStore().deleteAgent(this.agentId);
                this.successMessage = 'Agent deleted successfully.';
                this.router.push('/agent/list');
            } catch (error) {
                this.errorMessage = 'An error occurred while deleting the agent.';
            }
        },
        async saveAgent() {

            this.errorMessage = '';
            this.successMessage = '';

            if (!this.agentName || !this.selectedFoundationModel || !this.selectedProvider || !this.temperature.value || !this.topP.value || !this.requestToken || !this.responseToken || !this.selectedProvider || !this.userId) {
                this.errorMessage = 'Please enter the required information.';
                setTimeout(() => {
                    this.errorMessage = '';
                    this.successMessage = '';
                }, 2000);                
                return;
            }

            try {
                const agentData = {
                    user_id: this.userId,
                    agent_name: this.agentName,
                    agent_description: this.agentDescription,
                    fm_provider_type: this.modelType,
                    fm_provider_id: this.selectedProvider,
                    fm_model_id: this.selectedFoundationModel,
                    fm_temperature: this.temperature.value,
                    fm_top_p: this.topP.value,
                    fm_request_token_limit: this.requestToken,
                    fm_response_token_limit: this.responseToken,
                    embedding_enabled: this.embeddingEnabled,
                    embedding_provider_id: this.selectedEmbeddingProvider,
                    embedding_model_id: this.selectedEmbeddingModel,
                    storage_provider_id: this.selectedStorageProvider,
                    storage_object_id: this.selectedObject,
                    vector_db_provider_id: this.selectedVectorDB,
                    processing_enabled: this.processingEnabled,
                    pre_processing_id: this.selectedPreProcessing,
                    post_processing_id: this.selectedPostProcessing,
                    creator_id: this.userId,
                    updater_id: this.userId
                };

                if (this.agentId) {
                    agentData.agent_id = this.agentId;
                    await useAgentStore().updateAgent(agentData);
                    this.successMessage = 'Agent updated successfully.';
                } else {
                    await useAgentStore().createAgent(agentData);
                    const agentInfo = useAgentStore().agent;
                    this.agentId = agentInfo.agent_id;
                    this.successMessage = 'Agent created successfully.';
                }                
            } catch (error) {
                this.errorMessage = 'An error occurred while creating the agent.';
            }
            setTimeout(() => {
                this.errorMessage = '';
                this.successMessage = '';
            }, 2000);
        },        
    },
    async mounted() {
        this.router = useRouter();
        if (this.router.currentRoute.query.agentId || this.agentId) {
            await this.fetchAgentData();
        }
        await useProviderStore().fetchCredential({ userId: this.userId });
        await useProviderStore().fetchModels();
        if (this.credential.length > 0) {
            this.selectedProvider = this.filteredProviders[0]?.provider_id || '';
            this.selectedEmbeddingProvider = this.filteredEmbeddingProviders[0]?.provider_id || '';
            this.selectedStorageProvider = this.filteredStorageProviders[0]?.provider_id || '';
            this.selectedVectorDB = this.filteredVectorDBProviders[0]?.provider_id || '';
            
        }
        await useStorageStore().fetchAllStorages({ userId: this.userId });
        if (this.storages.length > 0) {
            this.selectedObject = this.filteredObjects[0]?.store_id || '';
        }        
    }    
}
</script>

<style scoped>
.fa {
    font: normal normal normal 30px / 1 FontAwesome;
}
.fa-minus {
    font: normal normal normal 10px / 1 FontAwesome;
}
.fa-plus {
    font: normal normal normal 10px / 1 FontAwesome;
}
.product-name {
    margin-left: 10px;
}
.prooduct-details-box {
    cursor: pointer;
    padding: 10px;
}
.media.selected {
    border: 2px solid #007bff;
    background-color: #e7f1ff;
}
.form-control-primary {
    border-color: var(--theme-deafult);
    color: var(--theme-deafult);
}
.disabled-card {
    pointer-events: none;
    opacity: 0.6;
}
</style>