<template>
    <Breadcrumbs main="app" title="Support Ticket" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h5>Support Ticket List</h5><span>List of ticket opend by customers</span>
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <supportTicket />
                        </div>
                        <div class="table-responsive">
                            <supportTable />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import supportTicket from "@/components/support/supportTicket.vue"
import supportTable from "@/components/support/supportTable.vue"
export default {
    components: {
        supportTicket, supportTable
    },


}
</script>