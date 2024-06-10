<template>
    <l-map :zoom="simple.zoom" :center="simple.center" style="height: 500px">
                            <l-tile-layer :url="simple.url"></l-tile-layer>
                        </l-map>
</template>
<script>
import "leaflet/dist/leaflet.css";
import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
export default {
    components:{
         LMap,
          LTileLayer
    },
    data(){
        return{
            simple:{
          zoom:5,
          center: [49.439557, 234.558105],
          url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
        },
        }
    }
}
</script>