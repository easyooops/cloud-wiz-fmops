<template>
  <div class="card" id="custom-state-button">
    <div class="card-header">
      <h5>Custom State Buttons</h5>
      <settingPage/><span>The <code>.btn</code> class used with <code>&lt;button&gt;</code>, <code>&lt;a&gt;</code> and <code>&lt;input&gt;</code> elements.</span>
    </div>
    <div class="card-body btn-showcase"><a class="btn btn-primary" href="javascript:void(0)" data-toggle="tooltip" title="btn btn-primary" role="button">Link</a>
      <input class="btn btn-secondary" type="button" value="Input" data-toggle="tooltip" title="btn btn-secondary">
      <input class="btn btn-success" type="submit" value="Submit" data-toggle="tooltip" title="btn btn-success">
      <button class="btn btn-info" type="submit" data-toggle="tooltip" title="btn btn-info">Button</button>
     
    </div>
  </div>
  <div class="card" id="outline-button">
    <div class="card-header">
      <h5>Outline Buttons</h5>
      <settingPage/><span>Add <code>.btn-outline-*</code> class for border button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary" type="button" title="btn btn-outline-primary">Primary Button</button>
      <button class="btn btn-outline-secondary" type="button" title="btn btn-outline-secondary">Secondary Button</button>
      <button class="btn btn-outline-success" type="button" title="btn btn-outline-success">Success Button</button>
      <button class="btn btn-outline-info" type="button" title="btn btn-outline-info">Info Button</button>
      <button class="btn btn-outline-warning" type="button" title="btn btn-outline-warning">Warning Button</button>
      <button class="btn btn-outline-danger" type="button" title="btn btn-outline-danger">Danger Button</button>
      <button class="btn btn-outline-light txt-dark" type="button" title="btn btn-outline-light">Light Button</button>
      
    </div>
  </div>
  <div class="card" id="outline-bold-button">
    <div class="card-header">
      <h5>Bold Border Outline Buttons</h5>
      <settingPage/> <span>Add <code>.btn-outline-*-2x</code> class for bold outline</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary-2x" type="button" title="btn btn-outline-primary-2x">Primary Button</button>
      <button class="btn btn-outline-secondary-2x" type="button" title="btn btn-outline-secondary-2x">Secondary Button</button>
      <button class="btn btn-outline-success-2x" type="button" title="btn btn-outline-success-2x">Success Button</button>
      <button class="btn btn-outline-info-2x" type="button" title="btn btn-outline-info-2x">Info Button</button>
      <button class="btn btn-outline-warning-2x" type="button" title="btn btn-outline-warning-2x">Warning Button</button>
      <button class="btn btn-outline-danger-2x" type="button" title="btn btn-outline-danger-2x">Danger Button</button>
      <button class="btn btn-outline-light-2x txt-dark" type="button" title="btn btn-outline-light-2x">Light Button</button>
    
    </div>
  </div>
  <div class="card" id="outline-large-button">
    <div class="card-header">
      <h5>Outline Large Buttons</h5>
      <settingPage/> <span>Add <code>.btn-outline-*</code> class for outline and <code>.btn-lg</code> class for large button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary btn-lg" type="button" title="btn btn-outline-primary btn-lg">Primary Button</button>
      <button class="btn btn-outline-secondary btn-lg" type="button" title="btn btn-outline-secondary btn-lg">Secondary Button</button>
      <button class="btn btn-outline-success btn-lg" type="button" title="btn btn-outline-success btn-lg">Success Button</button>
      <button class="btn btn-outline-info btn-lg" type="button" title="btn btn-outline-info btn-lg">Info Button</button>
      <button class="btn btn-outline-warning btn-lg" type="button" title="btn btn-outline-warning btn-lg">Warning Button</button>
      <button class="btn btn-outline-danger btn-lg" type="button" title="btn btn-outline-danger btn-lg">Danger Button</button>
      <button class="btn btn-outline-light txt-dark btn-lg" type="button" title="btn btn-outline-light btn-lg">Light Button</button>
      
    </div>
  </div>
  <div class="card" id="outline-small-button">
    <div class="card-header">
      <h5>Outline Small Buttons</h5>
      <settingPage/> <span>Add <code>.btn-outline-*</code> class for outline and <code>.btn-sm</code> class for small button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary btn-sm" type="button" title="btn btn-outline-primary btn-sm">Primary Button</button>
      <button class="btn btn-outline-secondary btn-sm" type="button" title="btn btn-outline-secondary btn-sm">Secondary Button</button>
      <button class="btn btn-outline-success btn-sm" type="button" title="btn btn-outline-success btn-sm">Success Button</button>
      <button class="btn btn-outline-info btn-sm" type="button" title="btn btn-outline-info btn-sm">Info Button</button>
      <button class="btn btn-outline-warning btn-sm" type="button" title="btn btn-outline-warning btn-sm">Warning Button</button>
      <button class="btn btn-outline-danger btn-sm" type="button" title="btn btn-outline-danger btn-sm">Danger Button</button>
      <button class="btn btn-outline-light btn-sm txt-dark" type="button" title="btn btn-outline-light btn-sm">Light Button</button>
     
    </div>
  </div>
  <div class="card" id="ex-outline-small-button">
    <div class="card-header">
      <h5>Outline Extra Small Buttons</h5>
      <settingPage/> <span>Add <code>.btn-outline-*</code> class for outline and <code>.btn-xs</code> class for extra small button</span>
    </div>
    <div class="card-body btn-showcase">
      <button class="btn btn-outline-primary btn-xs" type="button" title="btn btn-outline-primary btn-xs">Primary Button</button>
      <button class="btn btn-outline-secondary btn-xs" type="button" title="btn btn-outline-secondary btn-xs">Secondary Button</button>
      <button class="btn btn-outline-success btn-xs" type="button" title="btn btn-outline-success btn-xs">Success Button</button>
      <button class="btn btn-outline-info btn-xs" type="button" title="btn btn-outline-info btn-xs">Info Button</button>
      <button class="btn btn-outline-warning btn-xs" type="button" title="btn btn-outline-warning btn-xs">Warning Button</button>
      <button class="btn btn-outline-danger btn-xs" type="button" title="btn btn-outline-danger btn-xs">Danger Button</button>
      <button class="btn btn-outline-light btn-xs txt-dark" type="button" title="btn btn-outline-light btn-xs">Light Button</button>
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