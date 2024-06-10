<template>
  <tourProfile />
  <tourProfile2 />
  <tourProfile3 />
  <tourProfile4 />
  <tourProfile5 />
</template>

<script>
import tourProfile from "./tourProfile.vue";
import tourProfile2 from "./tourProfile2.vue";
import tourProfile3 from "./tourProfile3.vue";
import tourProfile4 from "./tourProfile4.vue";
import tourProfile5 from "./tourProfile5.vue";

export default {
  name: 'userProfile',
  components: {
    tourProfile,
    tourProfile2,
    tourProfile3,
    tourProfile4,
    tourProfile5,
  },

}
</script>
