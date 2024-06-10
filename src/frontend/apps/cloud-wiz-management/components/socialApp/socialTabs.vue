<template>
    <div class="col-sm-12 box-col-12">
        <div class="card">
            <div class="social-tab">
                <ul class="nav nav-tabs " id="top-tab" role="tablist">
                    <li class="nav-item" v-on:click="changetab('timeline')">
                        <a class="nav-link " :class="{ 'show active': showtab == 'timeline' }" id="top-timeline"
                            data-bs-toggle="tab" role="tab" aria-controls="timeline" aria-selected="false">
                            <vue-feather type="clock"></vue-feather>Timline
                        </a>
                    </li>
                    <li class="nav-item" v-on:click="changetab('about')">
                        <a class="nav-link" :class="{ 'show active': showtab == 'about' }" id="top-about" data-toggle="tab"
                            role="tab" aria-controls="about" aria-selected="false">
                            <vue-feather type="alert-circle"></vue-feather>About
                        </a>
                    </li>
                    <li class="nav-item" v-on:click="changetab('friends')">
                        <a class="nav-link" :class="{ 'show active': showtab == 'friends' }" id="top-friends"
                            data-toggle="tab" role="tab" aria-controls="friends" aria-selected="false">
                            <vue-feather type="users"></vue-feather>Friends
                        </a>
                    </li>
                    <li class="nav-item" v-on:click="changetab('photos')">
                        <a class="nav-link" :class="{ 'show active': showtab == 'photos' }" id="top-photos"
                            data-toggle="tab" role="tab" aria-controls="photos" aria-selected="false">
                            <vue-feather type="image"></vue-feather>Photos
                        </a>
                    </li>
                </ul>
                <div class="input-group">
                    <input class="form-control" type="text" placeholder="Search......."><span class="input-group-text"> <i
                            class="fa fa-search"></i></span>
                </div>
            </div>
        </div>
    </div>
    <div class="tab-content" id="top-tabContent">
        <div class="tab-pane fade" :class="{ 'show active': showtab == 'timeline' }" id="timeline" role="tabpanel"
            aria-labelledby="timeline">
            <SocialAppTimelineMyProfile />
        </div>
        <div class="tab-pane fade" :class="{ 'show active': showtab == 'about' }" id="about" role="tabpanel"
            aria-labelledby="about">
            <SocialAppAboutIndexAbout />
        </div>
        <div class="tab-pane fade" :class="{ 'show active': showtab == 'friends' }" id="friends" role="tabpanel"
            aria-labelledby="friends">
            <SocialAppFriendsPage />
        </div>
        <div class="tab-pane fade" :class="{ 'show active': showtab == 'photos' }" id="photos" role="tabpanel"
            aria-labelledby="photos">
            <SocialAppPhotosPage />
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showtab: 'timeline',
        }
    },
    methods: {
        changetab(tab) {
            this.showtab = tab;
        }
    }
}
</script>
