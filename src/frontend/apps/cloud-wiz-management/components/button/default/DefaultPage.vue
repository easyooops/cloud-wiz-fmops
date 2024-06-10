<template>
  <div class="card" id="default">
    <div class="card-header">
      <h5>Default Buttons</h5>
      <settingPage />
      <span>Bootstrap state buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary" type="button" data-bs-toggle="tooltip" title="btn btn-primary">Primary
        Button</button>
      <button class="btn btn-secondary" type="button" data-bs-toggle="tooltip" title="btn btn-secondary">Secondary
        Button</button>
      <button class="btn btn-success" type="button" data-bs-toggle="tooltip" title="btn btn-success">Success
        Button</button>
      <button class="btn btn-info" type="button" data-bs-toggle="tooltip" title="btn btn-info">Info Button</button>
      <button class="btn btn-warning" type="button" data-bs-toggle="tooltip" title="btn btn-warning">Warning
        Button</button>
      <button class="btn btn-danger" type="button" data-bs-toggle="tooltip" title="btn btn-danger">Danger Button</button>
      <button class="btn btn-light" type="button" data-bs-toggle="tooltip" title="btn btn-light">Light Button</button>
    </div>
  </div>
  <div class="card" id="large-btn">
    <div class="card-header">
      <h5>Large Buttons</h5>
      <settingPage />
      <span>Add <code>.btn-lg</code> class for large size buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-primary btn-lg">Primary
        Button</button>
      <button class="btn btn-secondary btn-lg" type="button" data-bs-toggle="tooltip"
        title="btn btn-secondary btn-lg">Secondary Button</button>
      <button class="btn btn-success btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-success btn-lg">Success
        Button</button>
      <button class="btn btn-info btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-info btn-lg">Info
        Button</button>
      <button class="btn btn-warning btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-warning btn-lg">Warning
        Button</button>
      <button class="btn btn-danger btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-danger btn-lg">Danger
        Button</button>
      <button class="btn btn-light btn-lg" type="button" data-bs-toggle="tooltip" title="btn btn-light btn-lg">Light
        Button</button>
    </div>
  </div>
  <div class="card" id="small-btn">
    <div class="card-header">
      <h5>Small Buttons</h5>
      <settingPage /><span>Add <code>.btn-sm</code> class for small size buttons</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary btn-sm" type="button" title="btn btn-primary btn-sm">Primary Button</button>
      <button class="btn btn-secondary btn-sm" type="button" title="btn btn-secondary btn-sm">Secondary Button</button>
      <button class="btn btn-success btn-sm" type="button" title="btn btn-success btn-sm">Success Button</button>
      <button class="btn btn-info btn-sm" type="button" title="btn btn-info btn-sm">Info Button</button>
      <button class="btn btn-warning btn-sm" type="button" title="btn btn-warning btn-sm">Warning Button</button>
      <button class="btn btn-danger btn-sm" type="button" title="btn btn-danger btn-sm">Danger Button</button>
      <button class="btn btn-light btn-sm" type="button" title="btn btn-light btn-sm">Light Button</button>
    </div>
  </div>
  <outlineButtons />
</template>
<script>
import outlineButtons from "./outlineButtons.vue"
export default {
  components: { outlineButtons },
  inject: ['Tooltip'],
  mounted() {
    new this.Tooltip(document.body, {
      selector: "[data-bs-toggle='tooltip']"
    })
  }
}
</script>