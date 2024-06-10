<template>
     <div class="col-sm-12 col-md-6 text-start">
                <div class="card">
                  <div class="card-header">
                    <h5>Copy Portion From Paragraph</h5>
                  </div>
                  <div class="card-body">
                    <div class="clipboaard-container">
                      <p class="card-description">Copy Portion From Paragraph</p>
                      <h6 class="border rounded card-body f-w-300">Lorem ipsum <span class="bg-primary text-white p-1" id="highlighted_paragraph">dolor sit amet</span>, consectetur adipiscing elit,
                        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
                      </h6>
                      <div class="mt-3">
                        <button class="btn btn-primary btn-clipboard" type="button" @click="copy_highlighted_paragraph_input('highlighted_paragraph')" ><i class="fa fa-copy"></i> Copy highlighted text</button>
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

        }
    },
    methods:{
        copy_highlighted_paragraph_input(elementId){
			
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