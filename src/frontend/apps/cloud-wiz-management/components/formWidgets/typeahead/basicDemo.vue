<template>
    <div class="col-sm-12 col-md-6 text-start">
        <div class="card">
            <div class="card-header">
                <h5>Basic Demo</h5><span>This is the simple demo for Typeahead.</span>
            </div>
            <div class="card-body">
                <div id="the-basics">
                    <form class="theme-form">
                        <div class="form-group">
                            <vue3-simple-typeahead :items="list" class="form-control typeahead form-control"
                                :placeholder="options.placeholder" @selectItem="selectItem" @onInput="onInput"
                                @onBlur="onBlur" :minInputLength="options.minInputLength" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    created() {
        this.listFiltered = this.list;
    },
    data() {
        return {
            options: {
                placeholder: 'States of USA',
                minInputLength: 1,
            },
            list: [
                'alabama',
                'alaska',
                'arizona',
                'arkansas',
                'california',
                'colorado',
                'connecticut',
                'delaware',
                'florida',
                'georgia',
                'hawaii',
                'idaho',
                'illinois',
                'indiana',
                'iowa',
                'kansas',
                'kentucky',
                'louisiana',
                'maine',
                'maryland',
                'massachusetts',
                'michigan',
                'minnesota',
                'mississippi',
                'missouri',
                'montana',
                'nebraska',
                'nevada',
                'new hampshire',
                'new jersey',
                'new mexico',
                'new york',
                'north carolina',
                'north dakota',
                'ohio',
                'oklahoma',
                'oregon',
                'pennsylvania',
                'rhode island',
                'south carolina',
                'south dakota',
                'tennessee',
                'texas',
                'utah',
                'vermont',
                'virginia',
                'washington',
                'west virginia',
                'wisconsin',
                'wyoming'
            ],
            listFiltered: [],
        };
    },
    methods: {
        selectItem(item) {
            this.data.selection = item;
        },
        onInput(event) {
            this.listFiltered = event.items;
        },
        onBlur(event) {
            this.data.input = event.input;
            this.listFiltered = event.items;
        },
    },
};
</script>