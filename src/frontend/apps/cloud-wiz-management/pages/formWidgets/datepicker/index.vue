<template>
  <Breadcrumbs title="Date Picker" main="Form Wizards" />
  <div class="container-fluid">
    <div class="card">
      <div class="card-header">
        <h3>Date Picker</h3>
      </div>
      <div class="card-body">
        <div class="row">
          <div class="col-md-12">
            <div class="date-picker">
              <form class="theme-form">
                <div class="mb-3 row g-3">
                  <label class="col-sm-3 col-form-label text-sm-end">Default</label>
                  <div class="col-xl-5 col-sm-9">
                    <div class="input-group">
                      <Datepicker class="datepicker-here form-control digits" v-model="date" data-language="en">
                      </Datepicker>
                    </div>
                  </div>
                </div>
                <multipleDate />
                <monthDate />
                <minimumMaximum />
                <rangeDate />
                <disableDate />
                <orientationDate />
                <div class="mb-3 row g-3 mb-0">
                  <label class="col-sm-3 col-form-label text-sm-end">Permanently visible Datepicker</label>
                  <div class="col-sm-3">
                    <Datepicker1 class="datepicker-here form-control digits" inline autoApply v-model="date1" range
                      data-language="en"></Datepicker1>

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
import { ref } from 'vue';
import multipleDate from "@/components/formWidgets/datepicker/multipleDate.vue"
import monthDate from "@/components/formWidgets/datepicker/monthDate.vue"
import minimumMaximum from "@/components/formWidgets/datepicker/minimumMaximum.vue"
import rangeDate from "@/components/formWidgets/datepicker/rangeDate.vue"
import disableDate from "@/components/formWidgets/datepicker/disableDate.vue"
import orientationDate from "@/components/formWidgets/datepicker/orientationDate.vue"
export default {
  components: {
    Datepicker,
    Datepicker1,
    multipleDate,
    monthDate,
    minimumMaximum,
    rangeDate,
    disableDate,
    orientationDate
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