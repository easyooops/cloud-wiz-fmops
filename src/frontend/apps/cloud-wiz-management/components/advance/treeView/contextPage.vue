<template>
    <div class="col-sm-12 col-xl-6">
        <div class="card">
            <div class="card-header">
                <h3>Contextmenu Tree</h3>
            </div>
            <div class="card-body">
                <div id="treeBasic">
                    <Tree :nodes="menu" :use-icon="false" draggable />
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import Tree from "vue3-tree";
import "vue3-tree/dist/style.css"
import treeView from "@/mixin/commen/treeView"
export default {
    components: {
        Tree
    },
    mixins: [treeView],


}
</script>