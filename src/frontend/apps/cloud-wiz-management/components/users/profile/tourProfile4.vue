<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="profile-img-style">
        <div class="row g-2">
          <div class="col-sm-8">
            <div class="media"><img class="img-thumbnail rounded-circle me-3" src="/images/user/7.jpg"
                alt="Generic placeholder image">
              <div class="media-body align-self-center">
                <h5 class="mt-0 user-name">JOHAN DIO</h5>
              </div>
            </div>
          </div>
          <div class="col-sm-4 align-self-center">
            <div class="float-sm-end"><small>10 Hours ago</small></div>
          </div>
        </div>
        <hr>
        <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin
          literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney
          College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and
          going through the cites of the word in classical literature, discovered the undoubtable source .Contrary to
          popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature
          from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in
          Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going
          through the cites of the word in classical literature, discovered the undoubtable source</p>
        <div class="like-comment mt-4">
          <ul class="list-inline">
            <li class="list-inline-item border-right pe-3">
              <label class="m-0"><a href="#"><i class="fa fa-heart"></i></a>  Like</label><span class="ms-2 counter">
                <number class="bold counter" ref="number1" :from="0" :to="2659" :duration="5" :delay="0"
                  easing="Power1.easeOut" />
              </span>
            </li>
            <li class="list-inline-item ms-2">
            <label class="m-0"><a href="#"><i class="fa fa-comment"></i></a>  Comment</label><span class="ms-2 counter">
              <number class="bold counter" ref="number1" :from="0" :to="569" :duration="5" :delay="0"
                easing="Power1.easeOut" />
            </span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div></template>