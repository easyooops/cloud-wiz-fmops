<template>
  <div class="card mb-0">
    <div class="card-header d-flex">
      <h5>Organization</h5><span class="f-14 pull-right mt-0">{{ menu.slice(3).length }} Contacts</span>
    </div>
    <div class="card-body p-0">
      <div class="row list-persons">
        <div class="col-xl-4 xl-50 col-md-5">
          <div class="nav flex-column nav-pills" id="v-pills-tab1" role="tablist" aria-orientation="vertical">
            <a class="nav-link" :class="this.activeTab == item.activeTab ? 'active' : ''" id="v-pills-iduser-tab"
              data-bs-toggle="pill" href="#v-pills-iduser" role="tab" aria-controls="v-pills-iduser" aria-selected="true"
              v-for="(item, index) in menu.slice(3)" :key="index" @click="activeDiv(item.activeTab)">
              <div class="media"><img class="img-50 img-fluid m-r-20 rounded-circle" :src="getImgUrl(item.img)" alt="">
                <div class="media-body">
                  <h6>{{ item.name }}</h6>
                  <p>{{ item.email }}</p>
                </div>
              </div>
            </a>
          </div>
        </div>
        <div class="col-xl-8 xl-50 col-md-7">
          <div class="tab-content" id="v-pills-tabContent1">
            <div class="tab-pane fade" :class="item.activeTab === this.activeTab ? 'active show' : ''" id="v-pills-iduser"
              role="tabpanel" aria-labelledby="v-pills-iduser-tab" v-for="(item, index) in menu.slice(3)" :key="index">
              <div class="profile-mail" v-if="this.activeTab == item.activeTab">
                <div class="media"><img class="img-100 img-fluid m-r-20 rounded-circle update_img_5"
                    :src="getImgUrl(item.img)" alt="">
                  <div class="media-body mt-0">
                    <h3><span class="first_name_5">{{ item.name }} </span><span class="last_name_5">{{ item.lastName }}</span>
                    </h3>
                    <p class="email_add_5">{{ item.email }}</p>
                    <ul>
                      <li><a href="javascript:void(0)" @click="activeDiv(item)" data-bs-toggle="modal"
                          data-bs-target="#printModal">Print</a></li>
                    </ul>
                  </div>
                </div>
                <div class="email-general">
                  <h4>General</h4>
                  <p>Email Address: <span class="font-primary email_add_5">markjecno@gmail.com</span></p>
                  <div class="gender">
                    <h4>Personal</h4>
                    <p>Gender: <span>Male</span></p>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import menu from '@/data/contact.json'

import { useContactStore } from '~~/store/contact'
export default {
  data() {
    return {
      menu: menu.data
    }
  },
  computed: {

    display() {
      return useContactStore().display
    },
    activeTab() {
      return useContactStore().activeTab
    },

  },
  methods: {
    getImgUrl(path) {
      return ('/images/' + path)
    },
    activeDiv(item) {
      useContactStore().active(item)
    },
  }
}
</script>
    