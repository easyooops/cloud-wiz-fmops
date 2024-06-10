<template>
  <div>
    <Breadcrumbs main="UI Kits" title="alert" />

    <div class="container-fluid">
      <div class="row">
        <ThemeColorAlerts />
        <LinkColorinTheme />
        <Dismissing />
        <AlertWithIcon />
        <LightAlerts />
        <LinkColor />
        <Dismissing1 />
        <OutlineAlerts />
        <OutlineDarkAlerts />
        <AlertWithIconoutline />
        <AlertWithIconinverse />
        <TextAsAction />
        <AdditionalContent />
      </div>
    </div>
  </div>
</template>

<script>
import ThemeColorAlerts from "@/components/uikits/alert/ThemeColorAlerts.vue"
import LinkColorinTheme from "@/components/uikits/alert/LinkColorinTheme-color.vue"
import Dismissing from "@/components/uikits/alert/Dismissing.vue";
import AlertWithIcon from "@/components/uikits/alert/AlertWithIcon.vue";
import LightAlerts from "@/components/uikits/alert/LightAlerts.vue";
import LinkColor from "@/components/uikits/alert/LinkColor.vue";
import Dismissing1 from "@/components/uikits/alert/Dismissing1.vue";
import OutlineAlerts from "@/components/uikits/alert/OutlineAlerts.vue";
import OutlineDarkAlerts from "@/components/uikits/alert/OutlineDarkAlerts.vue";
import AlertWithIconoutline from "@/components/uikits/alert/AlertWithIconoutline.vue";
import AlertWithIconinverse from "@/components/uikits/alert/AlertWithIconinverse.vue";
import TextAsAction from "@/components/uikits/alert/TextAsAction.vue";
import AdditionalContent from "@/components/uikits/alert/AdditionalContent.vue";
export default {
  components: {
    ThemeColorAlerts,
    LinkColorinTheme,
    Dismissing,
    AlertWithIcon,
    LightAlerts,
    LinkColor,
    Dismissing1,
    OutlineAlerts,
    OutlineDarkAlerts,
    AlertWithIconoutline,
    AlertWithIconinverse,
    TextAsAction,
    AdditionalContent
  },
  data() {
    return {
      primary: true,
      secondary: true,
      success: true,
      info: true,
      warning: true,
      danger: true,
      light: true,
      dark: true,
    };
  }
};
</script>