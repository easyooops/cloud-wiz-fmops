<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Order</h5>
            </div>
            <div class="card-body grid-showcase">
                <p>Use <code>.order-</code> classes for controlling the <strong>visual order</strong> of your content. These
                    classes are responsive, so you can set the <code>order</code> by breakpoint (e.g.,
                    <code>.order-1.order-md-2</code>). Includes support for <code>1</code> through <code>12</code> across
                    all five grid tiers.</p>
                <div class="row">
                    <div class="col"><span>First, but unordered</span></div>
                    <div class="col order-12"><span>Second, but last</span></div>
                    <div class="col order-1"><span>Third, but first</span></div>
                </div>
                <div class="row">
                    <div class="col order-last"><span>First, but last</span></div>
                    <div class="col"><span>Second, but unordered</span></div>
                    <div class="col order-first"><span>Third, but first</span></div>
                </div>
            </div>
        </div>
    </div></template>
    