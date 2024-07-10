<template>
    <Breadcrumbs main="Storage" title="Storage Create" />
    <div class="container-fluid">
        <div class="row">
        <div class="col-sm-12">
            <div class="card">
            <div class="card-body">
                <form @submit.prevent="createStorage">
                <div class="form theme-form">                     
                    <div class="row">
                        <div class="col">
                            <div class="mb-3">
                                <label>Storage Name</label>
                                <input v-model="storageName" class="form-control" type="text" placeholder="Storage Name *" required>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <div class="mb-3">
                                <label>Storage Description</label>
                                <input v-model="storageDescription" class="form-control" type="text" placeholder="Storage Description *">
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <button type="submit" class="btn btn-primary me-2">Create Storage</button>
                            <router-link to="/storage/list" class="btn btn-secondary">Back to List</router-link>
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
import { ref } from 'vue';
import { useStorageStore } from '@/store/storage';
import { useAuthStore } from '@/store/auth';
import { useRouter } from 'vue-router';

export default {
    name: 'createStorage',
    setup() {
        const storageStore = useStorageStore();
        const router = useRouter();
        const storageName = ref('');
        const storageDescription = ref('');
        const isLoading = ref(false);
        const errorMessage = ref(null);
        const successMessage = ref(null);
        const userId = ref(useAuthStore().userId);

        const createStorage = async () => {
        isLoading.value = true;
        errorMessage.value = null;
        successMessage.value = null;

        try {
            await storageStore.createStorage({
                user_id: userId.value,
                store_name: storageName.value,
                description: storageDescription.value,
                creator_id: userId.value,
                updater_id: userId.value
            });
            successMessage.value = 'Storage created successfully.';
            router.push('/storage/list');
        } catch (error) {
            errorMessage.value = 'An error occurred while creating the storage.';
        } finally {
            isLoading.value = false;
        }
        };

        return {
            storageName,
            storageDescription,
            isLoading,
            errorMessage,
            successMessage,
            createStorage,
        };
    }
};
</script>
