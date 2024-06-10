<template>
    <div class="col-sm-6">
                    <div class="card">
                        <div class="card-header card-no-border">
                            <div class="header-top gap-1">
                                <h5>Buy Coins</h5>
                                <div class="dropdown icon-dropdown">
                                    <button class="btn dropdown-toggle" id="buydropdown" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                        <i class="icon-more-alt"></i>
                                    </button>
                                    <div class="dropdown-menu dropdown-menu-end" aria-labelledby="buydropdown">
                                        <a class="dropdown-item" href="#">Weekly</a><a class="dropdown-item" href="#">Monthly</a><a class="dropdown-item" href="#">Yearly</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="card-body pt-0">
                            <form class="theme-form crypto-form">
                                <div class="mb-3">
                                    <label class="form-label f-light" for="money">Enter your Money</label>
                                    <div class="position-relative">
                                        <input class="form-control" id="money" type="number" placeholder="100" />
                                        <select class="form-select crypto-select warning">
                                            <option>USD</option>
                                            <option>BTC</option>
                                            <option>LTC</option>
                                            <option>ETH</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="mb-3">
                                    <label class="form-label f-light" for="coin">Enter Coins Converted to</label>
                                    <div class="position-relative">
                                        <input class="form-control" id="coin" type="number" placeholder="0.0043" />
                                        <select class="form-select crypto-select primary">
                                            <option>BTC</option>
                                            <option>USD</option>
                                            <option>LTC</option>
                                            <option>ETH</option>
                                        </select>
                                    </div>
                                </div>
                                <button class="btn btn-primary btn-hover-effect w-100" type="button">
                                    Buy Coins
                                </button>
                            </form>
                        </div>
                    </div>
                </div>
</template>