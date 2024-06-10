<template>
    <Breadcrumbs main="Project" title="Projects List" />

    <div class="container-fluid">
        <div class="row project-cards">
            <topMenu />
        </div>
    </div>
</template>

<script>
import topMenu from '../projectlist/topMenu.vue'
export default {
    name: 'indexList',
    components: {
        topMenu
    },

}

</script>
