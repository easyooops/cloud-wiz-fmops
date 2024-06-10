<template>
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">New message</h5>
                <button class="btn-close" type="button" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                    <div class="mb-3">
                        <label class="col-form-label" for="recipient-name">Recipient:</label>
                        <input class="form-control" id="recipient-name" type="text" value="@Mat">
                    </div>
                    <div class="mb-3">
                        <label class="col-form-label" for="message-text">Message:</label>
                        <textarea class="form-control"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button class="btn btn-secondary" type="button" data-bs-dismiss="modal">Close</button>
                <button class="btn btn-primary" type="button">Send message</button>
            </div>
        </div>
    </div>
</template>