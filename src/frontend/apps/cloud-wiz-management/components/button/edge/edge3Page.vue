<template>
  <div class="card">
    <div class="card-header">
      <h5>Outline extra small buttons</h5>
      <settingPage/><span>Add <code>.btn-pill</code>,<code>.btn-outline-*</code> and <code>.btn-xs</code> class for extra small button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-xs" type="button" title="btn btn-pill btn-outline-primary btn-xs">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary btn-xs" type="button" title="btn btn-pill btn-outline-secondary btn-xs">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success btn-xs" type="button" title="btn btn-pill btn-outline-success btn-xs">Success Button</button>
      <button class="btn btn-pill btn-outline-info btn-xs" type="button" title="btn btn-pill btn-outline-info btn-xs">Info Button</button>
      <button class="btn btn-pill btn-outline-warning btn-xs" type="button" title="btn btn-pill btn-outline-warning btn-xs">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger btn-xs" type="button" title="btn btn-pill btn-outline-danger btn-xs">Danger Button</button>
      <button class="btn btn-pill btn-outline-light btn-xs txt-dark" type="button" title="btn btn-pill btn-outline-light btn-xs">Light Button</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Disabled outline buttons</h5>
      <settingPage/><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-success disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-info disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-warning disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-danger disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-light disabled txt-dark" type="button">Disabled</button>
      
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Gradien buttons</h5>
     <span>Add <code>.btn-pill</code> and <code>.btn-*-gradien</code>class for gradien button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-primary-gradien" type="button" title="btn btn-pill btn-primary-gradien">Primary Button</button>
      <button class="btn btn-pill btn-secondary-gradien" type="button" title="btn btn-pill btn-secondary-gradien">Secondary Button</button>
      <button class="btn btn-pill btn-success-gradien" type="button" title="btn btn-pill btn-success-gradien">Success Button</button>
      <button class="btn btn-pill btn-info-gradien" type="button" title="btn btn-pill btn-info-gradien">Info Button</button>
      <button class="btn btn-pill btn-warning-gradien" type="button" title="btn btn-pill btn-warning-gradien">Warning Button</button>
      <button class="btn btn-pill btn-danger-gradien" type="button" title="btn btn-pill btn-danger-gradien">Danger Button</button>
      <button class="btn btn-pill btn-light-gradien txt-dark" type="button" title="btn btn-pill btn-light-gradien">Light Button</button>
    </div>
  </div>
</template>
<script>
export default{
  inject:['Tooltip'],

  mounted(){
    new this.Tooltip(document.body,{
      selector: "[data-bs-toggle='tooltip']"
    })
  }
}
</script>