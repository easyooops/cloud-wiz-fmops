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
                <ul class="list-inline float-start float-sm-end chat-menu-icons">
                    <li class="list-inline-item">
                        <a href="#"><i class="fa fa-save"></i></a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#"><i class="fa fa-list"></i></a>
                    </li>
                </ul>      
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
                                                <label class="col-md-2 col-form-label sm-left-text" for="requestToken">Request Token</label>
                                                <div class="input-group col-md-9">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="decrementRequestToken"><i class="fa fa-minus"></i></button>
                                                    <input class="touchspin form-control" type="text" v-model="requestToken">
                                                    <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-up" @click="incrementRequestToken"><i class="fa fa-plus"></i></button>
                                                </div>
                                            </fieldset>
                                        </div>
                                        <div class="mb-3">
                                            <label for="responseToken">Response Token</label>
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
                                            <div class="col-form-label">Storage</div>
                                            <select class="form-select form-control-primary" v-model="selectedProvider" :disabled="!embeddingEnabled">
                                                <option value="" disabled hidden>Select Storage</option>
                                                <option value="Amazon S3">Amazon S3</option>
                                                <option value="GIT">GIT</option>
                                                <option value="Notion">Notion</option>
                                                <option value="Google Drive">Google Drive</option>
                                            </select>
                                        </div>
                                        <div class="mb-3">
                                            <div class="col-form-label">Object</div>
                                            <select class="form-select form-control-primary" v-model="selectedStorage" :disabled="!embeddingEnabled">
                                                <option value="" disabled hidden>Selete Object</option>
                                                <option value="Default Storage">Default Storage</option>
                                                <option value="Private Storage">Private Storage</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>

                                <div class="card" :class="{ 'disabled-card': !embeddingEnabled }">
                                    <div class="card-body">
                                        <div class="mb-3">
                                            <div class="col-form-label">Vector DB</div>
                                            <select class="form-select form-control-primary" v-model="selectedVectorDB" :disabled="!embeddingEnabled">
                                                <option value="" disabled hidden>Selete Vector DB</option>
                                                <option value="FAISS">FAISS</option>
                                                <option value="ChromaDB">ChromaDB</option>
                                                <option value="Pincone">Pincone</option>
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
import { mapState, mapActions } from 'pinia';

export default {
    name: 'EngineeringSetup',
    components: {
        VueSlider,
    },
    data() {
        return {
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
            selectedStorage: '',
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
            return this.models.filter(model => model.model_type === "E" && model.provider_id == this.selectedProvider);
        }               
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
                    this.selectedFoundationModel = filteredEmbeddingModels[0].model_id;
                }
            }
        },
        selectedEmbeddingModel(newModelType) {
            if (this.models.length > 0) {
                const filteredEmbeddingModels = this.models.filter(model => model.model_type === "E" && model.provider_id == this.selectedProvider);
                if (filteredEmbeddingModels.length > 0) {
                    this.selectedFoundationModel = filteredEmbeddingModels[0].model_id;
                }
            }
        }        
        
        
    },
    methods: {
        ...mapActions(useProviderStore, ['fetchCredential', 'fetchModels']),
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
        async saveAgent() {
            try {
                const agentData = {
                    agentName: this.agentName,
                    agentDescription: this.agentDescription,
                    selectedFoundationModel: this.selectedFoundationModel,
                    requestToken: this.requestToken,
                    responseToken: this.responseToken,
                    selectedEmbeddingProvider: this.selectedEmbeddingProvider,
                    selectedEmbeddingModel: this.selectedEmbeddingModel,
                    selectedProvider: this.selectedProvider,
                    selectedStorage: this.selectedStorage,
                    selectedVectorDB: this.selectedVectorDB,
                    selectedPreProcessing: this.selectedPreProcessing,
                    selectedPostProcessing: this.selectedPostProcessing,
                    embeddingEnabled: this.embeddingEnabled,
                    processingEnabled: this.processingEnabled
                };

                await useAgentStore().createAgent(agentData);

            } catch (error) {
                console.error('Error saving agent:', error);
            }
        },        
    },
    async mounted() {
        await useProviderStore().fetchCredential({ userId: this.userId });
        await useProviderStore().fetchModels();
        if (this.credential.length > 0) {
            this.selectedProvider = this.credential[0].provider_id;
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