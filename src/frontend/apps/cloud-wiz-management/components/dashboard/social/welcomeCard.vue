<template>
    <div class="col-xl-12 col-md-6">
        <div class="card social-profile">
            <div class="card-body">
                <div class="social-img-wrap">
                    <div class="social-img">
                        <img src="/images/dashboard-5/profile.png" alt="profile" />
                    </div>
                    <div class="edit-icon">
                        <svg>
                            <use href="@/assets/svg/icon-sprite.svg#profile-check"></use>
                        </svg>
                    </div>
                </div>
                <div class="social-details">
                    <h5 class="mb-1">
                        <a>
                            <NuxtLink to="/socialApp">Brooklyn Simmons</NuxtLink>
                        </a>
                    </h5>
                    <span class="f-light">@brookly.simmons</span>
                    <ul class="social-follow">
                        <li>
                            <h5 class="mb-0">1,908</h5>
                            <span class="f-light">Posts</span>
                        </li>
                        <li>
                            <h5 class="mb-0">34.0k</h5>
                            <span class="f-light">Followers</span>
                        </li>
                        <li>
                            <h5 class="mb-0">897</h5>
                            <span class="f-light">Following</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
    