<template>
  <div class="col-sm-12 text-start">
    <div class="card">
      <div class="card-header">
        <h5>Alert State</h5>
      </div>
      <div class="card-body btn-showcase">
        <button
          class="btn btn-success sweet-8"
          type="button"
          v-on:click="success_alert_state"
        >
          Success
        </button>
        <button
          class="btn btn-danger sweet-7"
          type="button"
          v-on:click="danger_alert_state"
        >
          Danger
        </button>
        <button
          class="btn btn-info sweet-9"
          type="button"
          v-on:click="info_alert_state"
        >
          Information
        </button>
        <button
          class="btn btn-warning sweet-6"
          type="button"
          v-on:click="warning_alert_state"
        >
          Warning
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    success_alert_state: function () {
      this.$swal({
        icon: "success",
        title: "Good job!",
        text: "You clicked the button!",
        type: "success",
      });
    },
    danger_alert_state: function () {
      this.$swal({
        icon: "error",
        title: "Good job!",
        text: "You clicked the button!",
        type: "error",
      });
    },
    info_alert_state: function () {
      this.$swal({
        icon: "info",
        title: "Good job!",
        text: "You clicked the button!",
        type: "info",
      });
    },
    warning_alert_state: function () {
      this.$swal({
        icon: "warning",
        title: "Good job!",
        text: "You clicked the button!",
        type: "warning",
      });
    },
  },
};
</script>