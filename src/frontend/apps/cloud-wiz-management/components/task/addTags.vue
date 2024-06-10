<template>
    <li><span class="main-title"> Tags<span class="pull-right"><a href="javascript:void(0)" data-bs-toggle="modal" data-bs-target="#createtag"><vue-feather type="plus-circle"></vue-feather></a></span></span>
        <div class="modal fade modal-bookmark" id="createtag" tabindex="-1" role="dialog" aria-hidden="true">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 class="modal-title">Create Tag</h3>
                        <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form class="form-bookmark needs-validation" >
                            <div class="form-row">
                                <div class="form-group col-md-12">
                                    <label>Tag Name</label>
                                    <input class="form-control" type="text"  autocomplete="off">
                                </div>
                                <div class="form-group col-md-12 mb-0">
                                    <label>Tag color</label>
                                    <input class="form-control fill-color" type="color" value="#534686">
                                </div>
                            </div>
                            <button class="btn btn-secondary" type="button">Save</button>
                            <button class="btn btn-primary" type="button" data-bs-dismiss="modal">Cancel</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </li>
</template>