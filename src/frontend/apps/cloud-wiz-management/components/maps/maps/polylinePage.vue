<template>
  <GoogleMap api-key="YOUR_GOOGLE_MAPS_API_KEY" style="width: 100%; height: 500px" :center="center" :zoom="5">
    <Polyline :options="flightPath" />
  </GoogleMap>
</template>

<script>
import { GoogleMap, Polyline } from 'vue3-google-map'

export default {
  components: { GoogleMap, Polyline },
  setup() {
    const center = { lat: 52, lng: 5 }
    const flightPlanCoordinates = [
      { lat: 53.3477, lng: -6.2597 },
      { lat: 51.5008, lng: -0.1224 },
      { lat: 48.8567, lng: 2.3508 },
      { lat: 52.5166, lng: 13.3833 },
    ]
    const flightPath = {
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: 'black',
      strokeOpacity: 1.0,
      strokeWeight: 2,
    }

    return { center, flightPath }
  },
}
</script>