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
                <div class="col-lg-4 col-md-6" v-for="(dataItem, dataIndex) in data" :key="dataIndex">
                    <div class="project-box"><span class="badge" :class="dataItem.class">{{ dataItem.badge }}</span>
                        <h6>{{ dataItem.title }}</h6>
                        <div class="d-flex mb-3"><img class="img-20 me-2 rounded-circle" :src="dataItem.img" alt=""
                                data-original-title="" title="">
                            <div class="flex-grow-1 project-box-item">
                                <p>{{ dataItem.sites }}</p>
                            </div>
                        </div>
                        <p>{{ dataItem.desc }}</p>
                        <div class="row details">
                            <div class="col-6"><span>Created </span></div>
                            <div class="col-6 font-primary">{{ dataItem.created }} </div>
                            <div class="col-6"> <span>Updated</span></div>
                            <div class="col-6 font-primary">{{ dataItem.updated }}</div>
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
  import { All, Model, Storage } from '@/data/provider/data';
  
  export default {
    name: 'providerHeader',
    data() {
      return {
        tab: [
          {
            type: "all",
            name: "All",
            active: true,
            icon: "target",
            id: 'top-all',
            label: 'all-tab'
          },
          {
            type: 'M',
            name: "Model",
            active: false,
            icon: "cpu",
            id: 'top-model',
            label: 'model-tab'
          },
          {
            type: 'N',
            name: "Not Model",
            active: false,
            icon: "database",
            id: 'top-not-model',
            label: 'not-model-tab'
          }
        ],
        data: All,
        modelData: Model,
        storageData: Storage
      }
    },
    methods: {
      active(item) {
        if (!item.active) {
          this.tab.forEach(a => {
            a.active = false;
          })
        }
        item.active = !item.active;
        if (item.type === 'all') {
          this.data = All;
        } else if (item.type === 'M') {
          this.data = Model;
        } else if (item.type === 'N') {
          this.data = Storage;
        }
      }
    }
  }
  </script>
  