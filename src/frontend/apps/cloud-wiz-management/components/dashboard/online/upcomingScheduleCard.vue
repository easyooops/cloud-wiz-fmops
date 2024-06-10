<template>
    <div class="col-xxl-4 col-ed-6 col-md-7 box-col-7">
        <div class="card schedule-card">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5 class="m-0">Upcoming Schedule</h5>
                    <div class="card-header-right-icon">
                        <a class="btn badge-light-primary" href="#">+ Create</a>
                    </div>
                </div>
            </div>
            <div class="card-body pt-0">
                <ul class="schedule-list">
                    <li class="primary">
                        <img src="/images/dashboard/user/4.jpg" alt="profile" />
                        <div>
                            <h6 class="mb-1">Web Design</h6>
                            <ul>
                                <li class="f-light">
                                    <svg class="fill-icon f-light">
                                        <use href="@/assets/svg/icon-sprite.svg#bag"></use>
                                    </svg><span>January 3, 2022</span>
                                </li>
                                <li class="f-light">
                                    <svg class="fill-icon f-success">
                                        <use href="@/assets/svg/icon-sprite.svg#clock"></use>
                                    </svg><span> 09.00 - 12.00 AM</span>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li class="warning">
                        <img src="/images/dashboard/user/2.jpg" alt="profile" />
                        <div>
                            <h6 class="mb-1">UI/UX Design</h6>
                            <ul>
                                <li class="f-light">
                                    <svg class="fill-icon f-light">
                                        <use href="@/assets/svg/icon-sprite.svg#bag"></use>
                                    </svg><span>Febuary 10, 2022</span>
                                </li>
                                <li class="f-light">
                                    <svg class="fill-icon f-success">
                                        <use href="@/assets/svg/icon-sprite.svg#clock"></use>
                                    </svg><span> 11.00 - 1.00 PM</span>
                                </li>
                            </ul>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
    
<script>
import "@vuepic/vue-datepicker/dist/main.css";
import {
    onlineDashboard
} from "@/data/comon";

export default {
    data() {
        return {
            date1: new Date(),
            onlineDashboard: onlineDashboard,
        };
    },
};
</script>
    