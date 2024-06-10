<template>
     <div class="col-sm-12 text-start">
                <div class="card">
                  <div class="card-header">
                    <h5>Advanced State</h5>
                  </div>
                  <div class="card-body btn-showcase">
                    <button class="btn btn-success sweet-12" type="button"  v-on:click="advanced_success_alert">Success</button>
                    <button class="btn btn-danger sweet-11" type="button" v-on:click="advanced_danger_alert">Danger</button>
                    <button class="btn btn-info sweet-13" type="button" v-on:click="advanced_info_alert">Information</button>
                    <button class="btn btn-warning sweet-10" type="button" v-on:click="advanced_warning_alert">Warning</button>
                  </div>
                </div>
              </div>
</template>
<script>
export default {
    methods:{

        advanced_success_alert:function(){
        this.$swal({
          text:'A wild Pikachu appeared! What do you want to do?',
          showCancelButton: true,
          showDenyButton: true,
          denyButtonText: 'run away!',
          confirmButtonText: 'Throw Pokéball!',
          confirmButtonColor: '#4466f2',
          cancelButtonText: 'Defeat',
          cancelButtonColor: '#4466f2',
          
        }).then((result)=>{
          if(result.value){
            this.$swal({
              title:'Gotcha!',
              text:'Pikachu was caught!',
              type:'success'
            });
          }
          else if(result.isDenied){
            this.$swal({
              text:'Go away Safely',
            })
          }
          else{
            this.$swal({
              text:'Pikachu fainted! You gained 500 XP!'
            });
          }
        });
        
      },
      advanced_danger_alert:function(){
        this.$swal({
          text:'Are you sure you want to do this?',
          showCancelButton: true,
          confirmButtonText: 'Aww yiss!',
          confirmButtonColor: '#4466f2',
          cancelButtonText: 'Oh noez!',
          cancelButtonColor: '#efefef',
          reverseButtons: true
        });
      },
      advanced_info_alert:function(){
        this.$swal({
          text:'Write something here:',
          input: 'text',
        }).then((result)=>{
          if(result.value){
            this.$swal({
              text:'You typed:'+result.value,
            });
          } else{
            this.$swal({
              text:'You typed:'+result.value,
            });
          }
        });
      },
      advanced_warning_alert:function(){
        this.$swal({
          text:'Are you sure you want to do this?',
          showCancelButton: true,
          confirmButtonText: 'Aww yiss!',
          confirmButtonColor: '#4466f2',
          cancelButtonText: 'Oh noez!',
          cancelButtonColor: '#efefef',
          reverseButtons: true
        });
      },
    }
}
</script>