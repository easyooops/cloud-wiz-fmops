<template>
    <div class="card mb-0">
        <div class="card-header d-flex">
            <h5>Personal</h5><span class="f-14 pull-right mt-0">{{ menu.length }} Contacts</span>
        </div>
        <div class="card-body p-0">
            <div class="row list-persons" id="addcon">
                <div class="col-xl-4 xl-50 col-md-5">
                    <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                        <a class="contact-tab-0 nav-link" :class="this.activeTab == item.activeTab ? 'active show' : ''"
                            id="v-pills-user-tab" data-bs-toggle="pill" @click="activeDiv(item.activeTab)"
                            href="#v-pills-user" role="tab" aria-controls="v-pills-user" aria-selected="true"
                            v-for="(item, index) in menu" :key="index">
                            <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle update_img_0"
                                    :src="item.imgUrl || getImgUrl(item.img)" alt="">
                                <div class="media-body">
                                    <h6> <span class="first_name_0">{{ item.name }} </span><span class="last_name_0">{{
                                        item.lastName }}</span></h6>
                                    <p class="email_add_0">{{ item.email }}</p>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-xl-8 xl-50 col-md-7">
                    <div class="tab-content" id="v-pills-tabContent" :style="!this.display ? { display: 'none' } : ''">
                        <div class="tab-pane contact-tab-0 tab-content-child fade show"
                            :class="item.activeTab === this.activeTab ? 'active' : ''" id="v-pills-user" role="tabpanel"
                            aria-labelledby="v-pills-user-tab" v-for="(item, index) in menu" :key="index">
                            <div class="profile-mail" v-if="this.activeTab == item.activeTab">
                                <div class="media">
                                    <img class="img-100 img-fluid m-r-20 rounded-circle update_img_0"
                                        :src="item.imgUrl || getImgUrl(item.img)" alt="">
                                    <input class="updateimg" type="file" name="img" @change="(e) => { readURL(e, item) }">
                                    <div class="media-body mt-0">
                                        <h3><span class="first_name_0">{{ item.name }} </span><span class="last_name_0">{{
                                            item.lastName }}</span></h3>
                                        <p class="email_add_0">{{ item.email }}</p>
                                        <ul>
                                            <li><a href="javascript:void(0)" @click="editContact()">Edit</a> </li>
                                            <li><a href="javascript:void(0)" @click="deleteContact(index)">Delete</a></li>
                                            <historyPage />
                                            <li><a href="javascript:void(0)" @click="printContact(item)"
                                                    data-bs-toggle="modal" data-bs-target="#printModal">Print</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="email-general">
                                    <h4 class="mb-3">General</h4>
                                    <ul>
                                        <li>Name <span class="font-primary first_name_0">{{ item.name }}</span></li>
                                        <li>Gender <span class="font-primary">{{ item.gender }}</span></li>
                                        <li>Birthday<span class="font-primary"> <span class="birth_day_0">18</span><span
                                                    class="birth_month_0 ms-1">May</span><span
                                                    class="birth_year_0 ms-1">1994</span></span></li>
                                        <li>Personality<span class="font-primary personality_0">Cool</span></li>
                                        <li>City<span class="font-primary city_0">moline acres</span></li>
                                        <li>Mobile No<span class="font-primary mobile_num_0">{{ item.mobile }}</span></li>
                                        <li>Email Address <span class="font-primary email_add_0">barnes@gmail.com </span>
                                        </li>
                                        <li>Website<span class="font-primary url_add_0">www.test.com</span></li>
                                        <li>Interest<span class="font-primary interest_0">photography</span></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <editPage />
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import data from '@/data/contact.json'
import historyPage from './historyPage.vue'
import editPage from './editPage.vue'
import { useContactStore } from '~~/store/contact'
export default {
    components: {
        historyPage, editPage
    },
    data() {
        return {
            data: data,
            url: null,
            lastModified: null
        }
    },
    computed: {
        display() {
            return useContactStore().display
        },
        activeTab() {
            return useContactStore().activeTab
        },
        selectedUser() {
            return useContactStore().selectedUser
        },
        menu() {
            return this.data.data
        }
    },
    methods: {
        readURL(e, item) {
            var files = e.target.files[0];
            this.url = URL.createObjectURL(files)
            item.imgUrl = this.url
        },
        activeDiv(item) {
            useContactStore().active(item)
        },
        printContact(item) {
            useContactStore().print(item)
        },
        getImgUrl(path) {
            return ('/images/' + path)
        },
        editContact() {
            useContactStore().change()

        },
        deleteContact: function (items) {
            this.$swal({
                icon: 'warning', title: "Are you sure?",
                text: 'Once deleted, you will not be able to recover this imaginary file!',
                showCancelButton: true, confirmButtonText: 'Ok', confirmButtonColor: '#e64942',
                cancelButtonText: 'Cancel', cancelButtonColor: '#efefef',
            }).then((result) => {
                if (result.value) {
                    this.menu.splice(items, 1)
                    useContactStore().active(this.menu[items].activeTab)
                    this.$swal({
                        icon: 'success',
                        text: 'Poof! Your imaginary file has been deleted!',
                        type: 'success',
                    });
                } else {
                    this.$swal({
                        text: 'Your imaginary file is safe!'
                    });
                }
            });
        },
    }
}
</script>
