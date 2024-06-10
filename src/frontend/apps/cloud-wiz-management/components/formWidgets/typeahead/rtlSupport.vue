<template>
    <div class="col-sm-12 text-start">
        <div class="card">
            <div class="card-header">
                <h5>RTL Support</h5><span>Dataset shows in Right Side.</span>
            </div>
            <div class="card-body">
                <div id="rtl-support">
                    <form class="theme-form">
                        <div class="form-group">
                            <vue3-simple-typeahead :items="list" class="form-control typeahead form-control" dir="rtl"
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
                placeholder: 'Countries',
                minInputLength: 1,
            },
            list: [
                "India",
                "USA",
                "Australia",
                "UEA",
                "China"
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
