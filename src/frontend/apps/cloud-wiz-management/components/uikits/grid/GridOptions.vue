<template>
    <div class="col-sm-12">
        <div class="card">
            <div class="card-header">
                <h5>Grid Options</h5><span>Bootstrap grid allows building an equal height flexbile blocks easily</span>
            </div>
            <div class="card-body">
                <p>While Bootstrap uses <code>em </code>or <code>rem </code>for defining most sizes, <code>px</code> are
                    used for grid breakpoints and container widths. This is because the viewport width is in pixels and does
                    not change with the <a href="#">font size</a>.</p>
                <div class="table-responsive">
                    <table class="table table-bordered table-striped">
                        <thead>
                            <tr>
                                <th></th>
                                <th class="text-center">Extra small<br><small>&lt;576px</small></th>
                                <th class="text-center">Small<br><small>≥576px</small></th>
                                <th class="text-center">Medium<br><small>≥768px</small></th>
                                <th class="text-center">Large<br><small>≥992px</small></th>
                                <th class="text-center">Extra large<br><small>≥1200px</small></th>
                                <th class="text-center">Extra extra large<br><small class="digits">≥1400px</small></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th class="text-nowrap" scope="row">Grid behavior</th>
                                <td>Horizontal at all times</td>
                                <td colspan="5">Collapsed to start, horizontal above breakpoints</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Max container width</th>
                                <td>None (auto)</td>
                                <td>540px</td>
                                <td>720px</td>
                                <td>960px</td>
                                <td>1140px</td>
                                <td>1320px</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Class prefix</th>
                                <td><code>.col-</code></td>
                                <td><code>.col-sm-</code></td>
                                <td><code>.col-md-</code></td>
                                <td><code>.col-lg-</code></td>
                                <td><code>.col-xl-</code></td>
                                <td><code>.col-xxl-</code></td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row"># of columns</th>
                                <td colspan="6">12</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Gutter width</th>
                                <td colspan="6">1.5rem (.75rem on left and right)</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Nestable</th>
                                <td colspan="6">Yes</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Offsets</th>
                                <td colspan="6">Yes</td>
                            </tr>
                            <tr>
                                <th class="text-nowrap" scope="row">Column ordering</th>
                                <td colspan="6">Yes</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>
    