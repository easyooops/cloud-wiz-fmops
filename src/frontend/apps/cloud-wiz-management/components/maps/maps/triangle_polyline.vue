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
      { lat: 46.2276, lng: 2.2137 },
      { lat: 51.81925, lng: 12.35031 },
      { lat: 48.2082, lng: 16.54958 },
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