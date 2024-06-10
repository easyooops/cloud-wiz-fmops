<template>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modal title</h5>
                <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body grid-showcase">
                <div class="container-fluid bd-example-row">
                    <div class="row">
                        <div class="col-md-4"><span>.col-md-4</span></div>
                        <div class="col-md-4 ms-auto"><span>.col-md-4 .ms-auto</span></div>
                    </div>
                    <div class="row">
                        <div class="col-md-3 ms-auto"><span>.col-md-3 .ms-auto</span></div>
                        <div class="col-md-2 ms-auto"><span>.col-md-2 .ms-auto</span></div>
                    </div>
                    <div class="row">
                        <div class="col-md-6 ms-auto"><span>.col-md-6 .ms-auto</span></div>
                    </div>
                    <div class="row">
                        <div class="col-sm-9"><span>Level 1: .col-sm-9</span>
                            <div class="row">
                                <div class="col-8 col-sm-6"><span>Level 2: .col-8 .col-sm-6</span></div>
                                <div class="col-4 col-sm-6"><span>Level 2: .col-4 .col-sm-6</span></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                <button class="btn btn-primary" type="button">Save changes</button>
            </div>
        </div>
    </div>
</template>