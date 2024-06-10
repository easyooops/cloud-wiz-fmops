<template>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5>Custom Height Progress Bars</h5><span>Set a height value on the <code>.progress-bar</code>, so if you
                    change that value the outer <code>.progress </code> will automatically resize accordingly.</span>
            </div>
            <div class="card-body progress-showcase row">
                <div class="col">
                    <div class="progress" style="height: 1px;">
                        <div class="progress-bar bg-primary" role="progressbar" style="width: 25%" aria-valuenow="25"
                            aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress" style="height: 5px;">
                        <div class="progress-bar bg-secondary" role="progressbar" style="width: 50%" aria-valuenow="50"
                            aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress" style="height: 11px;">
                        <div class="progress-bar bg-success" role="progressbar" style="width: 75%" aria-valuenow="75"
                            aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress" style="height: 19px;">
                        <div class="progress-bar bg-info" role="progressbar" style="width: 100%" aria-valuenow="100"
                            aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>
        </div>
    </div>
</div></template>