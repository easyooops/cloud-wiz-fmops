<template>
    <Breadcrumbs main="Widgets" title="Chart" />

    <div class="container-fluid">
      <topChart/>
       <barChart/>
  <smallChart/>
        <div class="row">
         <stockChart/>
         <monthlyChart/>
        </div>
      </div>
</template>
<script>
import topChart from './topChart.vue'
import barChart from './barChart.vue'
import smallChart from './smallChart.vue';
import stockChart from './stockChart.vue';
import monthlyChart from './monthlyChart.vue';

export default {
    components:{
        topChart,
        barChart,smallChart,
        stockChart,monthlyChart
    }
}
</script>