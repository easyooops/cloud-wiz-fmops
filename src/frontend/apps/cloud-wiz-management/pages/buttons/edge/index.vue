<template>
  <Breadcrumbs title="Edge Style" main="Buttons" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12 ">
        <edge />
        <edge2 />
        <edge3 />
      </div>
    </div>
  </div>
</template>
<script>
import edge from "@/components/button/edge/edgePage.vue"
import edge2 from "@/components/button/edge/edge2Page.vue"
import edge3 from "@/components/button/edge/edge3Page.vue"
export default {
  components: {
    edge,
    edge2,
    edge3
  }
}
</script>