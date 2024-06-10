<template>
    <breadCrumbs title="Dark Layout" main="Page Layout" title1="Dark Layout" />


    <div class="container-fluid">
        <div class="row">
            <div class="col-sm-12">
                <div class="card alert alert-primary" role="alert">
                    <h3>Tip!</h3>
                    <p>Add the class="dark-only" to the body tag to get this layout.</p>
                </div>
            </div>
            <div class="col-sm-12">
                <div class="card">
                    <div class="card-header">
                        <h3>Title</h3>
                        <settingPage />
                    </div>
                    <div class="card-body"><span>Start Here</span>
                        <div class="code-box-copy">
                            <button class="code-box-copy__btn btn-clipboard" data-clipboard-target="#example-head"
                                title="Copy"><i class="icofont icofont-copy-alt"></i></button>
                            <pre><code class="language-html" id="example-head">&lt;!-- Cod Box Copy begin --&gt;
        &lt;div class=&quot;card-body&quot;&gt;
        &lt;span&gt;Start Here&lt;/span&gt;
        &lt;/div&gt;    
        &lt;!-- Cod Box Copy end --&gt;</code></pre>
                        </div>
                    </div>
                    <div class="card-footer">
                        <h3 class="mb-0">Card Footer</h3>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {
    useLayoutStore
} from '~~/store/layout'

export default {
    name: "indexDarklayout",

    mounted() {
        useLayoutStore().setLayout({
            class: 'dark-only'
        })

    },
    unmounted() {
        useLayoutStore().setLayout({
            class: ''
        })

    }
}
</script>
