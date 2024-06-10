<template>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5>Progress Bars animated</h5><span>The striped gradient can also be animated. Add
                    <code>.progress-bar-animated</code> to <code>.progress-bar </code> to animate the stripes right to left
                    via CSS3 animations.</span>
            </div>
            <div class="card-body progress-showcase row">
                <div class="col">
                    <div class="progress">
                        <div class="progress-bar-animated bg-primary progress-bar-striped" role="progressbar"
                            style="width: 10%" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress">
                        <div class="progress-bar-animated progress-bar-striped bg-secondary" role="progressbar"
                            style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress">
                        <div class="progress-bar-animated progress-bar-striped bg-success" role="progressbar"
                            style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <div class="progress">
                        <div class="progress-bar-animated progress-bar-striped bg-info" role="progressbar"
                            style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
            </div>
        </div>
    </div>
</div></template>