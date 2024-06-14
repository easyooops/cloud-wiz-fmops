<template>
    <div class="card mb-0">
        <div class="chat">
            <div class="card-header d-flex">
                <div class="about">
                    <ul>
                        <li class="list-inline-item"><i class="fa fa-chain"></i></li>
                        <li class="list-inline-item"><h5>Engineering</h5></li>
                    </ul>
                </div>
                <ul class="list-inline float-start float-sm-end chat-menu-icons">
                    <li class="list-inline-item">
                        <a href="#"><i class="fa fa-code"></i></a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#"><i class="fa fa-save"></i></a>
                    </li>
                    <li class="list-inline-item">
                        <a href="#"><i class="fa fa-list"></i></a>
                    </li>
                </ul>      
            </div>
        </div>

        <div class="card-body p-0">
            <div class="row list-persons" id="addcon">
                <div class="col-xl-3 xl-50 col-md-5">
                    <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
                        <a class="contact-tab-0 nav-link" :class="this.activeTab == item.activeTab ? 'active show' : ''"
                            id="v-pills-user-tab" data-bs-toggle="pill" @click="activeDiv(item.activeTab)"
                            href="#v-pills-user" role="tab" aria-controls="v-pills-user" aria-selected="true"
                            v-for="(item, index) in menu" :key="index">
                            <div class="media">
                                <li class="list-inline-item"><i :class="item.class"></i></li>
                                <div class="media-body">
                                    <h6> <span class="first_name_0">{{ item.menu }}</span></h6>
                                    <p class="email_add_0">{{ item.description }}</p>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
                <div class="col-xl-9 xl-50 col-md-7">
                    <div class="tab-content" id="v-pills-tabContent" :style="!this.display ? { display: 'none' } : ''">
                        <div class="tab-pane contact-tab-0 tab-content-child fade show"
                            :class="item.activeTab === this.activeTab ? 'active' : ''" id="v-pills-user" role="tabpanel"
                            aria-labelledby="v-pills-user-tab" v-for="(item, index) in menu" :key="index">

                            <div class="card-body" v-if="'0'==this.activeTab">
                                <div class="form theme-form">
                                    <div class="card">
                                        <div class="card-body">
                                            <div class="mb-3">
                                                <label for="agentName">Agent Name *</label>
                                                <input v-model="agentName" class="form-control" type="text" id="agentName" placeholder="Agent Name *" required>
                                            </div>
                                            <div class="mb-3">
                                                <label for="agentDescription">Agent Description</label>
                                                <input v-model="agentDescription" class="form-control" type="text" id="agentDescription" placeholder="Agent Description">
                                            </div>
                                        </div>
                                    </div>                                    

                                    <div class="card">
                                        <div class="card-body">                                    
                                            <div class="mb-3">
                                                <div class="col-form-label">Foundation Model *</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">OpenAI</option>
                                                    <option value="opt3">Anthropic</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div> 

                                    <div class="card">
                                        <div class="card-body">
                                            <div class="form-group row mb-5">
                                                <label class="col-md-2 col-form-label sm-left-text" for="u-range-01">Temperature *</label>
                                                <div class="col-md-9">
                                                    <VueSlider v-model="one.value" :data="one.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                                                </div>
                                            </div>
                                            <div class="form-group row mb-5">
                                                <label class="col-md-2 col-form-label sm-left-text" for="u-range-02">Top P *</label>
                                                <div class="col-md-9">
                                                    <VueSlider v-model="one.value" :data="one.data" :marks="true" :tooltip="'always'" :tooltip-placement="'top'" ></VueSlider>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
 
                                    <div class="card">
                                        <div class="card-body"> 
                                            <div class="mb-3">
                                                <fieldset>
                                                    <label class="col-md-2 col-form-label sm-left-text" for="agentDescription">Request Token</label>
                                                    <div class="input-group col-md-9">
                                                        <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num1--" ><i class="fa fa-minus"></i></button>
                                                        <input class="touchspin form-control" type="text" v-model="num1">
                                                        <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num1++" ><i class="fa fa-plus"></i></button>
                                                    </div>
                                                </fieldset>
                                            </div>
                                            <div class="mb-3">
                                                <label for="agentDescription">Response Token</label>
                                                <fieldset>
                                                    <div class="input-group">
                                                        <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num1--" ><i class="fa fa-minus"></i></button>
                                                        <input class="touchspin form-control" type="text" v-model="num1">
                                                        <button type="button" class="btn btn-primary btn-square bootstrap-touchspin-down" @click="num1++" ><i class="fa fa-plus"></i></button>
                                                    </div>
                                                </fieldset>
                                            </div>
                                        </div>
                                    </div>
                                                                          
                                </div>
                            </div>

                            <!-- Embedding -->
                            <div class="card-body" v-if="'1'==item.activeTab">
                                <div class="form theme-form">

                                    <div class="card">
                                        <div class="card-body">  
                                            <div class="mb-3">
                                                <div class="col-form-label">Embedding Model</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">OpenAI</option>
                                                    <option value="opt2">Anthropic</option>
                                                    <option value="opt3">Titan</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>

                                    <div class="card">
                                        <div class="card-body">   
                                            <div class="mb-3">
                                                <div class="col-form-label">Provider</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">Amazon S3</option>
                                                    <option value="opt2">GIT</option>
                                                    <option value="opt3">Notion</option>
                                                    <option value="opt4">Google Drive</option>
                                                </select>
                                            </div>
                                            <div class="mb-3">
                                                <div class="col-form-label">Storage</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">Default Storage</option>
                                                    <option value="opt2">Private Storage</option>
                                                </select>
                                            </div>                                            
                                        </div>
                                    </div>                                     
                                    
                                    <div class="card">
                                        <div class="card-body">   
                                            <div class="mb-3">
                                                <div class="col-form-label">Vector DB</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">FAISS</option>
                                                    <option value="opt2">ChromaDB</option>
                                                    <option value="opt3">Pincone</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div> 
                                
                                </div>
                            </div>
                            
                            <!-- Processing -->
                            <div class="card-body" v-if="'2'==item.activeTab">
                                <div class="form theme-form">

                                    <div class="card">
                                        <div class="card-body">     
                                            <div class="mb-3">
                                                <div class="col-form-label">Pre-Processing</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">Select One Value Only</option>
                                                    <option value="opt2">task I</option>
                                                    <option value="opt3">task II</option>
                                                    <option value="opt3">template I</option>
                                                </select>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="card">
                                        <div class="card-body">    
                                            <div class="mb-3">
                                                <div class="col-form-label">Post-Processing</div>
                                                <select class="form-select form-control-primary-fill" name="select">
                                                    <option value="opt1">Select One Value Only</option>
                                                    <option value="opt2">task I</option>
                                                    <option value="opt3">task II</option>
                                                    <option value="opt3">template I</option>
                                                </select>
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
import { useContactStore } from '~~/store/contact'
export default {
    name: 'setup',
    components: {
    },
    data() {
        return {
            num1:5000,
            one:{
                value:0.7,
                data:[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
            },    
            agentName: '',
            agentDescription: '',
            selectedProvider: '',                    
            data: {
                "data": [
                        {
                            "activeTab": "0",
                            "class": "fa fa-code-fork",
                            "menu": "Foundation Model *",
                            "description" : "Language Models (LLMs) serve as the foundation for chat systems, understanding and generating human-like text."
                        },
                        {
                            "activeTab": "1",
                            "class": "fa fa-database",
                            "menu": "Embedding",
                            "description" : "Embeddings capture semantic meaning of text for efficient retrieval in retrieval-augmented generation (RAG) models."
                        },
                        {
                            "activeTab": "2",
                            "class": "fa fa-cogs",
                            "menu": "Processing",
                            "description" : "Processing involves preparing input data for models (preprocessing) and handling model outputs (postprocessing) for effective communication or analysis."
                        }
                    ]
                },
            url: null,
            lastModified: null
        }
    },
    computed: {
        display() {
            return useContactStore().display
        },
        activeTab() {
            return useContactStore().activeTab
        },
        selectedUser() {
            return useContactStore().selectedUser
        },
        menu() {
            return this.data.data
        }
    },
    watch:{
      num1:function(newValue){
        if(newValue >= 5000) {
          this.num1 = 5000;
        } else if(newValue <= 0) {
          this.num1 = 0;
        }
      },
    },    
    methods: {
        selectProvider(provider) {
            this.selectedProvider = provider;
        },        
        readURL(e, item) {
            var files = e.target.files[0];
            this.url = URL.createObjectURL(files)
            item.imgUrl = this.url
        },
        activeDiv(item) {
            useContactStore().active(item)
            // this.activeTab = tab;
        },
        printContact(item) {
            useContactStore().print(item)
        },
        getImgUrl(path) {
            return ('/images/' + path)
        },
        editContact() {
            useContactStore().change()

        },
        deleteContact: function (items) {
            this.$swal({
                icon: 'warning', title: "Are you sure?",
                text: 'Once deleted, you will not be able to recover this imaginary file!',
                showCancelButton: true, confirmButtonText: 'Ok', confirmButtonColor: '#e64942',
                cancelButtonText: 'Cancel', cancelButtonColor: '#efefef',
            }).then((result) => {
                if (result.value) {
                    this.menu.splice(items, 1)
                    useContactStore().active(this.menu[items].activeTab)
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
        },
    }
}
</script>

<style scoped>
.fa { font: normal normal normal 30px / 1 FontAwesome; }
.fa-minus { font: normal normal normal 10px / 1 FontAwesome; }
.fa-plus { font: normal normal normal 10px / 1 FontAwesome; }
.product-name {
    margin-left: 10px;
}
.prooduct-details-box {
    cursor: pointer;
    padding: 10px;
}

.media.selected {
    border: 2px solid #007bff;
    background-color: #e7f1ff;
}
</style>