<template>
  <Breadcrumbs title="Range Slider" main="Bonus UI" />

  <div class="container-fluid ">
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5>Ion Range Slider</h5>
            </div>
            <div class="card-body">
                 <form class="theme-form form-label-align-right range-slider">
                  <div class="form-group row">
                  <label class="col-md-2 col-form-label sm-left-text" for="u-range-01">Default</label>
                  <div class="col-md-10">
                   <VueSlider v-model="one.value" :data="one.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  
                  </div>
                </div>
                <div class="form-group  row">
                  <label class="col-md-2 control-label sm-left-text" for="u-range-02">Min-Max Value</label>
                  <div class="col-md-10">
                    <VueSlider v-model="two.value" :data="two.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                 <div class="form-group  row">
                  <label class="col-md-2 control-label sm-left-text" for="u-range-03">Prefix</label>
                  <div class="col-md-10">
                    <VueSlider v-model="three.value" :data="three.data1" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                 <div class="form-group  row">
                  <label class="col-md-2 control-label sm-left-text" for="u-range-04">Nagative value</label>
                  <div class="col-md-10">
                    <VueSlider v-model="four.value" :data="four.data2" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                  <div class="form-group  row">
                  <label class="col-md-2 control-label sm-left-text" for="u-range-05">Steps</label>
                  <div class="col-md-10">
                   <VueSlider v-model="seven.value" :data="seven.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                 <div class="form-group  row">
                  <label class="col-md-2  control-label sm-left-text" for="u-range-06">Custom Values</label>
                  <div class="col-md-10">
                   <VueSlider v-model="five.value" :data="five.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                 <div class="form-group  row">
                  <label class="col-md-2 control-label sm-left-text" for="u-range-07">Prettify Numbers</label>
                  <div class="col-md-10">
                    <VueSlider v-model="six.value" :data="six.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                  </div>
                </div>
                 </form>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>
<script>

export default {

data(){
  return{
      one:{
    value:30,
    data:[10,20,30,40,50,60,70,80,90, 100]
  },
  two:{
    value:550,
    data:[100,1000]
  },
   three:{
    value:[200,800],
    data1: [10,  100, 200,250, 500,  750, 800, 1000 ],
   
  },
  four:{
    value:[-500,500],
    data2: [-1000,-720,-500,-250,0,250,500,720,1000 ],
  },
  five:{
      value:'April',
      data: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  },
   six:{
      value:2000,
      data: [1000,2000,3250,5500,7750,10000]
  },  
  seven:{
      value:2000,
      data: [1000,2000,3250,5500,7750,10000]
  }
  }
}
}
</script>