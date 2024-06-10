<template>
<div class="contact-editform" :style="this.display?{display:'none'}: '' ">
    <form>
        <div class="row g-2">
            <div class="mt-0 mb-3 col-md-12">
                <label>Name</label>
                <div class="row">
                    <div class="col-sm-6">
                        <input class="form-control" id="first_name" type="text" v-model="name" required placeholder="First Name">
                    </div>
                    <div class="col-sm-6">
                        <input class="form-control" id="last_name" type="text" v-model="lastName" required placeholder="Last Name">
                    </div>
                </div>
            </div>
            <div class="mt-0 mb-3 col-md-12">
                <label>Email Address</label>
                <input class="form-control" id="email_add" type="text" v-model="email" required autocomplete="off">
            </div>
            <div class="mt-0 mb-3 col-md-12">
                <label>Phone</label>
                <div class="row">
                    <div class="col-sm-6">
                        <input class="form-control" id="mobile_num" type="text" v-model="mobile" required autocomplete="off">
                    </div>
                    <div class="col-sm-6">
                        <select class="form-control">
                            <option>Mobile</option>
                            <option>Work</option>
                            <option>Others</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>

        <button class="btn btn-secondary update-contact" type="button" @click="saved()">Save</button>
        <button class="btn btn-primary" type="button" @click="cancel()">Cancel</button>
    </form>
</div>
</template>

<script>
import data from '@/data/contact.json'
import { useContactStore } from '~~/store/contact'

export default {
    data() {
        return {
            name: '',
            lastName: '',
            email: '',
            mobile: '',
            menu: data.data
        }
    },
    computed: {
   
        display(){
            return useContactStore().display
        },
        activeTab(){
            return useContactStore().activeTab
        }, 
    },
    methods: {
        saved() {
            useContactStore().change()
            this.menu.filter(item =>{
                if(item.activeTab === this.activeTab){
                    item.name= this.name
                    item.lastName= this.lastName
                    item.email= this.email
                    item.mobile = this.mobile
                }
            })
        },
        cancel(){
            useContactStore().change()
        }
    }
}
</script>
