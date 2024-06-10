import { defineNuxtConfig } from 'nuxt/config';
import { resolve } from "path";

export default defineNuxtConfig({
    // buildDir: '../../dist/apps/cloud-wiz-base/.nuxt',
    alias: {
        "@": resolve(__dirname, "/")
    },
    app: {
        head: {
            meta: [{ name: "viewport", content: "width=device-width, initial-scale=1" }],
            title: "CLOUDWIZ AI FMOPS - LLM 활용을 위한 클라우드 플랫폼",
            script: []
        }
    },
    typescript: {
        shim: false
    },
    css: [
      "vuetify/lib/styles/main.sass",
      "~/assets/css/vendors/bootstrap.min.css",
      "~/assets/css/vendors/flaticon.css",
      "~/assets/css/vendors/menu.css",
      "~/assets/css/vendors/fade-down.css",
      "~/assets/css/vendors/magnific-popup.css",
      "~/assets/css/vendors/animate.css",
      "~/assets/css/main.scss",
      "~/assets/css/responsive.scss",
      "~/assets/css/color-scheme/blue.scss",
      "~/assets/css/color-scheme/crocus.scss",
      "~/assets/css/color-scheme/green.scss",
      "~/assets/css/color-scheme/magenta.scss",
      "~/assets/css/color-scheme/pink.scss",
      "~/assets/css/color-scheme/skyblue.scss",
      "~/assets/css/color-scheme/violet.scss",
      "@mdi/font/css/materialdesignicons.min.css",
    ],
    modules: [
        [
            "@nuxtjs/google-fonts",
            {
                families: {
                    Rubik: {
                        wght: [300, 400, 500, 600, 700]
                    },
                    "Plus+Jakarta+Sans": {
                        wght: [400, 500, 600, 700]
                    },
                    Inter: {
                        wght: [400, 500, 600, 700, 800]
                    },
                    download: true,
                    inject: true
                }
            }
        ],
        [
            '@pinia/nuxt',
            {
                autoImports: [
                    // automatically imports `defineStore`
                    'defineStore',
                ],
            },
        ],
        "nuxt-swiper",
        [
            '@vee-validate/nuxt',
            {
                // disable or enable auto imports
                autoImports: true,
                // Use different names for components
                componentNames: {
                    Form: 'Form',
                    Field: 'Field',
                    FieldArray: 'FieldArray',
                    ErrorMessage: 'ErrorMessage',
                },
            },
        ]
    ],

    plugins: [
        '~/plugins/validation.ts'
    ],

    build: {
        transpile: ['@vuepic/vue-datepicker','vuetify']
    },
    buildModules: [
        '@pinia/nuxt',
        '@nuxtjs/fontawesome',
    ],
    loading: {
        color: 'blue',
        height: '5px'
    },
    fontawesome: {
        component: 'Fa',
        suffix: false,
        icons: {
            solid: true,
            brands: true,
        },
    },
    vite:{
        define: {'process.env.DEBUG':false,
        },
    },
    ssr: false
});

