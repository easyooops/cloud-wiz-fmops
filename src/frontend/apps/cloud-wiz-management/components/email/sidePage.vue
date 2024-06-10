<template>
    <div class="col-xl-3 box-col-12">
        <div class="md-sidebar"><a class="btn btn-primary md-sidebar-toggle" href="javascript:void(0)"
                @click="collapseFilter()">email filter</a>
            <div class="md-sidebar-aside job-left-aside custom-scrollbar" :class="filtered ? 'open' : ''">
                <div class="email-left-aside">

                    <div class="card">
                        <div class="card-body">
                            <div class="email-app-sidebar">
                                <div class="media">
                                    <div class="media-size-email"><img class="me-3 rounded-circle"
                                            src="/images/user/user.png" alt=""></div>
                                    <div class="media-body">
                                        <h6 class="f-w-600">MARKJENCO</h6>
                                        <p>Markjecno@gmail.com</p>

                                    </div>
                                </div>
                                <ul class="nav main-menu" role="tablist">
                                    <li class="nav-item"><nuxt-link class="btn-primary btn-block btn-mail show"
                                            id="pills-darkhome-tab" to="/email/compose"><i
                                                class="icofont icofont-envelope me-2"></i> NEW MAIL</nuxt-link></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-import"></i>
                                                Inbox</span><span class="badge pull-right">(236)</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-folder"></i> All
                                                mail</span><span class="badge pull-right">(59)</span></a></li>
                                    <li><nuxt-link to="/email/readMail"><span class="title"><i class="icon-new-window"></i>
                                                Sent</span><span class="badge pull-right">(69)</span></nuxt-link></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-pencil-alt"></i>
                                                DRAFT</span><span class="badge pull-right">(59)</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-trash"></i>
                                                TRASH</span><span class="badge pull-right">(99)</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-info-alt"></i>
                                                IMPORTANT</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-star"></i>
                                                Starred</span></a></li>
                                    <li>
                                        <hr>
                                    </li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-email"></i>
                                                UNREAD</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-export"></i>
                                                SPAM</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-share"></i>
                                                OUTBOX</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-file"></i>
                                                UPDATE</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-bell"></i>
                                                ALERT</span></a></li>
                                    <li><a href="javascript:void(0)"><span class="title"><i class="icon-notepad"></i>
                                                NOTES</span><span class="badge pull-right">(20)</span></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'sidePage',
    data() {
        return {
            filtered: false,
        };
    },
    methods: {
        collapseFilter() {
            this.filtered = !this.filtered
        },
    }
}
</script>