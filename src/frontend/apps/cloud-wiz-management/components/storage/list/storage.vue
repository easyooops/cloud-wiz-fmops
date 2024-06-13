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
            <nuxt-link class="btn btn-primary" to="/storage/create">
              <vue-feather class="me-1" type="plus-square"> </vue-feather>Add Storage
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
                    <div class="project-box" @click="navigateToEdit(dataItem.store_id, dataItem.store_name)" @mouseover="onMouseOver" @mouseleave="onMouseLeave">
                      <span class="badge badge-primary">Private</span>
                        <h6>{{ dataItem.store_name }}</h6>
                        <div class="d-flex mb-3"><img class="img-20 me-2 rounded-circle" :src="`/images/provider/aws.png`" alt="" data-original-title="" title="">
                            <div class="flex-grow-1 project-item-detail">
                                <p>Amazon S3</p>
                            </div>
                        </div>
                        <p>{{ dataItem.description }}</p>
                        <div class="row details">
                            <div class="col-6"><span>Create Date</span></div>
                            <div class="col-6 font-primary">{{ dataItem.creator_id }} </div>
                            <div class="col-6"> <span>Volume Size</span></div>
                            <div class="col-6 font-primary">{{ formatFileSize(dataItem.total_size) }}</div>
                            <div class="col-6"> <span>File Count</span></div>
                            <div class="col-6 font-primary">{{ dataItem.file_count }}</div>                                                  
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
import { useStorageStore } from '@/store/storage';
import { mapState, mapActions } from 'pinia';

export default {
    name: 'ListStorage',
    data() {
        return {
        tab: [
            { type: 'all', name: 'All', active: true, icon: 'target', id: 'top-all', label: 'all-tab' }
        ],
        userId: '3fa85f64-5717-4562-b3fc-2c963f66afa6'
        };
    },
    computed: {
        ...mapState(useStorageStore, ['storages']),
        filteredData() {
            if (this.activeTab.type === 'all') return this.storages;
        },
        activeTab() {
            return this.tab.find(t => t.active);
        }
    },
    methods: {
        ...mapActions(useStorageStore, ['fetchAllStorages']),
        active(item) {
            this.tab.forEach(a => (a.active = false));
            item.active = true;
        },
        navigateToEdit(storeId, storeName) {
            this.$router.push({ path: '/storage/modify', query: { storeId: storeId, storeName: storeName } });
        },   
        formatFileSize(sizeInBytes) {
            if (sizeInBytes < 1024) {
                return sizeInBytes.toFixed(1) + ' B';
            } else if (sizeInBytes < 1024 * 1024) {
                return (sizeInBytes / 1024).toFixed(1) + ' KB';
            } else {
                return (sizeInBytes / (1024 * 1024)).toFixed(1) + ' MB';
            }
        }, 
        onMouseOver(event) {
            event.currentTarget.classList.add('hover');
        },
        onMouseLeave(event) {
            event.currentTarget.classList.remove('hover');
        }
    },
    async mounted() {
        await this.fetchAllStorages({ userId: this.userId });
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