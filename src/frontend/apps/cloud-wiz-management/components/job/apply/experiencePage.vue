<template>
  <h6 class="mb-0">Your Experience</h6>
                     <form class="form theme-form">
                       <div class="row">
                         <div class="col-xl-6 xl-100">
                           <div class="form-group mb-3">
                             <label class="form-label" for="exampleFormControlInput7">Location:<span class="font-danger">*</span></label>
                             <input class="form-control" id="exampleFormControlInput7" type="text" placeholder="Enter Location">
                           </div>
                         </div>
                         <div class="col-xl-6 xl-100 xl-mt-job mb-3">
                           <label class="col-form-label text-end pt-0">Period:<span class="font-danger">*</span></label>
                           <div class="row">
                             <div class="col-sm-6">
                               <div class="input-group">
                                 <input class="datepicker-here form-control digits" type="text" data-language="en" placeholder="Start Date">
                               </div>
                             </div>
                             <div class="col-sm-6 xs-mt-period">
                               <div class="input-group">
                                 <input class="datepicker-here form-control digits" type="text" data-language="en" placeholder="End Date">
                               </div>
                             </div>
                           </div>
                         </div>
                         <div class="col-xl-6 xl-100">
                           <div class="form-group mb-3">
                             <label class="form-label">Position:<span class="font-danger">*</span></label>
                             <select class="js-example-basic-single col-sm-12 job-select2 form-select job-select2">
                               <optgroup label="Enter Position">
                                 <option value="position">Choose a option</option>
                                 <option value="Web designer">Web Designer</option>
                                 <option value="Graphic designer">Graphic Designer</option>
                                 <option value="UI designer">UI Designer</option>
                                 <option value="UI/UX designer">UI/UX Designer</option>
                               </optgroup>
                             </select>
                           </div>
                         </div>
                         <div class="col-xl-6 xl-100">
                           <div class="form-group mb-3">
                             <label class="form-label" for="exampleFormControlInput8">Company Name:<span class="font-danger">*</span></label>
                             <input class="form-control" id="exampleFormControlInput8" type="text" placeholder="Enter Company Name">
                           </div>
                         </div>
                       </div>
                     </form>
</template>