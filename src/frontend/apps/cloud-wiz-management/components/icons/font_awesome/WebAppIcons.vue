<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Web App Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(webi, index) in webicons" :key="index"
                        v-on:click="icon_bar(webi.name)">
                        <i class="" :class="'fa fa-' + webi.name"></i>{{ webi.name }}
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

            webicons: [{ name: 'adjust' }, { name: 'anchor' }, { name: 'archive' }, { name: 'arrows' }, { name: 'arrows-h' }, { name: 'arrows-v' }, { name: 'asterisk' }, { name: 'automobile' }, { name: 'ban' }, { name: 'bank' }, { name: 'bar-chart-o' }, { name: 'barcode' }, { name: 'bars' }, { name: 'beer' }, { name: 'bell' }, { name: 'bell-o' }, { name: 'bolt' }, { name: 'bomb' }, { name: 'book' }, { name: 'bookmark' }, { name: 'bookmark-o' }, { name: 'briefcase' }, { name: 'bug' }, { name: 'building' }, { name: 'building-o' }, { name: 'bullhorn' }, { name: 'bullseye' }, { name: 'cab' }, { name: 'calendar' }, { name: 'calendar-o' }, { name: 'camera' }, { name: 'camera-retro' }, { name: 'car' }, { name: 'caret-square-o-down' }, { name: 'caret-square-o-left' }, { name: 'caret-square-o-right' }, { name: 'caret-square-o-up' }, { name: 'certificate' }, { name: 'check' }, { name: 'check-circle' }, { name: 'check-circle-o' }, { name: 'check-square' }, { name: 'check-square-o' }, { name: 'child' }, { name: 'circle' }, { name: 'circle-o' }, { name: 'circle-o-notch' }, { name: 'circle-thin' }, { name: 'clock-o' }, { name: 'cloud' }, { name: 'cloud-download' }, { name: 'cloud-upload' }, { name: 'code' }, { name: 'code-fork' }, { name: 'coffee' }, { name: 'cog' }, { name: 'cogs' }, { name: 'comment' }, { name: 'comment-o' }, { name: 'comments' }, { name: 'comments-o' }, { name: 'compass' }, { name: 'credit-card' }, { name: 'crop' }, { name: 'crosshairs' }, { name: 'cube' }, { name: 'cubes' }, { name: 'cutlery' }, { name: 'dashboard' }, { name: 'database' }, { name: 'desktop' }, { name: 'dot-circle-o' }, { name: 'download' }, { name: 'edit' }, { name: 'ellipsis-h' }, { name: 'ellipsis-v' }, { name: 'envelope' }, { name: 'envelope-o' }, { name: 'envelope-square' }, { name: 'eraser' }, { name: 'exchange' }, { name: 'exclamation' }, { name: 'exclamation-circle' }, { name: 'exclamation-triangle' }, { name: 'external-link' }, { name: 'external-link-square' }, { name: 'eye' }, { name: 'eye-slash' }, { name: 'fax' }, { name: 'female' }, { name: 'fighter-jet' }, { name: 'file-archive-o' }, { name: 'file-audio-o' }, { name: 'file-code-o' }, { name: 'file-excel-o' }, { name: 'file-image-o' }, { name: 'file-movie-o' }, { name: 'file-pdf-o' }, { name: 'file-photo-o' }, { name: 'file-picture-o' }, { name: 'file-powerpoint-o' }, { name: 'file-sound-o' }, { name: 'file-video-o' }, { name: 'file-word-o' }, { name: 'file-zip-o' }, { name: 'film' }, { name: 'filter' }, { name: 'fire' }, { name: 'fire-extinguisher' }, { name: 'flag' }, { name: 'flag-checkered' }, { name: 'flag-o' }, { name: 'flash' }, { name: 'flask' }, { name: 'folder' }, { name: 'folder-o' }, { name: 'folder-open' }, { name: 'folder-open-o' }, { name: 'frown-o' }, { name: 'gamepad' }, { name: 'gavel' }, { name: 'gear' }, { name: 'gears' }, { name: 'gift' }, { name: 'glass' }, { name: 'globe' }, { name: 'graduation-cap' }, { name: 'group' }, { name: 'hdd-o' }, { name: 'headphones' }, { name: 'heart' }, { name: 'heart-o' }, { name: 'history' }, { name: 'home' }, { name: 'image' }, { name: 'inbox' }, { name: 'info' }, { name: 'info-circle' }, { name: 'institution' }, { name: 'key' }, { name: 'keyboard-o' }, { name: 'language' }, { name: 'laptop' }, { name: 'leaf' }, { name: 'legal' }, { name: 'lemon-o' }, { name: 'level-down' }, { name: 'level-up' }, { name: 'life-bouy' }, { name: 'life-ring' }, { name: 'life-saver' }, { name: 'lightbulb-o' }, { name: 'location-arrow' }, { name: 'lock' }, { name: 'magic' }, { name: 'magnet' }, { name: 'mail-forward' }, { name: 'mail-reply' }, { name: 'mail-reply-all' }, { name: 'male' }, { name: 'map-marker' }, { name: 'meh-o' }, { name: 'microphone' }, { name: 'microphone-slash' }, { name: 'minus' }, { name: 'minus-circle' }, { name: 'minus-square' }, { name: 'minus-square-o' }, { name: 'mobile' }, { name: 'mobile-phone' }, { name: 'money' }, { name: 'moon-o' }, { name: 'mortar-board' }, { name: 'music' }, { name: 'navicon' }, { name: 'paper-plane' }, { name: 'paper-plane-o' }, { name: 'paw' }, { name: 'pencil' }, { name: 'pencil-square' }, { name: 'pencil-square-o' }, { name: 'phone' }, { name: 'phone-square' }, { name: 'photo' }, { name: 'picture-o' }, { name: 'plane' }, { name: 'plus' }, { name: 'plus-circle' }, { name: 'plus-square' }, { name: 'plus-square-o' }, { name: 'power-off' }, { name: 'print' }, { name: 'puzzle-piece' }, { name: 'qrcode' }, { name: 'question' }, { name: 'question-circle' }, { name: 'quote-left' }, { name: 'quote-right' }, { name: 'random' }, { name: 'recycle' }, { name: 'refresh' }, { name: 'reorder' }, { name: 'reply' }, { name: 'reply-all' }, { name: 'retweet' }, { name: 'road' }, { name: 'rocket' }, { name: 'rss' }, { name: 'rss-square' }, { name: 'search' }, { name: 'search-minus' }, { name: 'search-plus' }, { name: 'send' }, { name: 'send-o' }, { name: 'share' }, { name: 'share-alt' }, { name: 'share-alt-square' }, { name: 'share-square' }, { name: 'share-square-o' }, { name: 'shield' }, { name: 'shopping-cart' }, { name: 'sign-in' }, { name: 'sign-out' }, { name: 'signal' }, { name: 'sitemap' }, { name: 'sliders' }, { name: 'smile-o' }, { name: 'sort' }, { name: 'sort-alpha-asc' }, { name: 'sort-alpha-desc' }, { name: 'sort-amount-asc' }, { name: 'sort-amount-desc' }, { name: 'sort-asc' }, { name: 'sort-desc' }, { name: 'sort-down' }, { name: 'sort-numeric-asc' }, { name: 'sort-numeric-desc' }, { name: 'sort-up' }, { name: 'space-shuttle' }, { name: 'spinner' }, { name: 'spoon' }, { name: 'square' }, { name: 'square-o' }, { name: 'star' }, { name: 'star-half' }, { name: 'star-half-empty' }, { name: 'star-half-full' }, { name: 'star-half-o' }, { name: 'star-o' }, { name: 'suitcase' }, { name: 'sun-o' }, { name: 'support' }, { name: 'tablet' }, { name: 'tachometer' }, { name: 'tag' }, { name: 'tags' }, { name: 'tasks' }, { name: 'taxi' }, { name: 'terminal' }, { name: 'thumb-tack' }, { name: 'thumbs-down' }, { name: 'thumbs-o-down' }, { name: 'thumbs-o-up' }, { name: 'thumbs-up' }, { name: 'ticket' }, { name: 'times' }, { name: 'times-circle' }, { name: 'times-circle-o' }, { name: 'tint' }, { name: 'toggle-down' }, { name: 'toggle-left' }, { name: 'toggle-right' }, { name: 'toggle-up' }, { name: 'trash-o' }, { name: 'tree' }, { name: 'trophy' }, { name: 'truck' }, { name: 'umbrella' }, { name: 'university' }, { name: 'unlock' }, { name: 'unlock-alt' }, { name: 'unsorted' }, { name: 'upload' }, { name: 'user' }, { name: 'users' }, { name: 'video-camera' }, { name: 'volume-down' }, { name: 'volume-off' }, { name: 'volume-up' }, { name: 'warning' }, { name: 'wheelchair' }, { name: 'wrench' }],
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