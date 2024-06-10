<template>
  <div class="col-xl-12">
    <div class="card">
      <div class="card-header">
        <h3>Pagination with active and disabled</h3>
      </div>
      <div class="card-body">
        <nav aria-label="...">
          <ul class="pagination pagination-primary">
            <li class="page-item disabled"><a class="page-link" href="javascript:void(0)" tabindex="-1">Previous</a></li>
            <li class="page-item"><a class="page-link" href="javascript:void(0)">1</a></li>
            <li class="page-item active"><a class="page-link" href="javascript:void(0)">2 <span class="sr-only">(current)</span></a></li>
            <li class="page-item"><a class="page-link" href="javascript:void(0)">3</a></li>
            <li class="page-item"><a class="page-link" href="javascript:void(0)">Next</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  </template>