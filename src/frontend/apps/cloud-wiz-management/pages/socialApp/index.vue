<template>
    <Breadcrumbs title="Social App" main="App" />
    <div class="container-fluid">
        <div class="user-profile social-app-profile ">
            <div class="row">
                <SocialAppHeaderPage />
            </div>
        </div>

        <div class="tab-content" id="top-tabContent">
            <SocialAppTimeline />

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

    </div>
</template>
<script>
</script>