<template>
    <div class="col-xxl-5 col-ed-6 col-xl-8 box-col-7">
        <div class="row">
            <div class="col-sm-12">
                <div class="card o-hidden welcome-card">
                    <div class="card-body">
                        <h4 class="mb-3 mt-1 f-w-500 mb-0 f-22">
                            Hello Jashmin<span>
                                <img src="/images/dashboard-3/hand.svg" alt="hand vector" /></span>
                        </h4>
                        <p>
                            Learn something new every day with world's best courses.Free
                            online courses available.
                        </p>
                    </div>
                    <img class="welcome-img" src="/images/dashboard-3/widget.svg" alt="search image" />
                </div>
            </div>
            <div class="col-sm-6">
                <div class="card course-box">
                    <div class="card-body">
                        <div class="course-widget">
                            <div class="course-icon">
                                <svg class="fill-icon">
                                    <use href="@/assets/svg/icon-sprite.svg#course-1"></use>
                                </svg>
                            </div>
                            <div>
                                <h4 class="mb-0">100+</h4>
                                <span class="f-light">Completed Courses</span><a class="btn btn-light f-light">
                                    <NuxtLink to="/learning/list">View course<span class="ms-2">
                                            <svg class="fill-icon f-light">
                                                <use href="@/assets/svg/icon-sprite.svg#arrowright"></use>
                                            </svg></span></NuxtLink>
                                </a>
                            </div>
                        </div>
                    </div>
                    <ul class="square-group">
                        <li class="square-1 warning"></li>
                        <li class="square-1 primary"></li>
                        <li class="square-2 warning1"></li>
                        <li class="square-3 danger"></li>
                        <li class="square-4 light"></li>
                        <li class="square-5 warning"></li>
                        <li class="square-6 success"></li>
                        <li class="square-7 success"></li>
                    </ul>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="card course-box">
                    <div class="card-body">
                        <div class="course-widget">
                            <div class="course-icon warning">
                                <svg class="fill-icon">
                                    <use href="@/assets/svg/icon-sprite.svg#course-2"></use>
                                </svg>
                            </div>
                            <div>
                                <h4 class="mb-0">50+</h4>
                                <span class="f-light">In Progress Courses</span><a class="btn btn-light f-light">
                                    <NuxtLink to="/learning/list">View course<span class="ms-2">
                                            <svg class="fill-icon f-light">
                                                <use href="@/assets/svg/icon-sprite.svg#arrowright"></use>
                                            </svg></span></NuxtLink>
                                </a>
                            </div>
                        </div>
                    </div>
                    <ul class="square-group">
                        <li class="square-1 warning"></li>
                        <li class="square-1 primary"></li>
                        <li class="square-2 warning1"></li>
                        <li class="square-3 danger"></li>
                        <li class="square-4 light"></li>
                        <li class="square-5 warning"></li>
                        <li class="square-6 success"></li>
                        <li class="square-7 success"></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
export default {

}
</script>
    