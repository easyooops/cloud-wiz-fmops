<template>
    <div class="col-xl-9 col-md-12 box-col-12">
        <div class="file-content">
            <div class="card">
                <div class="card-header">
                    <div class="media">
                        <form class="form-inline" action="#" method="get">
                            <div class="form-group mb-0">
                                <i class="fa fa-search"></i>
                                <input class="form-control-plaintext" type="text" placeholder="Search..." />
                            </div>
                        </form>
                        <div class="media-body text-end">
                            <form class="d-inline-flex" action="#" method="POST" enctype="multipart/form-data"
                                name="myForm">
                                <div class="btn btn-primary" onclick="getFile()">
                                    <vue-feather type="plus-square" class="text-top"></vue-feather>
                                    Add New
                                </div>
                                <div style="height: 0px; width: 0px; overflow: hidden">
                                    <input id="upfile" type="file" onchange="sub(this)" />
                                </div>
                            </form>
                            <div class="btn btn-outline-primary ms-2">
                                <vue-feather type="upload" class="text-top"></vue-feather> Upload
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-body file-manager">
                    <h4 class="mb-3">All Files</h4>
                    <h6>Recently opened files</h6>
                    <ul class="files">
                        <li class="file-box" v-for="file in recentOpenfiles" :key="file">
                            <div class="file-top">
                                <i :class="file.iconClass"></i><i class="fa fa-ellipsis-v f-14 ellips"></i>
                            </div>
                            <div class="file-bottom">
                                <h6>{{ file.fileName }}</h6>
                                <p class="mb-1">{{ file.fileSize }}</p>
                                <p><b>last open : </b>{{ file.lastOpen }}</p>
                            </div>
                        </li>
                    </ul>
                    <h6 class="mt-4">Folders</h6>
                    <ul class="folder">
                        <li class="folder-box" v-for="folder in folders" :key="folder">
                            <div class="media">
                                <i :class="folder.iconClass"></i>
                                <div class="media-body ms-3">
                                    <h6 class="mb-0">{{ folder.folderName }}</h6>
                                    <p>{{ folder.folderSize }}</p>
                                </div>
                            </div>
                        </li>
                    </ul>
                    <h6 class="mt-4">Files</h6>
                    <ul class="files">
                        <li class="file-box" v-for="file in files" :key="file">
                            <div class="file-top">
                                <i :class="file.iconClass"></i><i class="fa fa-ellipsis-v f-14 ellips"></i>
                            </div>
                            <div class="file-bottom">
                                <h6>{{ file.fileName }}</h6>
                                <p class="mb-1">{{ file.fileSize }}</p>
                                <p><b>last open : </b>{{ file.lastOpen }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    recentOpenfiles,
    folders,
    files
} from "@/data/filemanager/filemanager.json"
export default {
    data() {
        return {
            recentOpenfiles: recentOpenfiles,
            folders: folders,
            files: files
        }
    },
}
</script>
    