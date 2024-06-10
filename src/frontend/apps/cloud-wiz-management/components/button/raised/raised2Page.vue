<template>
  <div class="card">
    <div class="card-header">
      <h5>Disabled buttons</h5>
      <settingPage/><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-primary btn-air-primary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-secondary btn-air-secondary disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-success btn-air-success disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-info btn-air-info disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-warning btn-air-warning disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-danger btn-air-danger disabled" type="button">Disabled</button>
      <button class="btn btn-pill btn-light btn-air-light disabled" type="button">Disabled</button>
    
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>Custom state buttons</h5>
      <settingPage/><span>The <code>.btn</code> class used with <code>&lt;button&gt;</code>, <code>&lt;a&gt;</code> and <code>&lt;input&gt;</code> elements.</span>
    </div>
    <div class="card-body btn-showcase"><a class="btn btn-pill btn-primary btn-air-primary" href="javascript:void(0)" data-toggle="tooltip" title="btn btn-primary" role="button">Link</a>
      <input class="btn btn-pill btn-secondary btn-air-secondary btn-air-secondary" type="button" value="Input" data-toggle="tooltip" title="btn btn-secondary">
      <input class="btn btn-pill btn-success btn-air-success btn-air-success" type="submit" value="Submit" data-toggle="tooltip" title="btn btn-success">
      <button class="btn btn-pill btn-info btn-air-info btn-air-info" type="submit" title="btn btn-info">Button</button>
    
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>outline buttons</h5>
      <settingPage/><span>Add <code>.btn-pill</code>,<code>.btn-air-*</code> and <code>.btn-outline-*</code> class for button with outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-air-primary" type="button" title="btn btn-pill btn-outline-primary btn-air-primary">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary btn-air-secondary" type="button" title="btn btn-pill btn-outline-secondary btn-air-secondary">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success btn-air-success" type="button" title="btn btn-pill btn-outline-success btn-air-success">Success Button</button>
      <button class="btn btn-pill btn-outline-info btn-air-info" type="button" title="btn btn-pill btn-outline-info btn-air-info">Info Button</button>
      <button class="btn btn-pill btn-outline-warning btn-air-warning" type="button" title="btn btn-pill btn-outline-warning btn-air-warning">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger btn-air-danger" type="button" title="btn btn-pill btn-outline-danger btn-air-danger">Danger Button</button>
      <button class="btn btn-pill btn-outline-light btn-air-light txt-dark" type="button" title="btn btn-pill btn-outline-light btn-air-light">Light Button</button>
    
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>bold Border outline buttons</h5>
      <settingPage/><span>Add <code>.btn-pill</code>,<code>.btn-air-*</code> and <code>.btn-outline-*-2x</code> class for button with bold outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary-2x btn-air-primary" type="button" title="btn btn-pill btn-outline-primary-2x btn-air-primary">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary-2x btn-air-secondary" type="button" title="btn btn-pill btn-outline-secondary-2x btn-air-secondary">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success-2x btn-air-success" type="button" title="btn btn-pill btn-outline-success-2x btn-air-success">Success Button</button>
      <button class="btn btn-pill btn-outline-info-2x btn-air-info" type="button" title="btn btn-pill btn-outline-info-2x btn-air-info">Info Button</button>
      <button class="btn btn-pill btn-outline-warning-2x btn-air-warning" type="button" title="btn btn-pill btn-outline-warning-2x btn-air-warning">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger-2x btn-air-danger" type="button" title="btn btn-pill btn-outline-danger-2x btn-air-danger">Danger Button</button>
      <button class="btn btn-pill btn-outline-light-2x btn-air-light txt-dark" type="button" title="btn btn-pill btn-outline-light-2x btn-air-light">Light Button</button>
     
    </div>
  </div>
  <div class="card">
    <div class="card-header">
      <h5>outline Large buttons</h5>
     <settingPage/><span><code>.btn-pill</code>,<code>.btn-air-*</code>,<code>.btn-outline-*</code> and <code>.btn-lg</code> class for large button with outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-pill btn-outline-primary btn-air-primary btn-lg" type="button" title="btn btn-pill btn-outline-primary btn-air-primary btn-lg">Primary Button</button>
      <button class="btn btn-pill btn-outline-secondary btn-air-secondary btn-lg" type="button" title="btn btn-pill btn-outline-secondary btn-air-secondary btn-lg">Secondary Button</button>
      <button class="btn btn-pill btn-outline-success btn-air-success btn-lg" type="button" title="btn btn-pill btn-outline-success btn-air-success btn-lg">Success Button</button>
      <button class="btn btn-pill btn-outline-info btn-air-info btn-lg" type="button" title="btn btn-pill btn-outline-info btn-air-info btn-lg">Info Button</button>
      <button class="btn btn-pill btn-outline-warning btn-air-warning btn-lg" type="button" title="btn btn-pill btn-outline-warning btn-air-warning btn-lg">Warning Button</button>
      <button class="btn btn-pill btn-outline-danger btn-air-danger btn-lg" type="button" title="btn btn-pill btn-outline-danger btn-air-danger btn-lg">Danger Button</button>
      <button class="btn btn-pill btn-outline-light btn-air-light btn-lg txt-dark" type="button" title="btn btn-pill btn-outline-light btn-air-light btn-lg">Light Button</button>
     
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