<template>
    <Breadcrumbs title="Kanban Board" />
    <div class="container-fluid jkanban-container">
        <div class="row">
            <DefaultDemoCard />
            <CustomBoardCard />
            <api />
            <div class="col-12">
                <div class="card kanban-note p-20">jKanban is Pure agnostic Javascript plugin for Kanban boards for more options please refer <a href="http://www.riccardotartaglia.it/jkanban/" target="_blank">jkanban Official site </a>And <a href="https://github.com/riktar/jkanban" target="_blank">githup link</a></div>
            </div>
        </div>
    </div>
    </template>
    
    <script>
    import api from './api.vue'
    import DefaultDemoCard from './defaultDemoCard.vue';
    import CustomBoardCard from './customBoardCard.vue';
    import {
        VueDraggableNext
    } from 'vue-draggable-next'
    
    export default {
        name: "App",
        components: {
            draggable: VueDraggableNext,
            api,
            DefaultDemoCard,
            CustomBoardCard
        }
    }
    </script>
    