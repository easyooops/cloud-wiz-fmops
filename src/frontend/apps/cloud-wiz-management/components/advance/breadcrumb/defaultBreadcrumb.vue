<template>
  <div class="col-md-6">
    <div class="card">
      <div class="card-header">
        <h5>Default bootstrap breadcrumb</h5><span>use class <code>.breadcrumb to ol</code></span>
      </div>
      <div class="card-body">
        <ol class="breadcrumb p-t-0 p-l-0">
          <li class="breadcrumb-item active">Home</li>
        </ol>
        <ol class="breadcrumb p-l-0">
          <li class="breadcrumb-item"><a href="javascript:void(0)">Home</a></li>
          <li class="breadcrumb-item active">Library</li>
        </ol>
        <ol class="breadcrumb p-l-0">
          <li class="breadcrumb-item"><a href="javascript:void(0)">Home</a></li>
          <li class="breadcrumb-item"><a href="javascript:void(0)">Library</a></li>
          <li class="breadcrumb-item active">Data</li>
        </ol>
        <ol class="breadcrumb m-b-0 p-b-0 p-l-0">
          <li class="breadcrumb-item"><a href="javascript:void(0)"><i class="fa fa-home"></i></a></li>
          <li class="breadcrumb-item">Library</li>
          <li class="breadcrumb-item active">Data</li>
        </ol>
      </div>
    </div>
  </div>
</template>