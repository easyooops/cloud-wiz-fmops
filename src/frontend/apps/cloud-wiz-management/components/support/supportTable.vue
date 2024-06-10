<template>
    <table class="table display dataTable" id="basic-6">
        <div id="basic-6_filter" class="dataTables_filter"><label>Search:<input type="search" v-model="searchValue" class=""
                    placeholder="" aria-controls="basic-6" data-bs-original-title="" title=""></label></div>
        <EasyDataTable :headers="Headers" rowsPerPage="10" :items="Item" :search-field="searchField"
            :search-value="searchValue">

            <template #item-name="{ name, avator }">
                <div class="media"><img class="rounded-circle img-30 me-3" :src="getImageUrl(avator)"
                        alt="Generic placeholder image">
                    <div class="media-body align-self-center">
                        <div> {{ name }}</div>
                    </div>
                </div>
            </template>
            <template #item-Skill="{ classe, widthe }">
                <div class="progress-showcase">
                    <div class="progress sm-progress-bar">
                        <div class="progress-bar" :class="classe" role="progressbar" :style="{ width: widthe }"
                            aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </div>
            </template>
        </EasyDataTable>
    </table>
</template>
<script>
import supportTable from "@/mixin/supportTable"
import imageMixin from "@/mixin/commen/imageMixin"
export default {

    mixins: [supportTable, imageMixin]

}
</script>