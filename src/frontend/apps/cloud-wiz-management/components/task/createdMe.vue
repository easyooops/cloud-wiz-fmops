<template>
  <div class="tab-pane fade" :class="this.activeTab == 'pills-created-tab' ? 'active show' : ''" id="pills-created"
    role="tabpanel" aria-labelledby="pills-created-tab">
    <div class="card mb-0">
      <div class="card-header d-flex">
        <h5 class="mb-0">Created by me </h5><a class="f-w-600" href="javascript:void(0)"><vue-feather class="me-2"
            type="printer"></vue-feather>Print</a>
      </div>
      <div class="card-body p-0">
        <div class="taskadd">
          <div class="table-responsive">
            <table class="table">
              <tr v-for="(item, index) in tags" :key="index">
                <td>
                  <h6 class="task_title_0">{{ item.name }}</h6>
                  <p class="project_name_0">{{ item.type }}</p>
                </td>
                <td>
                  <p class="task_desc_0">{{ item.desc }}</p>
                </td>
                <td><a class="me-2" href="javascript:void(0)"><vue-feather type="link"></vue-feather></a></td>
                <td><a href="javascript:void(0)"><vue-feather type="more-horizontal"></vue-feather></a></td>
                <td><a href="#"><vue-feather type="trash-2" v-on:click="basic_warning_alert(index)"></vue-feather></a>
                </td>
              </tr>

            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'pinia'
import { useTagStore } from '~~/store/tags';
export default {

  computed: {
    ...mapState(useTagStore, {
      tags: 'tags',
    }),
    activeTab() {
      return useTagStore().activeclass
    }
  },
  methods: {

    basic_warning_alert: function (item) {
      this.$swal({
        icon: 'warning',
        title: "Are you sure?",
        text: 'Once deleted, you will not be able to recover this imaginary file!',
        showCancelButton: true,
        confirmButtonText: 'Ok',
        confirmButtonColor: '#e64942',
        cancelButtonText: 'Cancel',
        cancelButtonColor: '#efefef',
      }).then((result) => {
        if (result.value) {
          this.tags.splice(item, 1)
          this.$swal({
            icon: 'success',
            text: 'Poof! Your imaginary file has been deleted!',
            type: 'success',

          });
        } else {
          this.$swal({
            text: 'Your imaginary file is safe!'
          });
        }
      });
    }
  }
}

</script>