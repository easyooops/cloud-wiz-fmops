<template>
  <div class="col-md-12 project-list">
    <div class="card">
      <div class="row">
        <div class="col-md-6 d-flex">
          <ul class="nav nav-tabs border-tab" id="top-tab" role="tablist">
            <li v-for="(item,index) in tab" :key="index" class="nav-item">
              <a class="nav-link" :class="{ 'active': item.active }" :id="item.label" data-bs-toggle="tab" href="javascript:void(0)" role="tab" :aria-controls="item.id" :aria-selected="item.active ? 'true':'false'" @click.prevent="active(item)">
                <vue-feather :type="item.icon"></vue-feather>{{ item.name }}
              </a>
            </li>
          </ul>
        </div>
        <div class="col-md-6">
          <div class="form-group mb-0 me-0"></div>
          <nuxt-link class="btn btn-primary" to="/provider/create">
            <vue-feather class="me-1" type="plus-square"> </vue-feather>Add Provider
          </nuxt-link>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-body">
        <div class="tab-content" id="top-tabContent"> 
          <div v-for="(item, index) in tab" :key="index" :class="{ 'tab-pane': true, 'fade': !item.active, 'active show': item.active }" :id="item.id" role="tabpanel" :aria-labelledby="item.label">
            <div class="row">
              <div class="col-lg-4 col-md-6" v-for="(dataItem, dataIndex) in filteredData" :key="dataIndex">
                  <div class="project-box" @click="navigateToEdit(dataItem.credential_id)" @mouseover="onMouseOver" @mouseleave="onMouseLeave">
                    <span class="badge badge-primary" v-if="dataItem.provider_type==='M'">{{ dataItem.provider_type }}</span>
                      <h6>{{ dataItem.credential_name }}</h6>
                      <div class="d-flex mb-3"><img class="img-20 me-2 rounded-circle" :src="`/images/provider/${dataItem.provider_logo}`" alt="" data-original-title="" title="">
                          <div class="flex-grow-1 project-box-item">
                              <p>{{ dataItem.provider_company }}</p>
                          </div>
                      </div>
                      <p>{{ dataItem.provider_desc }}</p>
                      <div class="row details">
                          <div class="col-6" v-if="dataItem.access_key"><span>Access Key </span></div>
                          <div class="col-6 font-primary" v-if="dataItem.access_key">{{ mask(dataItem.access_key) }} </div>
                          <div class="col-6" v-if="dataItem.secret_key"> <span>Secret Access Key</span></div>
                          <div class="col-6 font-primary" v-if="dataItem.secret_key">{{ mask(dataItem.secret_key) }}</div>
                          <div class="col-6" v-if="dataItem.session_key"> <span>Session Key</span></div>
                          <div class="col-6 font-primary" v-if="dataItem.session_key">{{ mask(dataItem.session_key) }}</div>
                          <div class="col-6" v-if="dataItem.access_token"> <span>Access Token</span></div>
                          <div class="col-6 font-primary" v-if="dataItem.access_token">{{ mask(dataItem.access_token) }}</div>
                          <div class="col-6" v-if="dataItem.api_key"> <span>API Key</span></div>
                          <div class="col-6 font-primary" v-if="dataItem.api_key">{{ mask(dataItem.api_key) }}</div>                                                      
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
import { useProviderStore } from '@/store/provider';
import { mapState, mapActions } from 'pinia';

export default {
  name: 'ListProvider',
  data() {
    return {
      tab: [
        { type: 'all', name: 'All', active: true, icon: 'target', id: 'top-all', label: 'all-tab' },
        { type: 'M', name: 'Model', active: false, icon: 'cpu', id: 'top-model', label: 'model-tab' },
        { type: 'N', name: 'Not Model', active: false, icon: 'database', id: 'top-not-model', label: 'not-model-tab' }
      ],
      userId: '3fa85f64-5717-4562-b3fc-2c963f66afa6'
    };
  },
  computed: {
    ...mapState(useProviderStore, ['providers']),
    filteredData() {
      if (this.activeTab.type === 'all') return this.providers;
      return this.providers.filter(provider => provider.provider_type === this.activeTab.type);
    },
    activeTab() {
      return this.tab.find(t => t.active);
    }
  },
  methods: {
    ...mapActions(useProviderStore, ['fetchCredential']),
    active(item) {
      this.tab.forEach(a => (a.active = false));
      item.active = true;
    },
    mask(value) {
      if (value.length <= 3) return value;
      return value.slice(0, 3) + '*************';
    },
    navigateToEdit(credentialId) {
      // this.$router.push(`/provider/modify/${credentialId}`);
      this.$router.push({ path: '/provider/modify', query: { credentialId: credentialId } });
    },
    onMouseOver(event) {
      event.currentTarget.classList.add('hover');
    },
    onMouseLeave(event) {
      event.currentTarget.classList.remove('hover');
    }
  },
  async mounted() {
    await this.fetchCredential({ userId: this.userId });
  }
};
</script>

<style scoped>
.project-box {
  transition: transform 0.3s;
  cursor: pointer;
}
.project-box h6 {
    font-weight: bold;
}
.project-box.hover {
  transform: scale(1.05);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
</style>  