<template>
    <Breadcrumbs main="Page Layout" title="Email Compose" />

    <div class="container-fluid">
        <div class="email-wrap">
            <div class="row">
                <sidePage />
                <div class="col-xl-9 box-col-12">
                    <div class="email-right-aside">
                        <div class="card email-body">
                            <div class="row">
                                <indexCard />
                                <newMessageCard />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import sidePage from '../sidePage.vue'
import indexCard from './indexCard.vue'
import newMessageCard from './newMessageCard.vue'
import {
    inboxData
} from "@/data/email/email.json"

export default {
    name: 'composeView',
    components: {
        sidePage,
        indexCard,
        newMessageCard

    },
}
</script>
  
