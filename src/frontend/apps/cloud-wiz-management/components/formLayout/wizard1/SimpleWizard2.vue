<template>
    <div class="col-md-12">
        <div class="card">
            <div class="card-header">
                <h3>Simple Form Wizard</h3><span>Please Make sure fill all the filed before click on next button</span>
            </div>
            <div class="card-body">
                <Wizard :custom-tabs="[
                    {

                        title: 'Registration',
                    },
                    {

                        title: 'Email',
                    },
                    {

                        title: 'Birth Date',
                    },
                ]" :beforeChange="onTabBeforeChange" @change="onChangeCurrentTab" @complete:wizard="wizardCompleted"
                    @submit.prevent="onSubmit">
                    <div class="col-xs-12" v-if="currentTabIndex === 0">
                        <personal />
                    </div>
                    <div class="col-xs-12 text-start" v-if="currentTabIndex === 1">
                        <div class="col-md-12">
                            <div class="form-group">
                                <label class="control-label">Email</label>
                                <input class="form-control" type="text" placeholder="name@example.com"
                                    required="required" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Password</label>
                                <input class="form-control" type="password" placeholder="Password" required="required" />
                            </div>
                        </div>
                    </div>
                    <div class="col-xs-12 text-start" v-if="currentTabIndex === 2">
                        <div class="col-md-12">
                            <div class="form-group">
                                <label class="control-label">Birth date</label>
                                <input class="form-control" type="date" required="required" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Have Passport</label>
                                <input class="form-control" type="text" placeholder="yes/No" required="required" />
                            </div>
                        </div>
                    </div>
                </Wizard>
            </div>
        </div>
    </div>
</template>

<script>
import personal from "./personalPage2.vue";
import "form-wizard-vue3/dist/form-wizard-vue3.css";
import Wizard from "form-wizard-vue3";
export default {
    name: "App",
    components: {
        Wizard,
        personal,
    },
    data() {
        return {
            currentTabIndex: 0,
        };
    },
    methods: {
        onChangeCurrentTab(index, oldIndex) {
            this.currentTabIndex = index;
        },
        onTabBeforeChange() {
            if (this.currentTabIndex === 0) {
            }
        },
        wizardCompleted() {
        },
    },
};
</script>
