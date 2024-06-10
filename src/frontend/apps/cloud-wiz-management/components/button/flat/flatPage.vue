<template>
  <div class="card">
    <div class="card-header">
      <h5>Default buttons</h5>
      <settinPage/><span>Add <code>.btn-square</code> class for flat button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary" type="button" title="btn btn-square btn-primary">Primary Button</button>
      <button class="btn btn-square btn-secondary" type="button" title="btn btn-square btn-secondary">Secondary Button</button>
      <button class="btn btn-square btn-success" type="button" title="btn btn-square btn-success">Success Button</button>
      <button class="btn btn-square btn-info" type="button" title="btn btn-square btn-info">Info Button</button>
      <button class="btn btn-square btn-warning" type="button" title="btn btn-square btn-warning">Warning Button</button>
      <button class="btn btn-square btn-danger" type="button" title="btn btn-square btn-danger">Danger Button</button>
      <button class="btn btn-square btn-light" type="button" title="btn btn-square btn-light">Light Button</button>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Large buttons</h5>
     <settinPage/><span>Add <code>.btn-square</code> and <code>.btn-lg</code> class for large button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary btn-lg" type="button" title="btn btn-square btn-primary btn-lg">Primary Button</button>
      <button class="btn btn-square btn-secondary btn-lg" type="button" title="btn btn-square btn-secondary btn-lg">Secondary Button</button>
      <button class="btn btn-square btn-success btn-lg" type="button" title="btn btn-square btn-success btn-lg">Success Button</button>
      <button class="btn btn-square btn-info btn-lg" type="button" title="btn btn-square btn-info btn-lg">Info Button</button>
      <button class="btn btn-square btn-warning btn-lg" type="button" title="btn btn-square btn-warning btn-lg">Warning Button</button>
      <button class="btn btn-square btn-danger btn-lg" type="button" title="btn btn-square btn-danger btn-lg">Danger Button</button>
      <button class="btn btn-square btn-light btn-lg" type="button" title="btn btn-square btn-light btn-lg">Light Button</button>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Small buttons</h5>
      <settinPage/><span>Add <code>.btn-square</code> and <code>.btn-sm</code> class for small button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary btn-sm" type="button" title="btn btn-square btn-primary btn-sm">Primary Button</button>
      <button class="btn btn-square btn-secondary btn-sm" type="button" title="btn btn-square btn-secondary btn-sm">Secondary Button</button>
      <button class="btn btn-square btn-success btn-sm" type="button" title="btn btn-square btn-success btn-sm">Success Button</button>
      <button class="btn btn-square btn-info btn-sm" type="button" title="btn btn-square btn-info btn-sm">Info Button</button>
      <button class="btn btn-square btn-warning btn-sm" type="button" title="btn btn-square btn-warning btn-sm">Warning Button</button>
      <button class="btn btn-square btn-danger btn-sm" type="button" title="btn btn-square btn-danger btn-sm">Danger Button</button>
      <button class="btn btn-square btn-light btn-sm" type="button" title="btn btn-square btn-light btn-sm">Light Button</button>
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Extra Small buttons</h5>
      <settinPage/><span>Add <code>.btn-square</code> and <code>.btn-xs</code> class for extra small button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary btn-xs" type="button" title="btn btn-square btn-primary btn-xs">Primary Button</button>
      <button class="btn btn-square btn-secondary btn-xs" type="button" title="btn btn-square btn-secondary btn-xs">Secondary Button</button>
      <button class="btn btn-square btn-success btn-xs" type="button" title="btn btn-square btn-success btn-xs">Success Button</button>
      <button class="btn btn-square btn-info btn-xs" type="button" title="btn btn-square btn-info btn-xs">Info Button</button>
      <button class="btn btn-square btn-warning btn-xs" type="button" title="btn btn-square btn-warning btn-xs">Warning Button</button>
      <button class="btn btn-square btn-danger btn-xs" type="button" title="btn btn-square btn-danger btn-xs">Danger Button</button>
      <button class="btn btn-square btn-light btn-xs" type="button" title="btn btn-square btn-light btn-xs">Light Button</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Active Buttons</h5>
      <settinPage/><span>Add <code>.active</code> for active state</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary active" type="button" title="btn btn-square btn-primary active">Active</button>
      <button class="btn btn-square btn-secondary active" type="button" title="btn btn-square btn-secondary active">Active</button>
      <button class="btn btn-square btn-success active" type="button" title="btn btn-square btn-success active">Active</button>
      <button class="btn btn-square btn-info active" type="button" title="btn btn-square btn-info active">Active</button>
      <button class="btn btn-square btn-warning active" type="button" title="btn btn-square btn-warning active">Active</button>
      <button class="btn btn-square btn-danger active" type="button" title="btn btn-square btn-danger active">Active</button>
      <button class="btn btn-square btn-light active txt-dark" type="button" title="btn btn-square btn-light active">Active</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Disabled buttons</h5>
     <settinPage/> <span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-square btn-primary disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-success disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-info disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-warning disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-danger disabled" type="button">Disabled</button>
      <button class="btn btn-square btn-light disabled" type="button">Disabled</button>
     
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