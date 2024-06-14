<template>
    <div class="col-xl-12 col-md-12 box-col-12">
        <div class="file-content">
            <div class="card">
                <div class="card-header">
                    <div class="media">
                        <!-- <form class="form-inline" action="#" method="get">
                            <div class="form-group mb-0">
                                <i class="fa fa-search"></i>
                                <input class="form-control-plaintext" type="text" placeholder="Search..." />
                            </div>
                        </form> -->
                        <div class="media-body text-end">
                            <router-link to="/storage/list" class="btn btn-secondary">Back to List</router-link>
                            <button class="btn btn-outline-danger ms-2" @click="deleteStorage()">
                                <vue-feather type="trash-2" class="text-top"></vue-feather> Delete Directory
                            </button>
                        </div>
                    </div>
                </div>
                <div class="card-body file-manager">
                    <div class="col-sm-12">
                        <div class="card">
                            <div class="card-header">
                                <h3>File Upload</h3>
                            </div>
                            <div class="card-body">
                                <DropZone 
                                    :dropzoneItemClassName="customClass"
                                    :maxFileSize="Number(60000000)"
                                    :url="uploadUrl"
                                    :uploadOnDrop="true"
                                    :multipleUpload="true"
                                    :parallelUpload="10" 
                                    @uploaded="handleFileUploaded" />
                            </div>                            
                        </div>
                    </div>
                    <h4 class="mb-3">All Files</h4>
                    <h6 class="mt-4">Files</h6>
                    <ul class="files">
                        <li class="file-box mb-3" v-for="file in files" :key="file">
                            <div class="file-top">
                                <i :class="'fa fa-file-'+getFileIconClass(file.Key)+' txt-info'"></i>
                                <i class="fa fa-remove f-14 ellips cursor-pointer" @click="deleteFile(file)"></i>
                            </div>
                            <div class="file-bottom">
                                <h6>{{ getFileName(file.Key) }}</h6>
                                <p class="mb-1">{{ formatFileSize(file.Size) }}</p>
                                <p><b>Last Open:</b> {{ formatDate(file.LastModified) }}</p>
                            </div>
                        </li>                     
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useStorageStore } from '@/store/storage';
import { useRouter } from 'vue-router';

export default {
    name: 'ModifyStorage',    
    data() {
        return {
            files: [],
            customClass: 'custom-dropzone-item'
        };
    },
    setup() {
        const API_ENDPOINT = import.meta.env.VITE_API_ENDPOINT+'/api/v1';
        const storageStore = useStorageStore();
        const router = useRouter();         
        const storeName = ref('default');
        const storeId = ref('');
        storeName.value = String(router.currentRoute.value.query.storeName);
        storeId.value = String(router.currentRoute.value.query.storeId);
        const uploadUrl = API_ENDPOINT+'/store/'+encodeURIComponent(storeName.value)+'/upload';
        const files = ref([]);

        const fetchFiles = async () => {
            try {
                const fetchedFiles = await storageStore.fetchFiles(storeName.value);
                files.value = fetchedFiles;
            } catch (error) {
                console.error('An error occurred while fetching the file list.', error);
            }
        };

        const formatFileSize = (sizeInBytes) => {
            if (sizeInBytes < 1024) {
                return sizeInBytes.toFixed(1) + ' B';
            } else if (sizeInBytes < 1024 * 1024) {
                return (sizeInBytes / 1024).toFixed(1) + ' KB';
            } else {
                return (sizeInBytes / (1024 * 1024)).toFixed(1) + ' MB';
            }
        };

        const formatDate = (dateString) => {
            const date = new Date(dateString);
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            const formattedDate = date.toLocaleDateString('en-US', options);

            const day = date.getDate();
            const daySuffix = getDaySuffix(day);
            const formattedDateWithSuffix = formattedDate.replace(/\b\d+\b/, `${day}${daySuffix}`);

            return formattedDateWithSuffix;
        };

        const getDaySuffix = (day) => {
            if (day >= 11 && day <= 13) {
                return 'th';
            }
            switch (day % 10) {
                case 1: return 'st';
                case 2: return 'nd';
                case 3: return 'rd';
                default: return 'th';
            }
        };

        const handleFileUploaded = async () => {
            try {
                await fetchFiles();
            } catch (error) {
                console.error('An error occurred while uploading the file.', error);
            } finally {
            }
        };

        const getFileName = (filePath) => {
            if (filePath && filePath.lastIndexOf('/') !== -1) {
                return filePath.substring(filePath.lastIndexOf('/') + 1);
            }
            return filePath;
        };

        const getFileExtension = (fileName) => {
            const lastIndex = fileName.lastIndexOf('.');
            return fileName.substring(lastIndex + 1);
        };

        const getFileIconClass = (fileType) => {
            const fileTypeMappings = {
                text: ['txt', 'log', 'md'],
                pdf: ['pdf'],
                word: ['doc', 'docx'],
                excel: ['xls', 'xlsx', 'csv'],
                powerpoint: ['ppt', 'pptx'],
                // photo: ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
                // picture: ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
                image: ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
                zip: ['zip', 'rar', '7z'],
                archive: ['zip', 'rar', '7z'],
                // sound: ['mp3', 'wav', 'ogg', 'flac'],
                audio: ['mp3', 'wav', 'ogg', 'flac'],
                // movie: ['mp4', 'avi', 'mkv', 'mov'],
                video: ['mp4', 'avi', 'mkv', 'mov'],
                code: ['html', 'css', 'js', 'java', 'py', 'cpp', 'c', 'php', 'rb', 'swift', 'json', 'xml']
            };

            for (const [icon, extensions] of Object.entries(fileTypeMappings)) {
                if (extensions.includes(getFileExtension(fileType).toLowerCase())) {
                    return icon + '-o';
                }
            }

            return 'file-o';
        };

        const deleteFile = async (file) => {
            try {
                await storageStore.deleteFile(storeName.value, getFileName(file.Key));
                await fetchFiles();
            } catch (error) {
                console.error('An error occurred while deleting the file.', error);
            }
        };

        const deleteStorage = async () => {
            try {
                await storageStore.deleteStorage(storeId.value);
                router.push('/storage/list');
            } catch (error) {
                console.error('An error occurred while deleting the storage.', error);
            }
        };

        onMounted(fetchFiles);

        return {
            files,
            uploadUrl,
            formatFileSize,
            formatDate,
            handleFileUploaded,
            getFileName,
            getFileExtension,
            getFileIconClass,
            deleteFile,
            deleteStorage
        };
    },
};
</script>
    
<style>
.dropzone__item--style img {
    width: 100px;
    height: auto;
}
.cursor-pointer {
  cursor: pointer;
}
</style>