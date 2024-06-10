<template>
  <div class="tab-pane fade" v-bind:class="(activeclass === 'pills_created') ? 'active show' : ''" id="pills-created"
    role="tabpanel" aria-labelledby="pills-created-tab">
    <div class="card mb-0">
      <div class="card-header d-flex">
        <h6 class="f-w-600 mb-0">Created by me</h6>
        <ul>
          <li><a class="grid-bookmark-view" href="javascript:void(0);"><vue-feather type="grid"
                @click="liststyle = !liststyle"></vue-feather></a></li>
          <li><a class="list-layout-view" href="javascript:void(0);"><vue-feather type="list"
                @click="liststyle = !liststyle"></vue-feather></a></li>
        </ul>
      </div>
      <div class="card-body pb-0">
        <div class="details-bookmark text-center" v-bind:class="{ 'list-bookmark': liststyle }">
          <div class="row" id="bookmarkData">
            <div class="col-xl-3 col-lg-6 col-md-4 col-sm-6 xl-50 box-col-6" v-for="(item, index) in bookmark"
              :key="index">
              <div class="card card-with-border bookmark-card o-hidden">
                <div class="details-website">
                  <img class="img-fluid" :src='getImgUrl(item.image)' alt="">
                  <div class="favourite-icon favourite_0" :class="(getActive(item.id)) ? 'favourite' : ''"
                    @click="setFavourite(item)"><a href="javascript:void(0)"><i class="fa fa-star"></i></a></div>
                  <div class="desciption-data">
                    <div class="title-bookmark">
                      <h6 class="title_0">{{ item.title }}</h6>
                      <p class="weburl_0">{{ item.website_url }}</p>
                      <div class="hover-block">
                        <ul>
                          <editBookmark />
                          <li><a href="#"><vue-feather type="link"></vue-feather></a></li>
                          <li><a href="#"><vue-feather type="share-2"></vue-feather></a></li>
                          <li><a><vue-feather type="trash-2" v-on:click="basic_warning_alert(index)"></vue-feather></a>
                          </li>
                          <li class="pull-right text-end"><vue-feather type="tag"></vue-feather></li>
                        </ul>
                      </div>
                      <div class="content-general">
                        <p class="desc_0"> {{ item.desc }}</p><span class="collection_0">General</span>
                      </div>
                    </div>
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
import editBookmark from "./editBookmark.vue"
import { mapState } from 'pinia';
import { useCommonStore } from '~~/store/common';
import bookmarkMixin from "@/mixin/commen/bookmarkMixin"
export default {
  components: { editBookmark },
  mixins: [bookmarkMixin],
  data() {
    return {
      liststyle: false,
      data: [],
      favourite: useCommonStore().favourite,
      filtered: false,
    };
  },
  computed: {
    ...mapState(useCommonStore, {
      bookmark: 'bookmark',
    }),
    activeclass() {
      return useCommonStore().activeclass1
    }
  },

}
</script>