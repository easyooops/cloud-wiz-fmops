<template>
  <div>
    <Breadcrumbs main="UI Kits" title="avatars" />

    <div class="container-fluid">
      <div class="user-profile">
        <div class="row">
          <Sizing />
          <StatusIndicator />
          <Shape />
          <Ratio />
          <Groups />
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import Sizing from "@/components/uikits/avatars/Sizing.vue"
import StatusIndicator from "@/components/uikits/avatars/StatusIndicator.vue"
import Shape from "@/components/uikits/avatars/Shape.vue"
import Ratio from "@/components/uikits/avatars/Ratio.vue"
import Groups from "@/components/uikits/avatars/Groups.vue"
export default {
  components: {
    Sizing,
    StatusIndicator,
    Shape,
    Ratio,
    Groups,
  }
};
</script>