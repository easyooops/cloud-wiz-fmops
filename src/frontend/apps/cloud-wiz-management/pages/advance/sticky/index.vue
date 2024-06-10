<template>
    <Breadcrumbs title="Sticky" main="Bonus UI"  />
<div class="container-fluid">
    <div class="row sticky-header-main">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h3>Sticky Note <a class="btn btn-primary pull-right m-l-10" id="add_new" href="javascript:;" v-on:click="addNewSticky">Add New Note</a></h3>
          </div>
          <div class="card-body">
            <div class="sticky-note" id="board">
                <div class="note ui-draggable ui-draggable-handle" style="" v-for="(n) in sticky_notes" :key="'notes'+n.id">
                    <a href="javascript:;" v-on:click="removeSticky(n.id)" class="button remove">X</a>
                    <div class="note_cnt" >
                      <textarea class="title" placeholder="Enter note title" style="height: 64px;" v-text="n.title"></textarea>
                      <textarea class="cnt" placeholder="Enter note description here" style="height: 200px;" v-text="n.description"></textarea>
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
export default {
    data() {
        return {
            sticky_notes: [], 
            count:0
        };
    },
    mounted() {
        this.sticky_notes.push({
          id:1,
            title: '',
            description: ''
        });
        this.count++
    },
    methods: {
        addNewSticky: function () {
          this.count++
            this.sticky_notes.push({
              id: this.count,
                title: '',
                description: ''
            });
        },
        removeSticky: function (id) {
            this.sticky_notes.splice(this.sticky_notes.findIndex(item=>item.id == id),1);
        }
    }
}
</script>
