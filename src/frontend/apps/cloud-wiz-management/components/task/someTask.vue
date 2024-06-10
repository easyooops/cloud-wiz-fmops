<template>
    <div class="fade tab-pane" id="pills-todaytask" role="tabpanel" aria-labelledby="pills-todaytask-tab">
        <div class="card mb-0">
            <div class="card-header d-flex">
                <h3 class="mb-0">Today's Tasks</h3><a href="javascript:void(0)"><vue-feather class="me-2" type="printer"></vue-feather>Print</a>
            </div>
            <div class="card-body">
                <div class="details-bookmark text-center">
                    <div class="row" id="favouriteData"></div>
                    <div class="no-favourite"><span>No task due today.</span></div>
                </div>
            </div>
        </div>
    </div>
    <div class="fade tab-pane" id="pills-delayed" role="tabpanel" aria-labelledby="pills-delayed-tab">
        <div class="card mb-0">
            <div class="card-header d-flex">
                <h3 class="mb-0">Delayed Tasks</h3><a href="javascript:void(0)"><vue-feather class="me-2" type="printer"></vue-feather>Print</a>
            </div>
            <div class="card-body">
                <div class="details-bookmark text-center"><span>No tasks found.</span></div>
            </div>
        </div>
    </div>
    <div class="fade tab-pane" id="pills-upcoming" role="tabpanel" aria-labelledby="pills-upcoming-tab">
        <div class="card mb-0">
            <div class="card-header d-flex">
                <h3 class="mb-0">Upcoming Tasks</h3><a href="javascript:void(0)"><vue-feather class="me-2" type="printer"></vue-feather>Print</a>
            </div>
            <div class="card-body">
                <div class="details-bookmark text-center"><span>No tasks found.</span></div>
            </div>
        </div>
    </div>
    <div class="fade tab-pane" id="pills-weekly" role="tabpanel" aria-labelledby="pills-weekly-tab">
        <div class="card mb-0">
            <div class="card-header d-flex">
                <h3 class="mb-0">This Week Tasks</h3><a href="javascript:void(0)"><vue-feather class="me-2" type="printer"></vue-feather>Print</a>
            </div>
            <div class="card-body">
                <div class="details-bookmark text-center"><span>No tasks found.</span></div>
            </div>
        </div>
    </div>
    <div class="fade tab-pane" id="pills-monthly" role="tabpanel" aria-labelledby="pills-monthly-tab">
        <div class="card mb-0">
            <div class="card-header d-flex">
                <h3 class="mb-0">This Month Tasks</h3><a href="javascript:void(0)"><vue-feather class="me-2" type="printer"></vue-feather>Print</a>
            </div>
            <div class="card-body">
                <div class="details-bookmark text-center"><span>No tasks found.</span></div>
            </div>
        </div>
    </div>
</template>