<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Helper Classes" />
    <div class="container-fluid">
      <div class="row">
        <Padding />
        <Margins />
        <PaddingLeft />
        <PaddingRight />
        <PaddingTop />
        <PaddingBottom />
        <MarginLeft />
        <MarginRight />
        <MarginTop />
        <MarginBottom />
        <VerticalAlign />
        <ImageSizes />
        <TextColor />
        <BadgeColor />
        <BackgroundColor />
        <ButtonColor />
        <div class="col-md-6 col-sm-12">
          <BorderRadius />
          <FontWeight />
          <FontStyle />
          <Float />
          <Overflow />
        </div>
        <FontSize></FontSize>
        <AllBordersColor />
        <div class="col-md-6 col-sm-12">
          <BorderWidth />
          <Position />
          <ButtonOutline />
        </div>
      </div>
    </div>
  </div>
</template> 
<script>
import Padding from "@/components/uikits/helperClass/Padding.vue"
import Margins from "@/components/uikits/helperClass/Margins.vue";
import PaddingLeft from "@/components/uikits/helperClass/PaddingLeft.vue"
import PaddingRight from "@/components/uikits/helperClass/PaddingRight.vue";
import PaddingTop from "@/components/uikits/helperClass/PaddingTop.vue";
import PaddingBottom from "@/components/uikits/helperClass/PaddingBottom.vue";
import MarginLeft from "@/components/uikits/helperClass/MarginLeft.vue";
import MarginRight from "@/components/uikits/helperClass/MarginRight.vue";
import MarginTop from "@/components/uikits/helperClass/MarginTop.vue";
import MarginBottom from "@/components/uikits/helperClass/MarginBottom.vue";
import VerticalAlign from "@/components/uikits/helperClass/VerticalAlign.vue"
import ImageSizes from "@/components/uikits/helperClass/ImageSizes.vue";
import TextColor from "@/components/uikits/helperClass/TextColor.vue";
import BadgeColor from "@/components/uikits/helperClass/BadgeColor.vue";
import BackgroundColor from "@/components/uikits/helperClass/BackgroundColor.vue";
import ButtonColor from "@/components/uikits/helperClass/ButtonColor.vue";
import BorderRadius from "@/components/uikits/helperClass/BorderRadius.vue";
import FontSize from "@/components/uikits/helperClass/FontSize.vue";
import FontWeight from "@/components/uikits/helperClass/FontWeight.vue";
import FontStyle from "@/components/uikits/helperClass/FontStyle.vue";
import Float from "@/components/uikits/helperClass/Float.vue";
import Overflow from "@/components/uikits/helperClass/Overflow.vue";
import AllBordersColor from "@/components/uikits/helperClass/AllBordersColor.vue";
import BorderWidth from "@/components/uikits/helperClass/BorderWidth.vue";
import Position from "@/components/uikits/helperClass/Position.vue";
import ButtonOutline from "@/components/uikits/helperClass/ButtonOutline.vue";
export default {
  components: {
    Padding,
    Margins,
    PaddingLeft,
    PaddingRight,
    PaddingTop,
    PaddingBottom,
    MarginLeft,
    MarginRight,
    MarginTop,
    MarginBottom,
    VerticalAlign,
    ImageSizes,
    TextColor,
    BadgeColor,
    BackgroundColor,
    ButtonColor,
    BorderRadius,
    FontSize,
    FontWeight,
    FontStyle,
    Float,
    Overflow,
    AllBordersColor,
    BorderWidth,
    Position,
    ButtonOutline
  }
};
</script>