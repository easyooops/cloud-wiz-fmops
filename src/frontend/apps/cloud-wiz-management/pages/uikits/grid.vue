<template>
  <div>
    <Breadcrumbs main="UI Kits" title="grid" />

    <div class="container-fluid grid">
      <div class="row">
        <GridOptions />
        <GridColumn />
        <SettingoneOlumnwidth />
        <Verticalalignment />
        <Horizontalalignment />
        <NestingColumn />
        <Order />
        <Offset />
      </div>
    </div>

  </div>
</template>

<script>
import GridOptions from "@/components/uikits/grid/GridOptions.vue"
import GridColumn from "@/components/uikits/grid/GridColumn.vue";
import SettingoneOlumnwidth from "@/components/uikits/grid/Settingoneolumnwidth.vue";
import Verticalalignment from "@/components/uikits/grid/Verticalalignment.vue";
import Horizontalalignment from "@/components/uikits/grid/Horizontalalignment.vue";
import NestingColumn from "@/components/uikits/grid/NestingColumn.vue";
import Order from "@/components/uikits/grid/Order.vue";
import Offset from "@/components/uikits/grid/Offset.vue";
export default {
  components: {
    GridOptions,
    GridColumn,
    SettingoneOlumnwidth,
    Verticalalignment,
    Horizontalalignment,
    NestingColumn,
    Order,
    Offset
  }

};
</script>