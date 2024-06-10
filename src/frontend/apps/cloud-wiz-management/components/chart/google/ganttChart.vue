<template>
  <div class="col-sm-12 box-col-12">
    <div class="card">
      <div class="card-header">
        <h5>Gantt Chart</h5>
      </div>
      <div class="card-body chart-block">
        <div class="chart-overflow" id="gantt_chart">

          <GChart :type="type" :data="data" :options="options" :settings="settings" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
var primary = localStorage.getItem('primary_color') || '#7366FF';
var secondary = localStorage.getItem('secondary_color') || '#FF3364';
import { GChart } from "vue-google-charts";
function daysToMilliseconds(days) {
  return days * 24 * 60 * 60 * 1000;
}
const columns = [
  { type: 'string', label: 'Task ID' },
  { type: 'string', label: 'Task Name' },
  { type: 'date', label: 'Start Date' },
  { type: 'date', label: 'End Date' },
  { type: 'number', label: 'Duration' },
  { type: 'number', label: 'Percent Complete' },
  { type: 'string', label: 'Dependencies' },
];
const rows = [
  ['Research', 'Find sources', new Date(2015, 0, 1), new Date(2015, 0, 5), null, 100, null,],
  ['Write', 'Write paper', null, new Date(2015, 0, 9), daysToMilliseconds(3), 25, 'Research,Outline',],
  ['Cite', 'Create bibliography', null, new Date(2015, 0, 7), daysToMilliseconds(1), 20, 'Research'],
  ['Complete', 'Hand in paper', null, new Date(2015, 0, 10), daysToMilliseconds(1), 0, 'Cite,Write',],
  ['Outline', 'Outline paper', null, new Date(2015, 0, 6), daysToMilliseconds(1), 100, 'Research',],
];

export const chartType = 'Gantt';

export const chartData = [columns, ...rows];

export const chartOptions = {
  width: 1499,
  height: 275,
  gantt: {
    criticalPathEnabled: false,
    arrow: {
      angle: 100,
      width: 5,
      color: '#51bb25',
      radius: 0
    },
    palette: [
      {
        "color": primary,
        "dark": secondary,
        "light": "#54BA4A"
      }
    ]
  }
};
export default {
  components: {
    GChart
  },
  data() {
    return {
      type: chartType,
      data: chartData,
      options: chartOptions,
      settings: {
        packages: ['gantt'],
      },
    }
  }
}
</script>