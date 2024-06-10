<template>
<div>
    <GoogleMap :center="center" :zoom="4" style="width: 100%; height: 500px">
        <Marker v-for="(location, index) in positions.lists" :key="index" :options="{ position: { lat: location.lat, lng: location.lng } }" @click="markerClicked" />
    </GoogleMap>

</div>
</template>

<script>
import {
    reactive
} from "vue";
import {
    GoogleMap,
    Marker
} from "vue3-google-map";
export default {
    components: {
        GoogleMap,
        Marker
    },

    setup() {
        const center = {
            lat: 50,
            lng: 5
        };
        const positions = reactive({
            lists: [{
                    lat: 48.8567,
                    lng: 2.3508
                },
                {
                    lat: 41.9,
                    lng: 12.5
                },
                {
                    lat: 52.5166,
                    lng: 13.3833
                },
                {
                    lat: 40.4,
                    lng: -3.6833
                },
                {
                    lat: 51.5008,
                    lng: -0.1224
                },
            ],
        })
        return {
            center,
            positions
        };
    },

    methods: {}
};
</script>
