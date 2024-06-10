<template>
    <div class="col-sm-12">
        <div class="header-faq">
            <h5 class="mb-0">Browse articles by category</h5>
        </div>
        <div class="row">
            <div class="col-sm-12">
                <px-card title="Browse Articles" :actions="false">
                    <template v-slot:with-padding>
                        <div class="row browse g-sm-4 g-3">
                            <div class="col-xl-4 xl-50 col-md-6" v-for="(item, index) in knowledgebasedata" :key="index">
                                <div class="browse-articles">
                                    <h6>
                                        <span><vue-feather type="archive"></vue-feather></span>{{ item.title }}
                                    </h6>
                                    <ul>
                                        <li>
                                            <a href="#"><span><vue-feather type="file-text"></vue-feather> </span><span> {{
                                                item.text1 }}
                                                </span></a>
                                        </li>
                                        <li>
                                            <a href="#"><span><vue-feather type="file-text"></vue-feather> </span><span> {{
                                                item.text2 }}
                                                </span>
                                                <span class="badge badge-primary pull-right" v-if="item.text2_badge">
                                                    {{ item.text2_badge }}
                                                </span></a>
                                        </li>
                                        <li>
                                            <a href="#"><span><vue-feather type="file-text"></vue-feather> </span><span> {{
                                                item.text3 }}
                                                </span></a>
                                        </li>
                                        <li>
                                            <a href="#"><span><vue-feather type="file-text"></vue-feather> </span><span> {{
                                                item.text4 }}
                                                </span></a>
                                        </li>
                                        <li>
                                            <a href="#"><span><vue-feather type="arrow-right"></vue-feather> </span><span>
                                                    {{ item.text5
                                                    }} </span></a>
                                        </li>
                                    </ul>
                                </div>
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
import pxcard from '../Pxcard.vue'
import { useCommonStore } from '~~/store/common'
export default {
    components: {
        'px-card': pxcard,
    },
    data() {
        return {};
    },
    computed: {
        ...mapState(useCommonStore, {
            knowledgebasedata: 'knowledgebasedata'
        }),
    },
};
</script>