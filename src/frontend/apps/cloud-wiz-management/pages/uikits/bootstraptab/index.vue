<template>
    <breadCrumbs title="Bootstrap Tabs" main="Ui Kits" title1="Bootstrap Tabs" />
    <div class="container-fluid">
        <div class="row">
            <basicTabs />
            <botomLeftAlign />
            <tabsIcon />
            <tabsRight />
            <tabsVertical />
            <pillsTab />
            <pillsIcon />
            <pillsDark />
            <primaryColor />
            <infoWarningDanger />
        </div>
    </div>
</template>
<script>
import basicTabs from '@/components/uikits/bootstraptab/basicTabs.vue'
import botomLeftAlign from '@/components/uikits/bootstraptab/botomLeftAlign.vue';
import tabsIcon from '@/components/uikits/bootstraptab/tabsIcon.vue'
import tabsRight from '@/components/uikits/bootstraptab/tabsRight.vue'
import tabsVertical from '@/components/uikits/bootstraptab/tabsVertical.vue'
import pillsTab from '@/components/uikits/bootstraptab/piilsTab.vue'
import pillsIcon from '@/components/uikits/bootstraptab/pillsIcon.vue'
import pillsDark from '@/components/uikits/bootstraptab/pillsDark.vue'
import primaryColor from '@/components/uikits/bootstraptab/primarySecondary.vue'
import infoWarningDanger from '@/components/uikits/bootstraptab/infoWarningDanger.vue'
export default {
    name: 'bootstraptabPage',
    components: {
        basicTabs,
        botomLeftAlign, tabsIcon,
        tabsRight,
        tabsVertical, pillsTab, pillsIcon, pillsDark,
        primaryColor, infoWarningDanger
    }
}
</script>