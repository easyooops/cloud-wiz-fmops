<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Offset</h5>
            </div>
            <div class="card-body grid-showcase">
                <p>Move columns to the right using <code>.offset-md-*</code> classes. These classes increase the left margin
                    of a column by <code>*</code> columns. For example, <code>.offset-md-4</code> moves
                    <code>.col-md-4</code> over four columns.</p>
                <div class="row">
                    <div class="col-md-4"><span>.col-md-4</span></div>
                    <div class="col-md-4 offset-md-4"><span>.col-md-4 .offset-md-4</span></div>
                </div>
                <div class="row">
                    <div class="col-md-3 offset-md-3"><span>.col-md-3 .offset-md-3</span></div>
                    <div class="col-md-3 offset-md-3"><span>.col-md-3 .offset-md-3</span></div>
                </div>
                <div class="row">
                    <div class="col-md-6 offset-md-3"><span>.col-md-6 .offset-md-3</span></div>
                </div>
                <div class="row">
                    <div class="col-sm-5 col-md-6"><span>.col-sm-5 .col-md-6</span></div>
                    <div class="col-sm-5 offset-sm-2 col-md-6 offset-md-0"><span>.col-sm-5 .offset-sm-2 .col-md-6
                            .offset-md-0</span></div>
                </div>
                <div class="row">
                    <div class="col-sm-6 col-md-5 col-lg-6"><span>.col-sm-6 .col-md-5 .col-lg-6</span></div>
                    <div class="col-sm-6 col-md-5 offset-md-2 col-lg-6 offset-lg-0"><span>.col-sm-6 .col-md-5 .offset-md-2
                            .col-lg-6 .offset-lg-0</span></div>
                </div>
            </div>
        </div>
</div></template>
    