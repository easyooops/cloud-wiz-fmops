<template>
  <div class="card">
    <div class="card-header">
      <h5>Disabled Outline Buttons</h5>
   <settingPage/><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled state</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary disabled" type="button">Disabled</button>
      <button class="btn btn-outline-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-outline-success disabled" type="button">Disabled</button>
      <button class="btn btn-outline-info disabled" type="button">Disabled</button>
      <button class="btn btn-outline-warning disabled" type="button">Disabled</button>
      <button class="btn btn-outline-danger disabled" type="button">Disabled</button>
      <button class="btn btn-outline-light txt-dark disabled" type="button">Disabled</button>
    
    </div>
  </div>
  <div class="card" id="gradiant">
    <div class="card-header">
      <h5>Gradient Buttons</h5>
     <settingPage/><span>Add <code>.btn-*-gradien</code> class for gradien button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-primary-gradien" type="button" title="btn btn-primary-gradien">Primary Button</button>
      <button class="btn btn-secondary-gradien" type="button" title="btn btn-secondary-gradien">Secondary Button</button>
      <button class="btn btn-success-gradien" type="button" title="btn btn-success-gradien">Success Button</button>
      <button class="btn btn-info-gradien" type="button" title="btn btn-info-gradien">Info Button</button>
      <button class="btn btn-warning-gradien" type="button" title="btn btn-warning-gradien">Warning Button</button>
      <button class="btn btn-danger-gradien" type="button" title="btn btn-danger-gradien">Danger Button</button>
      
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