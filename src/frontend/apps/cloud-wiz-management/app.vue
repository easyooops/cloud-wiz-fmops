<template>
    <NuxtLayout>
        <Head>
            <Title>CLOUDWIZ AI FMOPS</Title>
        </Head>
        <NuxtPage />
    </NuxtLayout>
</template>
<script>
import { useStorage } from "@vueuse/core";

import Layout from "@/data/layout.json";
import { useProductStore } from "~/store/product";
import { useLayoutStore } from './store/layout';
export default {
    created() {},
    mounted() {
        window.addEventListener("beforeunload", (event) => {
            localStorage.setItem(
                "product",
                JSON.stringify(useProductStore().cart)
            );

            localStorage.setItem(
                "primary_color",
                useLayoutStore().primaryColor
            );

            localStorage.setItem(
                "secondary_color",
                useLayoutStore().secondaryColor
            );
        });
        let localPrimaryColor = localStorage.getItem('primary_color') || useLayoutStore().primaryColor;
        let localSecondaryColor = localStorage.getItem('secondary_color') || useLayoutStore().secondaryColor;
        useLayoutStore().intialChange({ localPrimaryColor, localSecondaryColor })
        let localStorageProducts = JSON.parse(localStorage.getItem("product"));
        if (localStorageProducts?.length) {
            useProductStore().setInitialCart(localStorageProducts);
        }
    },
    computed: {
        localPrimaryColor() {},
    },
};
</script>
