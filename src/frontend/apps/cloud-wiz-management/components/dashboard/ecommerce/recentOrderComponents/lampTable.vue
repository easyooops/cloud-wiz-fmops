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
                                <img src="/images/dashboard-2/order/sub-product/9.png" alt="lamp" />
                            </div>
                            <div>
                                <h6 class="f-14 mb-0">
                                    <a>
                                        <NuxtLink to="/ecommerce/order/history">Lamp</NuxtLink>
                                    </a>
                                </h6>
                                <span class="f-light f-12">Id : #CFDE-2163</span>
                            </div>
                        </div>
                    </td>
                    <td class="f-w-500">X1</td>
                    <td class="f-w-500">$20.00</td>
                    <td class="f-w-500">
                        <div class="recent-status font-success">
                            <svg class="me-1">
                                <use href="@/assets/svg/icon-sprite.svg#24-hour"></use>
                            </svg>Verified
                        </div>
                    </td>
                    <td class="f-w-500">$25.00</td>
                </tr>
                <tr>
                    <td>
                        <div class="product-content">
                            <div class="order-image">
                                <img src="/images/dashboard-2/order/sub-product/10.png" alt="lamp" />
                            </div>
                            <div>
                                <h6 class="f-14 mb-0">
                                    <a>
                                        <NuxtLink to="/ecommerce/order/history">Bedside lamp</NuxtLink>
                                    </a>
                                </h6>
                                <span class="f-light f-12">Id : #CFDE-2780</span>
                            </div>
                        </div>
                    </td>
                    <td class="f-w-500">X2</td>
                    <td class="f-w-500">$70.00</td>
                    <td class="f-w-500">
                        <div class="recent-status font-danger">
                            <svg class="me-1">
                                <use href="@/assets/svg/icon-sprite.svg#24-hour"></use>
                            </svg>Rejected
                        </div>
                    </td>
                    <td class="f-w-500">$88.00</td>
                </tr>
            </tbody>
    </table>
</div></template>