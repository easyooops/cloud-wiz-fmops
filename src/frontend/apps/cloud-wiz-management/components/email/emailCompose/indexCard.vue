<template>
    <div class="col-xl-4 col-md-12 box-md-12 pe-0">
        <div class="pe-0 b-r-light"></div>
        <div class="email-top">
            <div class="row">
                <div class="col">
                    <h5>Inbox</h5>
                </div>
                <div class="col text-end">
                    <div class="dropdown">
                        <button class="btn dropdown-toggle" id="dropdownMenuButton" type="button" data-bs-toggle="dropdown"
                            aria-expanded="false">More</button>
                        <div class="dropdown-menu dropdown-menu-end" aria-labelledby="dropdownMenuButton"><a
                                class="dropdown-item" href="#">Action</a><a class="dropdown-item" href="#">Another
                                action</a><a class="dropdown-item" href="#">Something else here</a></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="inbox custom-scrollbar">
            <div class="media" v-for="inbox in inboxData" :key="inbox">
                <div class="media-size-email"><img class="me-3 rounded-circle" src="/images/user/user.png" alt=""></div>
                <div class="media-body">
                    <h6> {{ inbox.senderName }} <small><span>({{ inbox.sendDate }}</span> {{ inbox.sendMonth }} <span>{{
                        inbox.sendYear }})</span></small></h6>
                    <p> {{ inbox.msg }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    inboxData
} from "@/data/email/email"
export default {
    data() {
        return {
            inboxData: inboxData
        };
    },

}
</script>
    