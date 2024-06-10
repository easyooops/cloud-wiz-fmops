<template>
<div class="container-fluid">
    <div class="row">
        <div class="col-sm-12">
            <div class="card">
                <div class="card-header">
                    <h5>Example</h5>
                </div>
                <div class="card-body">

                    <div class="timeliny loaded">

                        <div class="timeliny-wrapper">
                            <draggable :group="{ name: 'universalGroup', pull: 'clone', put: false }">

                            <div class="timeliny-timeline"  id="timeline-2" style="width: 896px; left: 208px;">
                                <div data-year="2010" class="timeliny-timeblock active">
                                    <a href="#" class="timeliny-dot" data-year="2010" data-text="Start" @click.prevent="move"></a>
                                </div>
                                <div class="timeliny-timeblock" data-year="2011" ><a href="#2011" class="timeliny-dot" data-year="2011" data-text="Lorem is simply dummy text of the printing and typesetting industry. the printing and typesetting industry."></a></div>
                                <div data-year="2013" class="timeliny-timeblock"><a href="#2013" class="timeliny-dot" data-year="2013" data-text="Lorem is simply dummy text of the printing and typesetting industry. "></a></div>
                                <div data-year="2014" class="timeliny-timeblock" id="start"><a href="#2014" class="timeliny-dot" data-year="2014" data-text="Lorem is simply dummy text of the printing and typesetting industry."></a></div>
                                <div data-year="2015" class="timeliny-timeblock"><a href="#2015" class="timeliny-dot" data-year="2015" data-text="Lorem is simply dummy text of the printing and typesetting industry."></a></div>
                                <div data-year="2017" class="timeliny-timeblock"><a href="#2017" class="timeliny-dot" data-year="2017" data-text="Lorem is simply dummy text of the printing and typesetting industry."></a></div>
                                <div data-year="2018" class="timeliny-timeblock"><a href="#2018" class="timeliny-dot" data-year="2018" data-text="End."></a></div>
                            </div>
                        </draggable >

                        </div>
                        <draggable :group="{ name: 'universalGroup', pull: 'clone', put: false }">
                         <div class="timeliny-vertical-line" id="stick"></div></draggable>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>
<script>
import { VueDraggableNext } from 'vue-draggable-next'

export default {
    components:{
       draggable: VueDraggableNext,
    },
    methods:{
        move(){
            var store= document.getElementById('start').offsetLeft
            document.getElementById('timeline-2').style.left='250px'

        }
    }
}
</script>
