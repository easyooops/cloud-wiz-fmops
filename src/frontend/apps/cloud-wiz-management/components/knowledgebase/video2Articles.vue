<template>
    <div class="col-xl-4">
        <div class="row">
            <div class="col-xl-12 col-md-6">
                <px-card :actions="false">
                    <template v-slot:with-padding>
                        <div class="media">
                            <vue-feather type="youtube" class="m-r-30"></vue-feather>
                            <div class="media-body">
                                <h6 class="f-w-600">Vel illum qu</h6>
                                <p>
                                    Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                                </p>
                            </div>
                        </div>
                    </template>
                </px-card>
            </div>
            <div class="col-xl-12 col-md-6">
                <px-card :actions="false">
                    <template v-slot:with-padding>
                        <div class="media">
                            <vue-feather type="youtube" class="m-r-30"></vue-feather>
                            <div class="media-body">
                                <h6 class="f-w-600">Cum sociis natoqu</h6>
                                <p>
                                    Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                                </p>
                            </div>
                        </div>
                    </template>
                </px-card>
            </div>
            <div class="col-xl-12">
                <px-card :actions="false">
                    <template v-slot:with-padding>
                        <div class="media">
                            <vue-feather type="youtube" class="m-r-30"></vue-feather>
                            <div class="media-body">
                                <h6 class="f-w-600">Donec pede justo</h6>
                                <p>
                                    Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
                                </p>
                            </div>
                        </div>
                    </template>
                </px-card>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from 'pinia';
import { useCommonStore } from '~~/store/common';
import pxcard from '../Pxcard.vue'
export default {
    components: {
        'px-card': pxcard
    },
    data() {
        return {};
    },
    computed: {
        ...mapState(useCommonStore, {
            knowledgebasedata: 'knowledgebasedata',
        }),
    },
};
</script>