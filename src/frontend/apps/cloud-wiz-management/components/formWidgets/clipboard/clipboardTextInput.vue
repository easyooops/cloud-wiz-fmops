<template>
    <div class="col-sm-12 col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h5>Clipboard On Text Input</h5>
                  </div>
                  <div class="card-body">
                    <div class="clipboaard-container">
                      <p class="card-description">Cut/copy from text input</p>
                      <input class="form-control" id="clipboardExample1" v-model="text_input" type="text" placeholder="type some text to copy / cut" ref="text">
                      <div class="mt-3">
                        <button class="btn btn-primary btn-clipboard me-1" @click="copy_text_input" type="button"  ><i class="fa fa-copy"></i> Copy</button>
                        <button class="btn btn-secondary btn-clipboard-cut " type="button"  @click="cut_text_input" ><i class="fa fa-cut"></i> Cut</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    data(){
        return{
            text_input:'',
        }
    },
     methods:{
      copy_text_input(){
        this.$refs.text.select();
        document.execCommand('copy');
        alert('copied');
      },
      cut_text_input(){
        this.$refs.text.select();
        document.execCommand('cut');
        this.text_input = '';
        alert('cut');
      },
     }
}
</script>