<template>
  <div class="col-sm-12 col-xl-6 box-col-12">
    <div class="card">
      <div class="card-header">
        <h4>Word Tree</h4>
      </div>
      <div class="card-body  chart-block">
        <div class="word-tree" id="wordtree_basic">

          <GChart :type="type" :data="data" :options="options" :settings="settings" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { GChart } from "vue-google-charts";
export const chartType = 'WordTree';

export const chartData = [
  ['Phrases'],
  ['cats are better than dogs'],
  ['cats eat kibble'],
  ['cats are better than hamsters'],
  ['cats are awesome'],
  ['cats are people too'],
  ['cats eat mice'],
  ['cats meowing'],
  ['cats in the cradle'],
  ['cats eat mice'],
  ['cats in the cradle lyrics'],
  ['cats eat kibble'],
  ['cats for adoption'],
  ['cats are family'],
  ['cats eat mice'],
  ['cats are better than kittens'],
  ['cats are evil'],
  ['cats are weird'],
  ['cats eat mice'],
];

export const chartOptions = {
  wordtree: {
    format: 'implicit',
    word: 'cats',
  },
  width: 707,
  height: 400,
};

export default {
  components: {
    GChart,
  },
  data() {
    return { 
       type: chartType,
      data: chartData,
      options: chartOptions,
      settings: {
        packages: ['wordtree'],
      },
    };
  },
};
</script>