
// @ts-nocheck


export const localeCodes =  [
  "en",
  "fr",
  "es",
  "pt"
]

export const localeLoaders = {
  "en": [],
  "fr": [],
  "es": [],
  "pt": []
}

export const vueI18nConfigs = [
  () => import("../i18n.config.ts?hash=bffaebcb&config=1" /* webpackChunkName: "__i18n_config_ts_bffaebcb" */)
]

export const nuxtI18nOptions = {
  "experimental": {
    "localeDetector": ""
  },
  "bundle": {
    "compositionOnly": true,
    "runtimeOnly": false,
    "fullInstall": true,
    "dropMessageCompiler": false
  },
  "compilation": {
    "jit": true,
    "strictMessage": true,
    "escapeHtml": false
  },
  "customBlocks": {
    "defaultSFCLang": "json",
    "globalSFCScope": false
  },
  "vueI18n": "./i18n.config.ts",
  "locales": [
    {
      "icon": "flag-icon-us",
      "code": "en",
      "name": "English",
      "short": "(US)"
    },
    {
      "icon": "flag-icon-fr",
      "code": "fr",
      "name": "Français"
    },
    {
      "icon": "flag-icon-es",
      "code": "es",
      "name": "Español"
    },
    {
      "icon": "flag-icon-pt",
      "short": "(BR)",
      "code": "pt",
      "name": "Português"
    }
  ],
  "defaultLocale": "en",
  "defaultDirection": "ltr",
  "routesNameSeparator": "___",
  "trailingSlash": false,
  "defaultLocaleRouteNameSuffix": "default",
  "strategy": "prefix_except_default",
  "lazy": false,
  "langDir": null,
  "rootRedirect": null,
  "detectBrowserLanguage": {
    "alwaysRedirect": false,
    "cookieCrossOrigin": false,
    "cookieDomain": null,
    "cookieKey": "i18n_redirected",
    "cookieSecure": false,
    "fallbackLocale": "",
    "redirectOn": "root",
    "useCookie": true
  },
  "differentDomains": false,
  "baseUrl": "",
  "dynamicRouteParams": false,
  "customRoutes": "page",
  "pages": {},
  "skipSettingLocaleOnNavigate": false,
  "types": "composition",
  "debug": false,
  "parallelPlugin": false,
  "i18nModules": []
}

export const nuxtI18nOptionsDefault = {
  "experimental": {
    "localeDetector": ""
  },
  "bundle": {
    "compositionOnly": true,
    "runtimeOnly": false,
    "fullInstall": true,
    "dropMessageCompiler": false
  },
  "compilation": {
    "jit": true,
    "strictMessage": true,
    "escapeHtml": false
  },
  "customBlocks": {
    "defaultSFCLang": "json",
    "globalSFCScope": false
  },
  "vueI18n": "",
  "locales": [],
  "defaultLocale": "",
  "defaultDirection": "ltr",
  "routesNameSeparator": "___",
  "trailingSlash": false,
  "defaultLocaleRouteNameSuffix": "default",
  "strategy": "prefix_except_default",
  "lazy": false,
  "langDir": null,
  "rootRedirect": null,
  "detectBrowserLanguage": {
    "alwaysRedirect": false,
    "cookieCrossOrigin": false,
    "cookieDomain": null,
    "cookieKey": "i18n_redirected",
    "cookieSecure": false,
    "fallbackLocale": "",
    "redirectOn": "root",
    "useCookie": true
  },
  "differentDomains": false,
  "baseUrl": "",
  "dynamicRouteParams": false,
  "customRoutes": "page",
  "pages": {},
  "skipSettingLocaleOnNavigate": false,
  "types": "composition",
  "debug": false,
  "parallelPlugin": false
}

export const normalizedLocales = [
  {
    "icon": "flag-icon-us",
    "code": "en",
    "name": "English",
    "short": "(US)",
    "files": []
  },
  {
    "icon": "flag-icon-fr",
    "code": "fr",
    "name": "Français",
    "files": []
  },
  {
    "icon": "flag-icon-es",
    "code": "es",
    "name": "Español",
    "files": []
  },
  {
    "icon": "flag-icon-pt",
    "short": "(BR)",
    "code": "pt",
    "name": "Português",
    "files": []
  }
]

export const NUXT_I18N_MODULE_ID = "@nuxtjs/i18n"
export const parallelPlugin = false
export const isSSG = false

export const STRATEGIES = {
  "PREFIX": "prefix",
  "PREFIX_EXCEPT_DEFAULT": "prefix_except_default",
  "PREFIX_AND_DEFAULT": "prefix_and_default",
  "NO_PREFIX": "no_prefix"
}
export const DEFAULT_LOCALE = ""
export const DEFAULT_STRATEGY = "prefix_except_default"
export const DEFAULT_TRAILING_SLASH = false
export const DEFAULT_ROUTES_NAME_SEPARATOR = "___"
export const DEFAULT_LOCALE_ROUTE_NAME_SUFFIX = "default"
export const DEFAULT_DETECTION_DIRECTION = "ltr"
export const DEFAULT_BASE_URL = ""
export const DEFAULT_DYNAMIC_PARAMS_KEY = "nuxtI18n"


