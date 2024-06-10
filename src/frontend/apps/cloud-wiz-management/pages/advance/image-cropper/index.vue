<template>
  <Breadcrumbs title="Image Copper" main="Bonus UI" />
  <div class="container-fluid">
    <div class="img-cropper">
      <div class="row">
        <div class="col-sm-12 ">
          <imageCropper />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import imageCropper from "@/components/advance/image-cropper/imageCropper.vue"
export default {
  components: {
    imageCropper,
  }
}
</script>