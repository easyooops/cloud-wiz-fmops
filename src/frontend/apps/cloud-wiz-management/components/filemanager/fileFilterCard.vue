<template>
    <div class="file-sidebar">
        <div class="card">
            <div class="card-body">
                <ul>
                    <li v-for="sidebar in sidebarMenus" :key="sidebar">
                        <div :class="sidebar.btnClass">
                            <vue-feather :type="sidebar.iconType"></vue-feather>
                            {{ sidebar.title }}
                        </div>
                    </li>
                </ul>
                <hr />
                <ul>
                    <li>
                        <div class="btn btn-outline-primary">
                            <vue-feather type="database"></vue-feather> Storage
                        </div>
                        <div class="m-t-15">
                            <div class="progress sm-progress-bar mb-1">
                                <div class="progress-bar bg-primary" role="progressbar" style="width: 25%"
                                    aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                            <p>25 GB of 100 GB used</p>
                        </div>
                    </li>
                </ul>
                <hr />
                <ul>
                    <li>
                        <div class="btn btn-outline-primary">
                            <vue-feather type="grid"></vue-feather> Pricing plan
                        </div>
                    </li>
                    <li>
                        <div class="pricing-plan">
                            <h6>Trial Version</h6>
                            <h5>FREE</h5>
                            <p>100 GB Space</p>
                            <div class="btn btn-outline-primary btn-xs">Selected</div>
                            <img class="bg-img" src="/images/dashboard/folder.png" alt="" />
                        </div>
                    </li>
                    <li>
                        <div class="pricing-plan">
                            <h6>Premium</h6>
                            <h5>$5/month</h5>
                            <p>200 GB Space</p>
                            <div class="btn btn-outline-primary btn-xs">
                                Contact Us
                            </div>
                            <img class="bg-img" src="/images/dashboard/folder1.png" alt="" />
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    sidebarMenus
} from "@/data/filemanager/filemanager.json"
export default {
    data() {
        return {
            sidebarMenus: sidebarMenus
        }
    },
}
</script>
    