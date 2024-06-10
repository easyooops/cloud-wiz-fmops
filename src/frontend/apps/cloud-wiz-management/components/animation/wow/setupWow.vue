<template>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-primary rounded-pill me-2">1</span>Setup wow.js</h5><span>(You can link to another
                CSS animation library by changing wow.js settings)</span>
        </div>
        <div class="card-body">
            <div>
                <div class="line"><code><span>&lt;link rel="stylesheet" href="css/animate.css" &gt;</span></code></div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-primary rounded-pill me-2">2</span>Link and activate wow.js</h5>
        </div>
        <div class="card-body">
            <div>
                <div class="line">&lt; script
                    src="js/wow.min.js" &gt; &lt; /script &gt; <br />&lt; script &gt; <br /><code>  WOW.init();</code><br />&lt; /script &gt;
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-primary rounded-pill me-2">3</span>Make an element revealable</h5><span>(You can
                change this CSS class in the WOW settings to avoid name conflicts.)</span>
        </div>
        <div class="card-body">
            <h6 class="text-muted">Add the CSS class .wow to a HTML element: it will be invisible until the user scrolls to
                reveal it.</h6>
            <div>
                <div class="line">&lt; div class="wow" &gt; <br /><code>Content to Reveal Here</code><br />&lt; /div &gt;
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-primary rounded-pill me-2">4</span>Choose the animation style</h5><span>Pick an
                animation style in Animate.css , then add the CSS class to the HTML element</span>
        </div>
        <div class="card-body">
            <div>
                <div class="line">&lt; div class="wow
                    bounceInUp" &gt; <br /><code>Content to Reveal Here</code><br />&lt; /div &gt;</div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-success rounded-pill me-2">Extra</span>Advance Options</h5>
        </div>
        <div class="card-body">
            <div>
                <div class="line">
                    <p><strong>data-wow-duration: </strong>Change the animation duration<br><strong>data-wow-delay:
                        </strong>Delay before the animation starts<br><strong>data-wow-offset: </strong>Distance to start
                        the animation (related to the browser bottom)<br><strong>data-wow-iteration: </strong>Number of
                        times the animation is repeated<br></p>
                    <pre
                        class="mb-0">&lt;section class="wow slideInLeft" data-wow-duration="2s" data-wow-delay="5s"&gt;<br /> &lt;/section&gt;<br /> &lt;section class="wow slideInRight" data-wow-offset="10" data-wow-iteration="10"&gt;<br /> &lt;/section&gt;</pre>
                </div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header wow-title">
            <h5><span class="badge badge-danger rounded-pill me-2">Settings</span>Customize Settings</h5>
        </div>
        <div class="card-body">
            <div>
                <div class="line">
                    <p><strong>boxClass: </strong>Class name that reveals the hidden box when user scrolls.</p>
                    <p><strong>animateClass: </strong>Class name that triggers the CSS animations (’animated’ by default for
                        the animate.css library)</p>
                    <p><strong>offset: </strong>Define the distance between the bottom of browser viewport and the top of
                        hidden box.<br>When the user scrolls and reach this distance the hidden box is revealed.</p>
                    <p><strong>mobile: </strong>Turn on/off wow.js on mobile devices.</p>
                    <p><strong>live: </strong>consatantly check for new WOW elements on the page.</p>
                    <pre
                        class="mb-0">wow = new WOW(<br /> {<br /> boxClass: 'wow', // default<br /> animateClass: 'animated', // default<br /> offset: 0, // default<br /> mobile: true, // default<br /> live: true // default<br /> }<br /> )<br /> wow.init();</pre>
                </div>
            </div>
        </div>
    </div>
</template>