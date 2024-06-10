<template>
    <div class="card">
        <div class="card-header">
            <h3>How to Use Scroll Reveal(Customize options according to requirements)</h3><span>Add
                <code>.reveal</code> class to any tag for Archive animation like this</span>
        </div>
        <div class="card-body">
            <div><span class="comment">// The Below Function is example of how to initlize reveal</span>
                <div class="line"><span class="text-danger">if (Modernizr.csstransforms3d)</span><span
                        class="text-success">{</span><br> window.sr = ScrollReveal();<br> sr.reveal('.reveal',
                    {<br> duration: 800,<br> delay: 400,<br> reset: true,<br> easing: 'linear',<br> scale: 1<br>
                    });<br><span class="text-success"> }</span></div>
            </div>
        </div>
    </div>
    <div class="card">
        <div class="card-header">
            <h3>Scroll Reveal Settings options</h3>
        </div>
        <div class="card-body">
            <div class="p-b-15"><span class="comment">// 'bottom', 'left', 'top', 'right'</span>
                <div class="line">origin: <span class="text-danger">'bottom',</span></div>
            </div>
            <div class="p-b-15"><span class="comment">// Can be any valid CSS distance, e.g. '5rem', '10%',
                    '20vw', etc.</span>
                <div class="line">distance: <span class="text-danger">'20px',</span></div>
            </div>
            <div class="p-b-15"><span class="comment">// Time in milliseconds.</span>
                <div class="line">duration: <span class="text-danger">500,</span> delay: <span class="text-danger">0,</span>
                </div>
            </div>
            <div class="p-b-15"><span class="comment">// Starting angles in degrees, will transition from these
                    values to 0 in all axes.</span>
                <div class="line">rotate: { x: <span class="text-danger">0</span>, y: <span class="text-danger">0</span>, z:
                    <span class="text-danger">0</span> },</div>
            </div>
            <div class="p-b-15"><span class="comment">// Starting opacity value, before transitioning to the
                    computed opacity.</span>
                <div class="line">opacity: <span class="text-danger">0</span>,</div>
            </div>
            <div class="p-b-15"><span class="comment">// Starting scale value, will transition from this value
                    to 1</span>
                <div class="line">scale: <span class="text-danger"> 0.9</span>,</div>
            </div>
            <div class="p-b-15"><span class="comment">// Accepts any valid CSS easing, e.g. 'ease',
                    'ease-in-out', 'linear', etc.</span>
                <div class="line">easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)',</div>
            </div>
            <div class="p-b-15"><span class="comment">// is the default reveal container. You can pass
                    either:<br> // DOM Node, e.g. document.querySelector('.fooContainer')<br> // Selector, e.g.
                    '.fooContainer'</span>
                <div class="line">easing: 'cubic-bezier(0.6, 0.2, 0.1, 1)',</div>
            </div>
            <div class="p-b-15"><span class="comment">// true/false to control reveal animations on
                    mobile.</span>
                <div class="line">mobile: true,</div>
            </div>
            <div class="p-b-15"><span class="comment">// true: reveals occur every time elements become
                    visible<br> // false: reveals occur once as elements become visible</span>
                <div class="line">reset: false,</div>
            </div>
            <div class="p-b-15"><span class="comment">// 'always' — delay for all reveal animations<br> //
                    'once' — delay only the first time reveals occur<br> // 'onload' - delay only for animations
                    triggered by first load</span>
                <div class="line">useDelay: 'always',</div>
            </div>
            <div class="p-b-15"><span class="comment">// Change when an element is considered in the viewport.
                    The default value<br> // of 0.20 means 20% of an element must be visible for its reveal to
                    occur.</span>
                <div class="line">viewFactor: 0.2,</div>
            </div>
            <div class="p-b-15"><span class="comment">// Pixel values that alter the container boundaries.<br>
                    // e.g. Set `{ top: 48 }`, if you have a 48px tall fixed toolbar.<br> // --<br> // Visual
                    Aid: https://scrollrevealjs.org/assets/viewoffset.png</span>
                <div class="line">viewOffset: { top: 0, right: 0, bottom: 0, left: 0 },</div>
            </div>
            <div class="p-b-15"><span class="comment">// Callbacks that fire for each triggered element reveal,
                    and reset.</span>
                <div class="line">beforeReveal: <span class="text-danger">function</span> (domEl) {},<br>
                    beforeReset: <span class="text-danger">function</span> (domEl) {},</div>
            </div>
            <div><span class="comment">// Callbacks that fire for each completed element reveal, and
                    reset.</span>
                <div class="line">afterReveal: <span class="text-danger">function</span> (domEl) {},<br>
                    afterReset: <span class="text-danger">function</span> (domEl) {}</div>
            </div>
        </div>
    </div>
</template>