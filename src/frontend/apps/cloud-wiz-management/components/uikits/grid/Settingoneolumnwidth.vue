<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Setting one column width</h5>
            </div>
            <div class="card-body grid-showcase">
                <p>Auto-layout for flexbox grid columns also means you can set the width of one column and have the sibling
                    columns automatically resize around it. You may use predefined grid classes (as shown below), grid
                    mixins, or inline widths. Note that the other columns will resize no matter the width of the center
                    column.</p>
                <div class="row">
                    <div class="col"><span>1 of 3</span></div>
                    <div class="col-6"><span>2 of 3 (wider)</span></div>
                    <div class="col"><span> 3 of 3</span></div>
                </div>
                <div class="row">
                    <div class="col"><span>1 of 3</span></div>
                    <div class="col-5"><span> 2 of 3 (wider)</span></div>
                    <div class="col"><span>3 of 3</span></div>
                </div>
            </div>
        </div>
    </div></template>
    