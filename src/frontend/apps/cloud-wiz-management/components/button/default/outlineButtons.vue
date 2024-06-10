<template>
    <div class="card" id="ex-small-btn">
        <div class="card-header">
            <h5>Extra Small buttons</h5>
            <settingPage /><span>Add <code>.btn-xs</code> class for extra small size buttons</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-primary btn-xs" type="button" title="btn btn-primary btn-xs">Primary Button</button>
            <button class="btn btn-secondary btn-xs" type="button" title="btn btn-secondary btn-xs">Secondary
                Button</button>
            <button class="btn btn-success btn-xs" type="button" title="btn btn-success btn-xs">Success Button</button>
            <button class="btn btn-info btn-xs" type="button" title="btn btn-info btn-xs">Info Button</button>
            <button class="btn btn-warning btn-xs" type="button" title="btn btn-warning btn-xs">Warning Button</button>
            <button class="btn btn-danger btn-xs" type="button" title="btn btn-danger btn-xs">Danger Button</button>
            <button class="btn btn-light btn-xs" type="button" title="btn btn-light btn-xs">Light Button</button>
        </div>
    </div>
    <div class="card" id="active-btn">
        <div class="card-header">
            <h5>Active Buttons</h5>
            <settingPage /><span>Add <code>.active</code> class for active state</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-primary active" type="button" title="btn btn-primary active">Active</button>
            <button class="btn btn-secondary active" type="button" title="btn btn-secondary active">Active</button>
            <button class="btn btn-success active" type="button" title="btn btn-success active">Active</button>
            <button class="btn btn-info active" type="button" title="btn btn-info active">Active</button>
            <button class="btn btn-warning active txt-dark" type="button" title="btn btn-warning active">Active</button>
            <button class="btn btn-danger active" type="button" title="btn btn-danger active">Active</button>
            <button class="btn btn-light active txt-dark" type="button" title="btn btn-light active">Active</button>

        </div>
    </div>
    <div class="card" id="disabled-btn">
        <div class="card-header">
            <h5>Disabled Buttons</h5>
            <settingPage /><span>Add <code>.disabled</code> class or <code>disabled="disabled"</code> attribute for disabled
                button</span>
        </div>
        <div class="card-body btn-showcase">
            <button class="btn btn-primary disabled" type="button">Disabled</button>
            <button class="btn btn-secondary disabled" type="button">Disabled</button>
            <button class="btn btn-success disabled" type="button">Disabled</button>
            <button class="btn btn-info disabled" type="button">Disabled</button>
            <button class="btn btn-warning disabled" type="button">Disabled</button>
            <button class="btn btn-danger disabled" type="button">Disabled</button>
            <button class="btn btn-light disabled" type="button">Disabled</button>
        </div>
    </div>
</template>
<script>

export default {
    inject: ['Tooltip'],
    mounted() {
        new this.Tooltip(document.body, {
            selector: "[data-bs-toggle='tooltip']"
        })
    }
}
</script>