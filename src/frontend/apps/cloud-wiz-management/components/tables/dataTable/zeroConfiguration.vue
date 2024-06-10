<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h3>Zero Configuration</h3><span>DataTables has most features enabled by default, so all you need to do to
                    use it with your own tables is to call the construction
                    function:<code>$().DataTable();</code>.</span><span>Searching, ordering and paging goodness will be
                    immediately added to the table, as shown in this example.</span>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="display" id="basic-1">
                        <EasyDataTable :headers="Headers" rowsPerPage="10" :items="Item" style="width:130%;">
                        </EasyDataTable>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import dataTable from "@/mixin/dataTable"
export default {
    mixins: [dataTable]


}
</script>
