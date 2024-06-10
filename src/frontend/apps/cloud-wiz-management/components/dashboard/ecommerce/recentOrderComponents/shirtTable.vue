<template>
    <div class="recent-table table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <th class="f-light">Item</th>
                    <th class="f-light">Qty</th>
                    <th class="f-light">Price</th>
                    <th class="f-light">Status</th>
                    <th class="f-light">Total Price</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <div class="product-content">
                            <div class="order-image">
                                <img src="/images/dashboard-2/order/sub-product/4.png" alt="t-shirt" />
                            </div>
                            <div>
                                <h6 class="f-14 mb-0">
                                    <a>
                                        <NuxtLink to="/ecommerce/order/history">T-shirt</NuxtLink>
                                    </a>
                                </h6>
                                <span class="f-light f-12">Id : #CFDE-2163</span>
                            </div>
                        </div>
                    </td>
                    <td class="f-w-500">X1</td>
                    <td class="f-w-500">$56.00</td>
                    <td class="f-w-500">
                        <div class="recent-status font-success">
                            <svg class="me-1">
                                <use href="@/assets/svg/icon-sprite.svg#24-hour"></use>
                            </svg>Verified
                        </div>
                    </td>
                    <td class="f-w-500">$100.00</td>
                </tr>
                <tr>
                    <td>
                        <div class="product-content">
                            <div class="order-image">
                                <img src="/images/dashboard-2/order/sub-product/3.png" alt="t-shirt" />
                            </div>
                            <div>
                                <h6 class="f-14 mb-0">
                                    <a>
                                        <NuxtLink to="/ecommerce/order/history">Pink T-shirt</NuxtLink>
                                    </a>
                                </h6>
                                <span class="f-light f-12">Id : #CFDE-2780</span>
                            </div>
                        </div>
                    </td>
                    <td class="f-w-500">X2</td>
                    <td class="f-w-500">$156.00</td>
                    <td class="f-w-500">
                        <div class="recent-status font-danger">
                            <svg class="me-1">
                                <use href="@/assets/svg/icon-sprite.svg#24-hour"></use>
                            </svg>Rejected
                        </div>
                    </td>
                    <td class="f-w-500">$870.00</td>
                </tr>
            </tbody>
    </table>
</div></template>