<template>
    <div>
        <Breadcrumbs main="Widgets" title="General" />

        <div class="container-fluid">
            <div class="row">
                <coinGeneral />
                <averageGeneral />
                <fourCard />
                <courseGeneral />
                <visitorGeneral />
                <socialGeneral />
                <newGeneral />
                <dateGeneral />
            </div>
        </div>

    </div>
</template>

<script>
import coinGeneral from './coinGeneral.vue'
import averageGeneral from './averageGeneral.vue'
import fourCard from './fourCard.vue'
import courseGeneral from './courseGeneral.vue'
import visitorGeneral from './visitorGeneral.vue'
import socialGeneral from './socialGeneral.vue'
import newGeneral from './newGeneral.vue'
import dateGeneral from './dateGeneral.vue'
export default {
    components: {
        coinGeneral,
        averageGeneral,
        fourCard,
        courseGeneral,
        visitorGeneral,
        socialGeneral,
        newGeneral,
        dateGeneral
    }
}
</script>
