<template>
    <div class="row">
        <div class="col">
            <div class="mb-3">
                <label>Project Title</label>
                <input class="form-control" type="text" placeholder="Project name *">
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col">
            <div class="mb-3">
                <label>Client name</label>
                <input class="form-control" type="text" placeholder="Name client or company name">
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-4">
            <div class="mb-3">
                <label>Project Rate</label>
                <input class="form-control" type="text" placeholder="Enter project Rate">
            </div>
        </div>
        <div class="col-sm-4">
            <div class="mb-3">
                <label>Project Type</label>
                <select class="form-select">
                    <option>Hourly</option>
                    <option>Fix price</option>
                </select>
            </div>
        </div>
        <div class="col-sm-4">
            <div class="mb-3">
                <label>Priority</label>
                <select class="form-select">
                    <option>Low</option>
                    <option>Medium</option>
                    <option>High</option>
                    <option>Urgent</option>
                </select>
            </div>
        </div>
    </div>
</template>