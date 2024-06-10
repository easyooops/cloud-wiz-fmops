<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Spinners" />
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <div class="card">
            <div class="card-header">
              <h5>Loader Style</h5>
            </div>
            <div class="card-body row">
              <loader />
              <loader2page />
              <loader3page />
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import loader from "@/components/uikits/loader/loader.vue"
import loader2page from "@/components/uikits/loader/loader2page.vue"
import loader3page from "@/components/uikits/loader/loader3page.vue"
export default {
  components: {
    loader2page,
    loader3page,
    loader
  }
};
</script>