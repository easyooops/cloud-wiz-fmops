<template>
    <Breadcrumbs title="Styling table" main="Bootstrap Table" />
    <div class="container-fluid">
        <div class="row">
            <tableRow1 />
            <tableRow2 />
            <tableRow3 />
            <tableCheckbox />
            <tableRadio />
            <tableSelect />
            <tableInput />
            <tableBadge />
            <tableTooltip />
            <tableSwitch />

        </div>
    </div>
</template>
<script>
import tableRow1 from "@/components/tables/stylingtable/tableRow1.vue"
import tableRow2 from "@/components/tables/stylingtable/tableRow2.vue"
import tableRow3 from "@/components/tables/stylingtable/tableRow3.vue"
import tableCheckbox from "@/components/tables/stylingtable/tableCheckbox.vue"
import tableRadio from "@/components/tables/stylingtable/tableRadio.vue"
import tableSelect from "@/components/tables/stylingtable/tableSelect.vue"
import tableInput from "@/components/tables/stylingtable/tableInput.vue"
import tableBadge from "@/components/tables/stylingtable/tableBadge.vue"
import tableTooltip from "@/components/tables/stylingtable/tableTooltip.vue"
import tableSwitch from "@/components/tables/stylingtable/tableSwitch.vue"


export default {
    components: {
        tableRow1,
        tableRow2,
        tableRow3,
        tableCheckbox,
        tableRadio,
        tableSelect,
        tableInput,
        tableBadge,
        tableTooltip,
        tableSwitch,
    }
}
</script>