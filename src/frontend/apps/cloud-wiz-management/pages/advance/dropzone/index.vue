<template>
  <Breadcrumbs title="Creative Card" main="Card" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h3>Single File Upload</h3>
          </div>
          <div class="card-body">
            <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true" />
          </div>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h3>Multi File Upload</h3>
          </div>
          <div class="card-body">
            <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true"
              :multipleUpload="true" :parallelUpload="2" />
          </div>
        </div>
      </div>
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>File Type Validation</h5>
          </div>
          <div class="card-body">
            <DropZone :maxFileSize="Number(60000000)" url="http://localhost:8080" :uploadOnDrop="true"
              :multipleUpload="true" :parallelUpload="2" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>