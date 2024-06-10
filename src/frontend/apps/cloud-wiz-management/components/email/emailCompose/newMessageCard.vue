<template>
<div class="col-xl-8 col-md-12 box-md-12 ps-0">
    <div class="email-right-aside">
        <div class="email-body radius-left">
            <div class="ps-0">
                <div class="tab-content">
                    <div class="tab-pane fade active show" id="pills-darkhome" role="tabpanel" aria-labelledby="pills-darkhome-tab">
                        <div class="email-compose">
                            <div class="email-top compose-border">
                                <div class="row">
                                    <div class="col-sm-8 xl-50">
                                        <h4 class="mb-0">New Message</h4>
                                    </div>
                                    <div class="col-sm-4 btn-middle xl-50">
                                        <button class="btn btn-primary btn-block btn-mail text-center mb-0 mt-0 w-100" type="button"><i class="fa fa-paper-plane me-2"></i> SEND</button>
                                    </div>
                                </div>
                            </div>
                            <div class="email-wrapper">
                                <form class="theme-form">
                                    <div class="mb-3">
                                        <label class="col-form-label pt-0" for="exampleInputEmail1">To</label>
                                        <input class="form-control" id="exampleInputEmail1" type="email">
                                    </div>
                                    <div class="mb-3">
                                        <label for="exampleInputPassword1">Subject</label>
                                        <input class="form-control" id="exampleInputPassword1" type="text">
                                    </div>
                                    <div>
                                        <label class="text-muted">Message</label>
                                        <ClientOnly>
                                            <ckeditor :editor="editor" v-model="editorData"></ckeditor>
                                        </ClientOnly>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                    <composeEmail />
                </div>
            </div>
        </div>
    </div>
</div>
</template>

    
    
<script>
import composeEmail from './composeEmailCard.vue';
import CKEditor from '@ckeditor/ckeditor5-vue';
export default {
    name: 'composeView',
    inject:['ClassicEditor'],
    components: {
        composeEmail,
        ckeditor: CKEditor.component
    },
    data() {
        return {
            type: 'inbox',
            editor: this.ClassicEditor,
            editorData: '<p>Content of the editor.</p>',
            editorConfig: {
                config: {
                    height: '300px'
                }
            },
            menutoogle: false,
        };
    },

}
</script>
