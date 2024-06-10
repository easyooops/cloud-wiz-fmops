import { defineRule, configure } from 'vee-validate';
import * as AllRules from '@vee-validate/rules';

export default defineNuxtPlugin((nuxtApp) => {
    Object.keys(AllRules).forEach(rule => {
        // @ts-ignore
        defineRule(rule, AllRules[rule]);
    });


    // vee-validate config
    configure({
        // classes: {
        //     valid: 'is-valid',
        //     invalid: 'is-invalid'
        // },
        // bails: true,
        // skipOptional: true,
        // mode: 'aggressive',
        // useConstraintAttrs: true
    });
});

