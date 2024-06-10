<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5 class="m-b-0">Brand Icons</h5>
            </div>
            <div class="card-body">
                <div class="row icon-lists">

                    <div class="col-sm-6 col-md-4 col-xl-3" v-for="(brand, index) in branddicons" :key="index"
                        v-on:click="icon_bar(brand.name)">
                        <i class="" :class="'fa fa-' + brand.name"></i>{{ brand.name }}
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

            branddicons: [{ name: 'adn' }, { name: 'android' }, { name: 'apple' }, { name: 'behance' }, { name: 'behance-square' }, { name: 'bitbucket' }, { name: 'bitbucket-square' }, { name: 'bitcoin' }, { name: 'btc' }, { name: 'codepen' }, { name: 'css3' }, { name: 'delicious' }, { name: 'deviantart' }, { name: 'digg' }, { name: 'dribbble' }, { name: 'dropbox' }, { name: 'drupal' }, { name: 'empire' }, { name: 'facebook' }, { name: 'facebook-square' }, { name: 'flickr' }, { name: 'foursquare' }, { name: 'ge' }, { name: 'git' }, { name: 'git-square' }, { name: 'github' }, { name: 'github-alt' }, { name: 'github-square' }, { name: 'gittip' }, { name: 'google' }, { name: 'google-plus' }, { name: 'google-plus-square' }, { name: 'hacker-news' }, { name: 'html5' }, { name: 'instagram' }, { name: 'joomla' }, { name: 'jsfiddle' }, { name: 'linkedin' }, { name: 'linkedin-square' }, { name: 'linux' }, { name: 'maxcdn' }, { name: 'openid' }, { name: 'pagelines' }, { name: 'pied-piper' }, { name: 'pied-piper-alt' }, { name: 'pinterest' }, { name: 'pinterest-square' }, { name: 'qq' }, { name: 'ra' }, { name: 'rebel' }, { name: 'reddit' }, { name: 'reddit-square' }, { name: 'renren' }, { name: 'share-alt' }, { name: 'share-alt-square' }, { name: 'skype' }, { name: 'slack' }, { name: 'soundcloud' }, { name: 'spotify' }, { name: 'stack-exchange' }, { name: 'stack-overflow' }, { name: 'steam' }, { name: 'steam-square' }, { name: 'stumbleupon' }, { name: 'stumbleupon-circle' }, { name: 'tencent-weibo' }, { name: 'trello' }, { name: 'tumblr' }, { name: 'tumblr-square' }, { name: 'twitter' }, { name: 'twitter-square' }, { name: 'vimeo-square' }, { name: 'vine' }, { name: 'vk' }, { name: 'wechat' }, { name: 'weibo' }, { name: 'weixin' }, { name: 'windows' }, { name: 'wordpress' }, { name: 'xing' }, { name: 'xing-square' }, { name: 'yahoo' }, { name: 'youtube' }, { name: 'youtube-play' }, { name: 'youtube-square' }],
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