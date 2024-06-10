<template>
  <Breadcrumbs title="Input Groups" main="Forms Control" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <input1 />
        <input2 />
      </div>
    </div>
  </div>
</template>
<script>
import input1 from "@/components/forms/InputGroup/input1Page.vue"
import input2 from "@/components/forms/InputGroup/input2Page.vue"
export default {
  components: {
    input1,
    input2
  }
}
</script>