import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
    // buildDir: '../../dist/apps/cloud-wiz-menagement/.nuxt',
    css: ["@/assets/scss/app.scss"],
    ssr:false,
    target: 'static',
    generate: {
        fallback: '404.html'
    },
    app: {
        head: {
            link: [
                {
                    href: "https://fonts.googleapis.com/css?family=Rubik:400,400i,500,500i,700,700i&amp;display=swap",
                    rel: "stylesheet",
                },
                {
                    href: "https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,500,500i,700,700i,900&amp;display=swap",
                    rel: "stylesheet",
                },
            ],
            title: "CLOUDWIZ AI FMOPS - LLM 활용을 위한 클라우드 플랫폼",
            script: [
                {
                    src: "https://www.paypal.com/sdk/js?client-id=test&currency=USD",
                },
                { src: "https://checkout.stripe.com/checkout.js" },
                { src: 'https://accounts.google.com/gsi/client', async:true, defer:true}
            ],
        },
    },
    // alias: {
    //     pinia: "/node_modules/@pinia/nuxt/node_modules/pinia/dist/pinia.mjs"
    //     },
    modules: [
        "@nuxtjs/i18n",
        [
            "@pinia/nuxt",
            {
                autoImports: ["defineStore",'acceptHMRUpdate'],
            },
        ],
    ],
    // debug: false,
    i18n: {
        strategy: "prefix_except_default",
        defaultLocale: "en",
        locales: [
            {
                icon: "flag-icon-us",
                code: "en",
                name: "English",
                short: "(US)"
            },
            {
                icon: "flag-icon-fr",
                code: "fr",
                name: "Français"
            },
            {
                icon: "flag-icon-es",
                code: "es",
                name: "Español"
            },
            {
                icon: "flag-icon-pt",
                short: "(BR)",
                code: "pt",
                name: "Português"
            }
        ],
        vueI18n: "./i18n.config.ts"
    },
    plugins: [
        { src: "~/plugins/plugins.js", mode: "client" },
        { src: "~/plugins/google-oauth.js", mode: "client" },
        { src: "./plugins/useBootstrap.client.ts", mode: "client" }
    ]   
});
