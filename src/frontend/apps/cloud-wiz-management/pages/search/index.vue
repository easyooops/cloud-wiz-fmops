<template>
    <Breadcrumbs title="Search Website" main="App" />
    <div class="container-fluid search-page">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <form class="theme-form">
                            <div class="input-group m-0 flex-nowrap">
                                <input class="form-control-plaintext" type="search" placeholder="Pixelstrap .."><span
                                    class="btn btn-primary input-group-text">Search</span>
                            </div>
                        </form>
                    </div>
                    <div class="card-body">
                        <div class="text-center">
                            <ul class="nav nav-tabs search-list" id="top-tab" role="tablist">
                                <li class="nav-item" v-on:click="changetab('all')">
                                    <a class="nav-link " :class="{ 'show active': showtab == 'all' }" id="top-all"
                                        data-bs-toggle="tab" role="tab" aria-controls="all" aria-selected="false"><i
                                            class="icon-target"></i>All</a>
                                </li>
                                <li class="nav-item" v-on:click="changetab('images')">
                                    <a class="nav-link" :class="{ 'show active': showtab == 'images' }" id="top-images"
                                        data-toggle="tab" role="tab" aria-controls="images" aria-selected="false"><i
                                            class="icon-image"></i>Images </a>
                                </li>
                                <li class="nav-item" v-on:click="changetab('videos')">
                                    <a class="nav-link" :class="{ 'show active': showtab == 'videos' }" id="top-videos"
                                        data-toggle="tab" role="tab" aria-controls="videos" aria-selected="false"><i
                                            class="icon-video-clapper"></i>Videos</a>
                                </li>
                                <li class="nav-item" v-on:click="changetab('audio')">
                                    <a class="nav-link" :class="{ 'show active': showtab == 'audio' }" id="audios-link"
                                        data-toggle="tab" role="tab" aria-controls="maps" aria-selected="false"><i
                                            class="icon-map-alt"> </i>Audios</a>
                                </li>
                                <li class="nav-item bg-light-success" v-on:click="changetab('settings')">
                                    <a class="nav-link txt-success" :class="{ 'show active': showtab == 'settings' }"
                                        id="setting-link" data-toggle="tab" role="tab" aria-controls="settings"
                                        aria-selected="false">Settings</a>
                                </li>
                                <li class="nav-item bg-light-secondary" v-on:click="changetab('tools')"><a
                                        class="nav-link txt-secondary" :class="{ 'show active': showtab == 'settings' }"
                                        id="setting-link" data-bs-toggle="tab" href="#tools-links" role="tab"
                                        aria-selected="false">Tools</a></li>
                            </ul>
                        </div>
                        <div class="tab-content" id="top-tabContent">
                            <div class="search-links tab-pane fade" :class="{ 'show active': showtab == 'all' }"
                                id="all-links" role="tabpanel" aria-labelledby="all">
                                <allView />
                            </div>
                            <div class="tab-pane fade" :class="{ 'show active': showtab == 'images' }" id="about"
                                role="tabpanel" aria-labelledby="images">
                                <imagesView />
                            </div>
                            <div class="tab-pane fade" :class="{ 'show active': showtab == 'videos' }" id="friends"
                                role="tabpanel" aria-labelledby="videos">
                                <videoView />
                            </div>
                            <div class="tab-pane fade" :class="{ 'show active': showtab == 'audio' }" id="friends"
                                role="tabpanel" aria-labelledby="maps">
                                <videoView />
                            </div>
                            <div class="tab-pane fade" :class="{ 'show active': showtab == 'settings' }" id="photos"
                                role="tabpanel" aria-labelledby="settings">
                                <videoView />
                            </div>
                            <div class="tab-pane fade" :class="{ 'show active': showtab == 'tools' }" id="photos"
                                role="tabpanel" aria-labelledby="settings">
                                <videoView />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import allView from "@/components/search/allView.vue"
import imagesView from "@/components/search/imagesView.vue"
import videoView from "@/components/search/videoView.vue"
export default {
    components: {
        allView, imagesView, videoView
    },
    data() {
        return {
            showtab: 'all',
        }
    },
    methods: {
        changetab(tab) {
            this.showtab = tab;
        }
    }
}
</script>