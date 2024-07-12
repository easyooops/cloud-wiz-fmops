<template>
    <Breadcrumbs main="Provider" title="Provider Create" />

    <div class="container-fluid">
        <div class="loader-overlay" v-if="loading">
            <div class="loader-box">
                <div class="loader-30"></div>
            </div>
        </div>

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
                                                <option value="M">Model</option>
                                                <option value="S">Storage</option>
                                                <option value="V">VectorDB</option>
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
                               <div class="row" v-else-if="isGoogleDrive">
                                 <div class="col">
                                   <div class="mb-3">
                                     <label>Google Client ID</label>
                                     <input v-model="clientId" class="form-control" type="text" placeholder="Client ID *">
                                   </div>
                                 </div>
                                 <div class="col">
                                   <div class="mb-3">
                                     <label>Auth Secret Key</label>
                                     <input v-model="authSecret" class="form-control" type="text" placeholder="Client Secret *">
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

                        <!-- loading area -->
                        <!-- <div class="loader-box" v-if="loading">
                            <div class="loader-30"></div>
                        </div> -->
                                                
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
import { useAuthStore } from '@/store/auth';
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
        const allProviders = ref([]);
        const providers = ref([]);
        const selectedCompany = ref(null);
        const loading = ref(false);
        const errorMessage = ref(null);
        const successMessage = ref(null);
        const userId = ref(useAuthStore().userId);
        const clientId = ref('');
        const authSecret = ref('');

        const fetchAllProviders = async () => {
            loading.value = true;
            try {
                await providerStore.fetchProviders();
                allProviders.value = providerStore.allProviders;
                filterProvidersByType(selectedType.value);
            } finally {
                loading.value = false;
            }
        };

        const filterProvidersByType = (type) => {
            providers.value = allProviders.value.filter(provider => provider.type === type);
            if (providers.value.length > 0) {
                selectedProvider.value = providers.value[0].provider_id;
                selectedCompany.value = providers.value[0].company;
            } else {
                selectedProvider.value = null;
                selectedCompany.value = null;
            }
        };

        const isAmazonWebServices = computed(() => {
            return selectedCompany.value && (selectedCompany.value.includes('Amazon') || selectedCompany.value.includes('Bedrock'));
        });

        const isGitOrNotion = computed(() => {
            return selectedCompany.value && (selectedCompany.value.includes('GIT') || selectedCompany.value.includes('Notion'));
        });

        const isGoogleDrive = computed(() => {
          return selectedCompany.value && selectedCompany.value.includes('Google');
        });

        const createCredential = async () => {
            loading.value = true;
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
                    client_id: clientId.value,
                    auth_secret_key: authSecret.value,
                    creator_id: userId.value,
                    updater_id: userId.value
                });
                successMessage.value = 'Credential created successfully.';
                router.push('/provider/list');
            } catch (error) {
                errorMessage.value = 'An error occurred while creating the credential.';
            } finally {
                loading.value = false;
            }
        };

        onMounted(() => {
            fetchAllProviders();
        });

        watch(selectedType, (newType) => {
            filterProvidersByType(newType);
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
            clientId,
            authSecret,
            allProviders,
            providers,
            isAmazonWebServices,
            isGitOrNotion,
            isGoogleDrive,
            loading,
            errorMessage,
            successMessage,
            createCredential,
        };
    }
}
</script>

<style scoped>
.loader-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* 검정색 배경, 투명도 조절 가능 */
    z-index: 999; /* 로딩 오버레이가 최상위에 오도록 설정 */
    display: flex;
    justify-content: center;
    align-items: center;
}

.loader-box {
    width: 100px; /* 로딩 바의 너비 설정 */
    height: 100px; /* 로딩 바의 높이 설정 */
    background-color: #fff; /* 로딩 바의 배경색 */
    border-radius: 10px; /* 로딩 바 모서리 둥글게 */
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.5); /* 로딩 바에 그림자 효과 추가 */
}
</style>