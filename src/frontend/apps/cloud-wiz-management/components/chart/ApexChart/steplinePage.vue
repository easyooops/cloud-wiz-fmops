<template>
  <div class="col-sm-12 col-xl-6 box-col-6">
    <div class="card">
      <div class="card-header">
        <h3>Stepline Chart </h3>
      </div>
      <div class="card-body">
        <div id="stepline">
          <apexchart
            height="350"
            type="line"
            :options="chartOptions"
            :series="series"
          ></apexchart>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#24695c';
export default {
  data() {
    return {
         series: [{
        data: [34, 44, 54, 21, 12, 43, 33, 23, 66, 66, 58]
    }],
    chartOptions:{
         chart: {
        type: 'line',
        height: 350,
        toolbar:{
          show: false
        }
    },
    stroke: {
        curve: 'stepline',
    },
    dataLabels: {
        enabled: false
    },

    title: {
        text: 'Stepline Chart',
        align: 'left'
    },
    markers: {
        hover: {
            sizeOffset: 4
        }
    },
    colors:[primary]
    }

    };
  },
};
</script>