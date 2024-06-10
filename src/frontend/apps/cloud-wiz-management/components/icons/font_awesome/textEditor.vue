<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Text Editor Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(texteditor, index) in texteditoricons" :key="index"
                        v-on:click="icon_bar(texteditor.name)">
                        <i class="" :class="'fa fa-' + texteditor.name"></i>{{ texteditor.name }}
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>
<script>

export default {
    data() {
        return {
            customAnimation: {
                enter: "animated bounce",
                exit: "animated bounce",
            },
            icon_bar_status: false,

            select_icon: {
                class: '',
                tag: ''
            },

            texteditoricons: [{ name: 'align-center' }, { name: 'align-justify' }, { name: 'align-left' }, { name: 'align-right' }, { name: 'bold' }, { name: 'chain' }, { name: 'chain-broken' }, { name: 'clipboard' }, { name: 'columns' }, { name: 'copy' }, { name: 'cut' }, { name: 'dedent' }, { name: 'eraser' }, { name: 'file' }, { name: 'file-o' }, { name: 'file-text' }, { name: 'file-text-o' }, { name: 'files-o' }, { name: 'floppy-o' }, { name: 'font' }, { name: 'header' }, { name: 'indent' }, { name: 'italic' }, { name: 'link' }, { name: 'list' }, { name: 'list-alt' }, { name: 'list-ol' }, { name: 'list-ul' }, { name: 'outdent' }, { name: 'paperclip' }, { name: 'paragraph' }, { name: 'paste' }, { name: 'repeat' }, { name: 'rotate-left' }, { name: 'rotate-right' }, { name: 'save' }, { name: 'scissors' }, { name: 'strikethrough' }, { name: 'subscript' }, { name: 'superscript' }, { name: 'table' }, { name: 'text-height' }, { name: 'text-width' }, { name: 'th' }, { name: 'th-large' }, { name: 'th-list' }, { name: 'underline' }, { name: 'undo' }, { name: 'unlink' }],
        };
    },
    methods: {
        icon_bar(icon) {

            this.$emit('selected', icon);
        },
    }
};
</script>
<style lang="scss" scoped>
@import "@/assets/scss/vendors/animate.scss"
</style>