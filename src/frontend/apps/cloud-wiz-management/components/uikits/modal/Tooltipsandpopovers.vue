<template>
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modal title</h5>
                <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <h5>Popover in a modal</h5>
                <p>This <a class="btn btn-primary popover-test" href="#" role="button" title="popover"
                        data-bs-toggle="popover">button</a> triggers a popover on click.</p>
                <hr>
                <h5>Tooltips in a modal</h5>
                <p><a class="tooltip-test" href="#" title="Tooltip" data-bs-toggle="tooltip">This link</a> and <a
                        class="tooltip-test" href="#" title="Link" data-bs-toggle="tooltip">that link</a> have tooltips on
                    hover.</p>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                <button class="btn btn-primary" type="button">Save changes</button>
            </div>
        </div>
</div></template>