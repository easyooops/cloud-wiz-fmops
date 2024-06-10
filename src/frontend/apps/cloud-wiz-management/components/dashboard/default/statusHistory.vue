<template>
  <!--  <Breadcrumbs title="Date Picker" main="Form Wizards" />-->
  <h5>Statue History</h5>
  <div class="container-fluid">
    <div class="card">
      <!--      <div class="card-header">-->
      <!--        <h3>Date Picker</h3>-->
      <!--      </div>-->
      <div class="card-body">
        <div class="row">
          <div class="col-md-12">
            <div class="date-picker">
              <form>
                <div class="mb-3 row g-3 mb-0">
                  <div class="col-sm-3">
                    <Datepicker1 class="datepicker-here form-control digits"
                                 inline autoApply v-model="date1" range
                                 data-language="en">
                    </Datepicker1>
                    <br/>
                    <div class="col">
                      <div class="form-group m-t-15 mb-0 m-checkbox-inline">
                        <div class="checkbox checkbox-solid-info">
                          <input id="solid6" type="checkbox" checked="">
                          <label for="solid6">Info</label>
                        </div>
                        <div class="checkbox checkbox-solid-warning">
                          <input id="solid6" type="checkbox" checked="">
                          <label for="solid6">Warning</label>
                        </div>
                        <div class="checkbox checkbox-solid-success">
                          <input id="solid1" type="checkbox" checked="">
                          <label for="solid1">Resolved</label>
                        </div>
                        <div class="checkbox checkbox-solid-danger">
                          <input id="solid4" type="checkbox" checked="">
                          <label for="solid4">Error</label>
                        </div>
                      </div>
                    </div>

                    <br/>
                    <!--                    <label class="form-label" for="validationDefault01">Message</label>-->
                    <input class="form-control input-air-primary" id="exampleFormControlInput15" type="text"
                           placeholder="Content..">

                    <br/>
                    <button class="btn btn-primary m-r-15" type="submit">Search</button>


                  </div>
                  <div class="col-sm-9">
                    <statusHitoryTable/>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Datepicker from "vue3-datepicker";
import Datepicker1 from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import {ref} from 'vue';
import multipleDate from "~/components/formWidgets/datepicker/multipleDate.vue"
import monthDate from "~/components/formWidgets/datepicker/monthDate.vue"
import minimumMaximum from "~/components/formWidgets/datepicker/minimumMaximum.vue"
import rangeDate from "~/components/formWidgets/datepicker/rangeDate.vue"
import disableDate from "~/components/formWidgets/datepicker/disableDate.vue"
import orientationDate from "~/components/formWidgets/datepicker/orientationDate.vue"

import statusHitoryTable from "~/components/tables/bootstrapTable/basicTables/statusHistoryTable.vue"

export default {
  components: {
    // Datepicker,
    Datepicker1,
    // multipleDate,
    // monthDate,
    // minimumMaximum,
    rangeDate,
    // disableDate,
    // orientationDate
    statusHitoryTable,
  },
  data() {
    return {
      date: new Date(),
      date1: [this.startDate, this.endDate],
    }
  },
  setup() {
    const date3 = ref();
    return {
      date3,
    }
  }
}
</script>