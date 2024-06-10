<template>
  <div>
    <Breadcrumbs main="UI Kits" title="Dropdown" />

    <div class="container-fluid">
      <div class="row">
        <BasicDropdown />
        <BasicColorDropdown />
        <DropdownSplitButton />
        <RoundedDropdown />
        <DropdownWithDivider />
        <DropdownWithHeader />
        <DropdownWithDisable />
        <DropdownWithDropUp />
      </div>
    </div>

  </div>
</template>

<script>
import BasicDropdown from "@/components/uikits/dropdown/BasicDropdown.vue"
import BasicColorDropdown from "@/components/uikits/dropdown/BasicColorDropdown.vue"
import DropdownSplitButton from "@/components/uikits/dropdown/DropdownSplitButton.vue"
import RoundedDropdown from "@/components/uikits/dropdown/RoundedDropdown.vue"
import DropdownWithDivider from "@/components/uikits/dropdown/DropdownWithDivider.vue"
import DropdownWithHeader from "@/components/uikits/dropdown/DropdownWithHeader.vue"
import DropdownWithDisable from "@/components/uikits/dropdown/DropdownWithDisable.vue"
import DropdownWithDropUp from "@/components/uikits/dropdown/DropdownWithDropUp.vue"
export default {
  components: {
    BasicDropdown,
    BasicColorDropdown,
    DropdownSplitButton,
    RoundedDropdown,
    DropdownWithDivider,
    DropdownWithHeader,
    DropdownWithDisable,
    DropdownWithDropUp

  }
};
</script>