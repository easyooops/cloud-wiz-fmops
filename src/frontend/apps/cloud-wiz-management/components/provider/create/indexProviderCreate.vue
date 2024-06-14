<template>
    <Breadcrumbs main="Provider" title="Provider Create" />

    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-body">
                        <form @submit.prevent="createCredential">
                            <div class="form theme-form">
                                <div class="row">
                                    <div class="col-sm-4">
                                        <div class="mb-3">
                                            <label>Provider Type</label>
                                            <select class="form-select" v-model="selectedType">
                                                <option :value="'M'">Model</option>
                                                <option :value="'N'">Not Model</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div class="col-sm-4">
                                        <div class="mb-3">
                                            <label>Provider</label>
                                            <select class="form-select" v-model="selectedProvider">
                                                <option v-for="provider in providers" :key="provider.provider_id" :value="provider.provider_id">
                                                    {{ provider.name }}
                                                </option>
                                            </select>                                        
                                        </div>
                                    </div>
                                </div>                            
                                <div class="row">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>Provider Name</label>
                                            <input v-model="providerName" class="form-control" type="text" placeholder="Provider Name *" required>
                                        </div>
                                    </div>
                                </div>
                                <div class="row" v-if="isAmazonWebServices">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>Access Key</label>
                                            <input v-model="accessKey" class="form-control" type="text" placeholder="Access Key *">
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>Secret Access Key</label>
                                            <input v-model="secretAccessKey" class="form-control" type="text" placeholder="Secret Access Key *">
                                        </div>
                                    </div>
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>Session Key</label>
                                            <input v-model="sessionKey" class="form-control" type="text" placeholder="Session Key *">
                                        </div>
                                    </div>
                                </div>
                                <div class="row" v-else-if="isGitOrNotion">
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>Access Token</label>
                                            <input v-model="accessToken" class="form-control" type="text" placeholder="Access Token *">
                                        </div>
                                    </div>
                                </div>
                                <div class="row" v-else>
                                    <div class="col">
                                        <div class="mb-3">
                                            <label>API Key</label>
                                            <input v-model="apiKey" class="form-control" type="text" placeholder="API Key *">
                                        </div>
                                    </div>
                                </div>   
                                <div class="row">
                                    <div class="col">
                                        <button type="submit" class="btn btn-primary me-2">Submit</button>
                                        <router-link to="/provider/list" class="btn btn-secondary">Back to List</router-link>
                                    </div>
                                </div>                       
                            </div>
                        </form>
                        <div v-if="errorMessage" class="alert alert-danger mt-3">{{ errorMessage }}</div>
                        <div v-if="successMessage" class="alert alert-success mt-3">{{ successMessage }}</div>                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, watch, onMounted, computed } from 'vue';
import { useProviderStore } from '@/store/provider';
import { useRouter } from 'vue-router';

export default {
    name: 'createProvider',
    setup() {
        const providerStore = useProviderStore();
        const router = useRouter();        
        const selectedType = ref('M');
        const selectedProvider = ref(null);
        const providerName = ref('');
        const accessKey = ref('');
        const secretAccessKey = ref('');
        const sessionKey = ref('');
        const accessToken = ref('');
        const apiKey = ref('');
        const apiEndpoint = ref('');
        const providers = ref([]);
        const selectedCompany = ref(null);
        const isLoading = ref(false);
        const errorMessage = ref(null);
        const successMessage = ref(null);
        const userId = ref('3fa85f64-5717-4562-b3fc-2c963f66afa6');

        const fetchProvidersByType = async (type) => {
            await providerStore.fetchProvidersByType(type);
            providers.value = providerStore.allProviders;

            if (providers.value.length > 0) {
                selectedProvider.value = providers.value[0].provider_id;
                selectedCompany.value = providers.value[0].company;
            }
        };

        const isAmazonWebServices = computed(() => selectedCompany.value && selectedCompany.value.includes('Amazon'));
        const isGitOrNotion = computed(() => selectedCompany.value && (selectedCompany.value.includes('GIT') || selectedCompany.value.includes('Notion')));

        const createCredential = async () => {
            isLoading.value = true;
            errorMessage.value = null;
            successMessage.value = null;

            try {
                await providerStore.createCredential({
                    user_id: userId.value,
                    provider_id: selectedProvider.value,
                    credential_name: providerName.value,
                    access_key: accessKey.value,
                    secret_key: secretAccessKey.value,
                    session_key: sessionKey.value,
                    access_token: accessToken.value,
                    api_key: apiKey.value,
                    api_endpoint: apiEndpoint.value,
                    creator_id: userId.value,
                    updater_id: userId.value
                });
                successMessage.value = 'Credential created successfully.';
                router.push('/provider/list');
            } catch (error) {
                errorMessage.value = 'An error occurred while creating the credential.';
            } finally {
                isLoading.value = false;
            }
        };

        onMounted(() => {
            fetchProvidersByType(selectedType.value);
        });

        watch(selectedType, (newType) => {
            fetchProvidersByType(newType);
        });

        watch(selectedProvider, (newProviderId) => {
            const selectedProviderObj = providers.value.find(provider => provider.provider_id === newProviderId);
            if (selectedProviderObj) {
                selectedCompany.value = selectedProviderObj.company;
            }
        });

        return {
            selectedType,
            selectedProvider,
            providerName,
            accessKey,
            secretAccessKey,
            sessionKey,
            accessToken,
            apiKey,
            apiEndpoint,
            providers,
            isAmazonWebServices,
            isGitOrNotion,
            isLoading,
            errorMessage,
            successMessage,
            createCredential,
        };
    }
}
</script>

