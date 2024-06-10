<template>
    <Breadcrumbs main="Charts" title="ApexChart" />
    <div class="container-fluid ">
        <div class="row">
            <basicArea />
            <areaSpaline />
            <barChart />
            <columnChart />
            <bubbleChart />
            <stepline />
            <columnChart2 />
            <pieChart />
            <donutChart />
            <mixedChart />
            <candlestick />
            <radarChart />
            <radialBar />
        </div>
    </div>
</template>

<script>
import basicArea from "@/components/chart/ApexChart/basicArea.vue"
import areaSpaline from "@/components/chart/ApexChart/areaSpaline.vue"
import barChart from "@/components/chart/ApexChart/barChart.vue"
import columnChart from "@/components/chart/ApexChart/columnChart.vue"
import bubbleChart from "@/components/chart/ApexChart/bubbleChart.vue"
import stepline from "@/components/chart/ApexChart/steplinePage.vue"
import columnChart2 from "@/components/chart/ApexChart/columnChart2.vue"
import pieChart from "@/components/chart/ApexChart/pieChart.vue"
import donutChart from "@/components/chart/ApexChart/donutChart.vue"
import mixedChart from "@/components/chart/ApexChart/mixedChart.vue"
import candlestick from "@/components/chart/ApexChart/candlestickChart.vue"
import radarChart from "@/components/chart/ApexChart/radarChart.vue"
import radialBar from "@/components/chart/ApexChart/radialBar.vue"
export default {
    components: {
        basicArea,
        areaSpaline,
        barChart,
        columnChart,
        bubbleChart,
        stepline,
        columnChart2,
        pieChart,
        donutChart,
        mixedChart,
        candlestick,
        radarChart,
        radialBar
    }
};
</script>
