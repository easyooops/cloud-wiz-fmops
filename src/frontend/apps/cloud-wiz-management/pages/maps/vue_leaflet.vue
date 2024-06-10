<template>
    <Breadcrumbs main="Maps" title="Vue Leaflet" />
    <div class="container-fluid">
        <div class="row">
            <div class="col-xl-6 text-start">
                <div class="card">
                    <div class="card-header">
                        <h5>Simple Map</h5>
                    </div>
                    <div class="card-body">
                        <simplemap />
                    </div>
                </div>
            </div>
            <div class="col-xl-6 text-start">
                <div class="card">
                    <div class="card-header">
                        <h5>Multi-language support</h5><span>Display a map with labels in a foreign language</span>
                    </div>
                    <div class="card-body">
                        <multilanguage />
                    </div>
                </div>
            </div>
            <div class="col-xl-12 text-start">
                <div class="card">
                    <div class="card-header">
                        <h5>Multi-language support</h5><span>Display a map with labels in a foreign language</span>
                    </div>
                    <div class="card-body">
                        <multilanguage2 />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import simplemap from "@/components/maps/maps/simpleMap.vue"
import multilanguage from "@/components/maps/maps/multiLanguage.vue"
import multilanguage2 from "@/components/maps/maps/multiLanguage2.vue"
export default {
    components: {
        simplemap,
        multilanguage,
        multilanguage2
    }
}
</script>