<template>
    <div class="col-xxl-5 col-lg-12 col-md-12 box-col-8 col-ed-6">
        <div class="card papernote-wrap">
            <div class="card-header card-no-border">
                <div class="header-top">
                    <h5>Paper Note</h5>
                    <a class="f-light d-flex align-items-center" href="#">View project <i
                            class="f-w-700 icon-arrow-top-right"></i></a>
                </div>
            </div>
            <div class="card-body pt-0">
                <img class="banner-img img-fluid" src="/images/dashboard/papernote.jpg" alt="multicolor background" />
                <div class="note-content mt-sm-4 mt-2">
                    <p>
                        You should be able to look beautiful and feel good with little
                        effort thanks to design and elegance.
                    </p>
                    <div class="note-labels">
                        <ul>
                            <li v-for="item in paperNotes" :key="item">
                                <span :class="item.labelClass">{{ item.label }}</span>
                            </li>
                        </ul>
                        <div class="last-label">
                            <span class="badge badge-light-success">Inprogress</span>
                        </div>
                    </div>
                    <div class="mt-sm-4 mt-2 user-details">
                        <div class="customers">
                            <ul>
                                <li class="d-inline-block" v-for="customer in customers" :key="customer">
                                    <img class="img-40 rounded-circle" :src="getImgURL(customer.image)" alt="user" />
                                </li>
                                <li class="d-inline-block">
                                    <div class="light-card">
                                        <span class="f-w-500">+5</span>
                                    </div>
                                </li>
                            </ul>
                        </div>
                        <div class="d-flex align-items-center">
                            <h5 class="mb-0 font-primary f-18 me-1">$239,098</h5>
                            <span class="f-light f-w-500">(Budget)</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
    
<script>
import {
    paperNotes,
    customers
} from "@/data/dashboard/default.json"
export default {
    data() {
        return {
            paperNotes: paperNotes,
            customers: customers
        };
    },
    methods: {
        getImgURL(path) {
            return '/images/dashboard/' + path
        }
    }
};
</script>
    