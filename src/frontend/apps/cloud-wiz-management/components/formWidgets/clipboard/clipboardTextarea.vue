<template>
    <div class="col-sm-12 col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h5>Clipboard On Textarea</h5>
                  </div>
                  <div class="card-body">
                    <div class="clipboaard-container">
                      <p class="card-description">Cut/copy from textarea</p>
                      <textarea class="form-control" v-model="textarea" ref="textarea" rows="1" >Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has</textarea>
                      <div class="mt-3">
                        <button class="btn btn-primary btn-clipboard" type="button" @click="copy_textarea_input"><i class="fa fa-copy"></i> Copy</button>
                        <button class="btn btn-secondary btn-clipboard-cut" type="button" @click="cut_textarea_input"><i class="fa fa-cut"></i> Cut</button>
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
            textarea:'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has',
        }
    },
    methods:{
         copy_textarea_input(){
        this.$refs.textarea.select();
        document.execCommand('copy');
        alert('copied');
      },
      cut_textarea_input(){
        this.$refs.textarea.select();
        document.execCommand('cut');
        this.textarea = '';
        alert('cut');
      },
    }
}
</script>