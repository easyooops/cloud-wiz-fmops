<template>
  <div class="card">
    <div class="card-header">
      <h5>outline small buttons</h5>
      <settingPage/><span><code>.btn-pill</code>,<code>.btn-air-*</code>,<code>.btn-outline-*</code> and <code>.btn-sm</code> class for small button with outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-air-primary btn-sm" type="button" title="btn btn-pill btn-outline-primary btn-air-primary btn-sm">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary btn-air-secondary btn-sm" type="button" title="btn btn-pill btn-outline-secondary btn-air-secondary btn-sm">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success btn-air-success btn-sm" type="button" title="btn btn-pill btn-outline-success btn-air-success btn-sm">Success Button</button>
      <button class="btn btn-pill btn-outline-info btn-air-info btn-sm" type="button" title="btn btn-pill btn-outline-info btn-air-info btn-sm">Info Button</button>
      <button class="btn btn-pill btn-outline-warning btn-air-warning btn-sm" type="button" title="btn btn-pill btn-outline-warning btn-air-warning btn-sm">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger btn-air-danger btn-sm" type="button" title="btn btn-pill btn-outline-danger btn-air-danger btn-sm">Danger Button</button>
      <button class="btn btn-pill btn-outline-light btn-air-light btn-sm txt-dark" type="button" title="btn btn-pill btn-outline-light btn-air-light btn-sm">Light Button</button>
      
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>outline extra small buttons</h5>
      <settingPage/><span><code>.btn-pill</code>,<code>.btn-air-*</code>,<code>.btn-outline-*</code> and <code>.btn-xs</code> class for extra small button with outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-air-primary btn-xs" type="button" title="btn btn-pill btn-outline-primary btn-air-primary btn-xs">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary btn-air-secondary btn-xs" type="button" title="btn btn-pill btn-outline-secondary btn-air-secondary btn-xs">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success btn-air-success btn-xs" type="button" title="btn btn-pill btn-outline-success btn-air-success btn-xs">Success Button</button>
      <button class="btn btn-pill btn-outline-info btn-air-info btn-xs" type="button" title="btn btn-pill btn-outline-info btn-air-info btn-xs">Info Button</button>
      <button class="btn btn-pill btn-outline-warning btn-air-warning btn-xs" type="button" title="btn btn-pill btn-outline-warning btn-air-warning btn-xs">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger btn-air-danger btn-xs" type="button" title="btn btn-pill btn-outline-danger btn-air-danger btn-xs">Danger Button</button>
      <button class="btn btn-pill btn-outline-light btn-air-light btn-xs txt-dark" type="button" title="btn btn-pill btn-outline-light btn-air-light btn-xs">Light Button</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Disabled outline buttons</h5>
      <settingPage/><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-air-primary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-secondary btn-air-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-success btn-air-success disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-info btn-air-info disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-warning btn-air-warning disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-danger btn-air-danger disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-outline-light btn-air-light disabled txt-dark" type="button">Disabled</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Gradien buttons</h5>
      <settingPage/><span><code>.btn-pill</code>,<code>.btn-air-*</code>,<code>.btn-*</code> and <code>.btn-*-gradien</code> class for gradien button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-air-primary btn-primary-gradien" type="button" title="btn btn-pill btn-air-primary btn-primary-gradien">Primary Button</button>
      <button class="btn btn-pill btn-air-secondary btn-secondary-gradien" type="button" title="btn btn-pill btn-air-secondary btn-secondary-gradien">Secondary Button</button>
      <button class="btn btn-pill btn-air-success btn-success-gradien" type="button" title="btn btn-pill btn-air-success btn-success-gradien">Success Button</button>
      <button class="btn btn-pill btn-air-info btn-info-gradien" type="button" title="btn btn-pill btn-air-info btn-info-gradien">Info Button</button>
      <button class="btn btn-pill btn-air-warning btn-warning-gradien" type="button" title="btn btn-pill btn-air-warning btn-warning-gradien">Warning Button</button>
      <button class="btn btn-pill btn-air-danger btn-danger-gradien" type="button" title="btn btn-pill btn-air-danger btn-danger-gradien">Danger Button</button>
      <button class="btn btn-pill btn-air-light btn-light-gradien txt-dark" type="button" title="btn btn-pill btn-air-light btn-light-gradien">Light Button</button>
   
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