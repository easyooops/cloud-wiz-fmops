<template>
    <Breadcrumbs main="Ecommerce" title="Invoice" />

    <div class="container invoice" id="print">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-body">
                        <div>
                            <div>
                                <div class="row invo-header">
                                    <div class="col-sm-6">
                                        <div class="d-flex align-items-center">
                                            <div class="d-flex-left"><img class="d-flex-object img-60"
                                                    src="/images/other-images/logo-login.png" alt=""></div>
                                            <div class="flex-grow-1 m-l-20">
                                                <h4 class="d-flex-headin">Cuba</h4>
                                                <p>hello@cuba.in<br><span class="digits">289-335-6503</span></p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="text-md-end text-xs-center">
                                            <h3>Invoice #<span class="digits counter">1069</span></h3>
                                            <p>Issued: May<span class="digits"> 27, 2023</span><br> Payment Due: June <span
                                                    class="digits">27, 2023</span></p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <hr />
                            <div class="row invo-profile">
                                <div class="col-xl-4">
                                    <div class="invo-profile-left">
                                        <div class="d-flex">
                                            <div class="d-flex-left"><img class="d-flex-object rounded-circle img-60"
                                                    src="/images/user/1.jpg" alt=""></div>
                                            <div class="flex-grow-1 ms-3">
                                                <h4 class="d-flex-heading">Johan Deo</h4>
                                                <p>JohanDeo@gmail.com<br /><span class="digits">555-555-5555</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-8">
                                    <div class="invo-profile-right">
                                        <div id="project" class="text-xl-end">
                                            <h6>Project Description</h6>
                                            <p>You're only as good as your last collection, which is an enormous pressure.
                                                Jeans represent democracy in fashion. Fashion is about dressing according to
                                                what's fashionable.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <invoiceTable />
                                <div class="row mt-3">
                                    <div class="col-md-8">
                                        <div>
                                            <p class="legal"><strong>Thank you for your business!</strong>Payment is
                                                expected within 31 days; please process this invoice within that time. There
                                                will be a 5% interest charge per month on late invoices.</p>
                                        </div>
                                    </div>
                                    <div class="col-md-4">
                                        <form class="text-end invo-pal">
                                            <input type="image" :src="('/images/other-images/paypal.png')"
                                                alt="PayPal - The safer, easier way to pay online!">
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-12 text-center mt-3">
                            <button class="btn btn btn-primary me-2" type="button" @click="myFunction()">Print</button>
                            <button class="btn btn-secondary" type="button">Cancel</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import invoiceTable from "@/components/ecommerce/invoice/invoiceTable.vue"
export default {
    name: 'invoiceView',
    components: { invoiceTable },
    methods: {
        myFunction() {
            if (process.client) {
                var printContents = document.getElementById('print').innerHTML;
                window.print(printContents);
            }
        }
    }
}
</script>