<template>
    <div class="customizer-header">
      <Teleport to="body">
        <div class="modal fade modal-bookmark" id="agent-modal" tabindex="-1" role="dialog"
          aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-md" role="document">
            <div class="modal-content">
              <header id="modal-customizer___BV_modal_header_" class="modal-header">
                <h5 id="modal-customizer___BV_modal_title_" class="modal-title">Agent CURL</h5><button type="button"
                  aria-label="Close" data-bs-dismiss="modal" class="close">×</button>
              </header>
              <div class="modal-body">
                <div class="config-popup">
                  <p>
                    To replace our design with your desired theme. Please do
                    configuration as mention
                  </p>
                  <div>
                    <pre>
                        <code>
                        <textarea :value="data" ref="layout" rows="1" v-bind:style="styleObject"/>
curl http://localhost:3000/api/v1/agent/0b7a2040-2619-4f1a-b11b-4bbdacab0d01 \
-X POST \
-d '{"question": "Hey, how are you?"}' \
-H "Content-Type: application/json"
                        </code>
                    </pre>
                  </div>
                  <button class="btn btn-primary mt-2" @click="copyText()">
                    Copy
                  </button>
                </div>
              </div>
              <footer id="modal-customizer___BV_modal_footer_" class="modal-footer">
                <!-- <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button> -->
                <button type="button" class="btn btn-primary" data-bs-dismiss="modal">OK</button></footer>
            </div>
          </div>
        </div>
      </Teleport>
    </div>
  </template>
  
  <script>
  import { mapState } from 'pinia';
  import { useLayoutStore } from '~~/store/layout';
  import { useMenuStore } from '~~/store/menu';
  
  export default {
    name: 'CustomizerConfiguration',
    data() {
      return {
        styleObject: {
          position: 'fixed',
          left: '0',
          top: '0',
          opacity: '0',
        },
      };
    },
    computed: {
      ...mapState(useMenuStore, {
        customizer: 'customizer',
      }),
      ...mapState(useLayoutStore, {
  
        layout: 'layout',
      }),
      data() {
        return `curl http://localhost:3000/api/v1/agent/0b7a2040-2619-4f1a-b11b-4bbdacab0d01 \
            -X POST \
            -d '{"question": "Hey, how are you?"}' \
            -H "Content-Type: application/json"`
      }
    },
    methods: {
      closecustomizer() {
        useMenuStore().customizer = ''
      },
      copyText() {
        this.$refs.layout.select();
        document.execCommand('copy');
        this.$toasted.show('Code Copied to clipboard', {
          theme: 'outline',
          position: 'top-right',
          type: 'default',
          duration: 2000,
        });
      },
    },
  };
  </script>
  