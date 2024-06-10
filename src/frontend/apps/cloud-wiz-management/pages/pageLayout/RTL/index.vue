<template>
  <breadCrumbs title="RTL" main="Page Layout" title1="RTL" />

  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card alert alert-primary bg-primary" role="alert">
          <h3 class="alert-heading">Tip!</h3>
          <p>Add the dir="rtl" to the html tag to get this layout.</p>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h3>How to use it?</h3>
            <settingPage />
          </div>
          <div class="card-body">
            <h5>Step 1</h5>
            <p>On this layout, First of all you have to add the class rtl attribute in body tag</p>
            <h5>Step 2</h5>
            <p>Contents are change right to left from left to right respectively</p>
            <h5>Step 3</h5>
            <p>when you want to change spacing left to right at that right left spacing you have to unset css and apply
              right spacing in css</p>
            <h5>Step 4</h5>
            <p>Sometimes js are not change directly with text-align css,so that time you have to copy js and change the
              class as rtl="true".</p>

          </div>
          <div class="card-footer">
            <h4 class="mb-0">Card Footer</h4>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { useLayoutStore } from '~~/store/layout'
export default {
  name: 'indexRTL',
  mounted() {

    useLayoutStore().setLayoutType({ class: 'rtl', rtl: true })
  },
  unmounted() {

    useLayoutStore().setLayoutType({ class: '' })
  }
}

</script>