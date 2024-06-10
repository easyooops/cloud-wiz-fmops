<template>
     <div class="col-sm-12 col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h5>Clipboard On Paragraph</h5>
                  </div>
                  <div class="card-body">
                    <div class="clipboaard-container">
                      <p class="card-description">Copy from Paragraph</p>
                      <h6 class="border rounded card-body f-w-300" v-text="paragraph" id="paragraph">

                      </h6>
                      <div class="mt-3">
                        <button class="btn btn-primary btn-clipboard" type="button" @click="copy_paragraph_input('paragraph')"><i class="fa fa-copy"></i> Copy</button>
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
              paragraph:'Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        }
    },
    methods:{
         copy_paragraph_input(elementId){
			
        var aux = document.createElement('input');
        aux.setAttribute('value', document.getElementById(elementId).innerHTML);
        document.body.appendChild(aux);
        aux.select();
        document.execCommand('copy');
        document.body.removeChild(aux);
        alert('copied');
      },
    }
}
</script>