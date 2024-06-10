<template>
     <div class="card">
                  <div class="card-header">
                    <h5>Disabled outline buttons</h5>
                    <span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled button</span>
                  </div>
                  <div class="card-body btn-showcase">
                    <button class="btn btn-square btn-outline-primary disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-secondary disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-success disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-info disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-warning disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-danger disabled" type="button">Disabled</button>
                    <button class="btn btn-square btn-outline-light disabled txt-dark" type="button">Disabled</button>
                    
                  </div>
                </div>
                <div class="card">
                  <div class="card-header">
                    <h5>Gradien buttons</h5>
                   <span>Add <code>.btn-square</code> and <code>.btn-*-gradien</code> class for gradien button</span>
                  </div>
                  <div class="card-body btn-showcase">
                    <button class="btn btn-square btn-primary-gradien" type="button">Primary Button</button>
                    <button class="btn btn-square btn-secondary-gradien" type="button">Secondary Button</button>
                    <button class="btn btn-square btn-success-gradien" type="button">Success Button</button>
                    <button class="btn btn-square btn-info-gradien" type="button">Info Button</button>
                    <button class="btn btn-square btn-warning-gradien" type="button">Warning Button</button>
                    <button class="btn btn-square btn-danger-gradien" type="button">Danger Button</button>
                    <button class="btn btn-square btn-light-gradien txt-dark" type="button">Light Button</button>
                    
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