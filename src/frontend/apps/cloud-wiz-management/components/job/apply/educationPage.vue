<template>
  <h6 class="mb-0">Your Education</h6>
                     <form class="form theme-form">
                       <div class="row">
                         <div class="col-xl-6 xl-100">
                           <div class="form-group mb-3">
                             <label class="form-label" for="exampleFormControlInput5">College Name:<span class="font-danger">*</span></label>
                             <input class="form-control" id="exampleFormControlInput5" type="text" placeholder="Enter college name">
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
                             <label class="form-label">Degree Level:<span class="font-danger">*</span></label>
                             <select class="js-example-basic-single col-sm-12 job-select2 form-select job-select2">
                               <optgroup label="Choose a Option">
                                 <option value="student">Student</option>
                                 <option value="Bachelor">Bachelor</option>
                                 <option value="Master">Master</option>
                                 <option value="Associate">Associate</option>
                               </optgroup>
                             </select>
                           </div>
                         </div>
                         <div class="col-xl-6 xl-100">
                           <div class="form-group mb-3">
                             <label class="form-label" for="exampleFormControlInput6">Specialization:<span class="font-danger">*</span></label>
                             <input class="form-control" id="exampleFormControlInput6" type="email" placeholder="Enter specialization">
                           </div>
                         </div>
                       </div>
                     </form>
</template>