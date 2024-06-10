<template>
    <div class="faq-title">
        <h6>Intellectual Property</h6>
    </div>
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon5"
                    aria-expanded="false" :class="[isActive ? 'active' : '', 'collapsible']"
                    v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress Site Maintenance ?</button>
            </h5>
        </div>
        <div class="collapse" id="collapseicon5" aria-labelledby="collapseicon5" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
                <p>We’ve just published a detailed on how to backup your WordPress website, however, if you’re in a hurry,
                    here’s a quick solution.</p>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon7"
                    aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']"
                    v-on:click="toggle"><vue-feather type="help-circle"></vue-feather> WordPress in Your Language ?</button>
            </h5>
        </div>
        <div class="collapse" id="collapseicon7" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
                <p>As of version 4.0, you can have WordPress automatically install the language of your choice during the
                    installation process.</p>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header">
            <h5 class="mb-0">
                <button class="btn btn-link collapsed" data-bs-toggle="collapse" data-bs-target="#collapseicon8"
                    aria-expanded="false" aria-controls="collapseicon2" :class="[isActive ? 'active' : '', 'collapsible']"
                    v-on:click="toggle"><vue-feather type="help-circle"></vue-feather>Integrating WordPress with Your
                    Website ?</button>
            </h5>
        </div>
        <div class="collapse" id="collapseicon8" data-parent="#accordionoc"
            :class="[isActive ? 'block' : 'none', 'content']" v-show="isActive">
            <div class="card-body">
                <p>How you approach this process will depend on which web host you use. For example, a lot of hosting
                    providers use cPanel, which includes an option to set up subdomains with just a few clicks.</p>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    data() {
        return {
            isActive: false,
            lorem: "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
        }
    },
    methods: {
        toggle() {
            this.isActive = !this.isActive
        },
    }
}
</script>