<template>
    <Breadcrumbs main="Page Layout" title="Email Application" />

    <div class="container-fluid">
        <div class="email-wrap">
            <div class="row">
                <sidePage />
                <div class="col-xl-9 col-md-12 xl-70 box-col-70">
                    <div class="email-right-aside">
                        <div class="card email-body">
                            <div class="email-profile">
                                <div class="email-right-aside">
                                    <div class="email-body">
                                        <div class="email-content">
                                            <div class="email-top">
                                                <div class="row">
                                                    <div class="col-xl-12">
                                                        <div class="d-flex"><img class="me-3 rounded-circle"
                                                                src="/images/user/user.png" alt="">
                                                            <div class="flex-grow-1">
                                                                <h6 class="d-block">Kori Thomas</h6>
                                                                <p>Inquiry about our theme pages design.</p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="email-wrapper">
                                                <div class="emailread-group">
                                                    <div class="read-group">
                                                        <p>Hello</p>
                                                        <p>Dear Sir Good Morning,</p>
                                                    </div>
                                                    <div class="read-group">
                                                        <h3>Inquiry about our theme pages design.</h3>
                                                        <p>Cuba Admin is a full featured, multipurpose, premium bootstrap
                                                            admin template built with Bootstrap 5 Framework, HTML5, CSS and
                                                            JQuery.It has a huge collection of reusable UI components and
                                                            integrated with latest jQuery plugins.</p>
                                                        <p class="m-t-10">It can be used for all type of Web applications
                                                            like custom admin panel, app backend, CMS or CRM. UI components
                                                            and integrated with latest jQuery plugins. Tivo Admin is a full
                                                            featured, multipurpose, premium bootstrap admin template built
                                                            with Bootstrap 5 Framework.</p>
                                                    </div>
                                                </div>
                                                <div class="emailread-group">
                                                    <h6 class="text-muted"><i class="icofont icofont-clip"></i> ATTACHMENTS
                                                    </h6><a class="text-muted text-end right-download font-primary f-w-600"
                                                        href="javascript:void(0)"><i
                                                            class="fa fa-long-arrow-down me-2"></i>Download All</a>
                                                    <div class="clearfix"></div>
                                                    <div class="attachment">
                                                        <ul class="list-inline">
                                                            <li class="list-inline-item"><img class="img-fluid"
                                                                    src="/images/email/1.jpg" alt=""></li>
                                                            <li class="list-inline-item"><img class="img-fluid"
                                                                    src="/images/email/2.jpg" alt=""></li>
                                                            <li class="list-inline-item"><img class="img-fluid"
                                                                    src="/images/email/3.jpg" alt=""></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                                <div class="emailread-group">
                                                    <textarea class="form-control" rows="4" cols="50"
                                                        placeholder="write about your nots"></textarea>
                                                    <div class="action-wrapper">
                                                        <ul class="actions">
                                                            <li><a class="btn btn-primary" href="javascript:void(0)"><i
                                                                        class="fa fa-reply me-2"></i>Reply</a></li>
                                                            <li><a class="btn btn-secondary" href="javascript:void(0)"><i
                                                                        class="fa fa-reply-all me-2"></i>Reply All</a></li>
                                                            <li><a class="btn btn-danger" href="javascript:void(0)"><i
                                                                        class="fa fa-share me-2"></i>Forward</a></li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

  
<script>
import sidePage from '../sidePage'
export default {
    name: 'readMail',
    components: {
        sidePage
    }
}
</script>
