<template>
    <div class="mb-2">
        <label class="col-form-label">Select2 single select</label>
        <multiselect v-model="value" :options="options1" :searchable="false" group-values="libs" group-label="language"
            :group-select="true" :close-on-select="false" track-by="name" label="name" placeholder="Pick a value">
        </multiselect>
    </div>
</template>
<script>
import multiselect from 'vue-multiselect'

export default {
    components: { multiselect, },
    data() {
        return {

            options1: [
                {
                    language: 'Developer',
                    libs: [
                        { name: 'Alabama', category: 'Front-end' },
                        { name: 'Wyoming', category: 'Backend' }
                    ]
                },
                {
                    language: 'Designer',
                    libs: [
                        { name: 'Peter', category: 'Backend' },
                        { name: 'Hanry Die', category: 'Backend' },
                        { name: 'John Doe', category: 'Backend' }
                    ]
                },
            ],
            value: [{ name: 'Alabama', category: 'Front-end' },]
        }
    }
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>