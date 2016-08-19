var createCategory = function() {
    var createApiUrl = 'api/create/';

    var $form = $('#create-category');
    var $submitBtn = $('.submit-button');
    var $serverSuccess = $('.server-success');
    var $serverFailure = $('.server-failure');

    var formData = {};

    function init() {
        $form.on('submit', submitFormEventHandler);
    }

    function submitFormEventHandler(event) {
        event.preventDefault();

        $serverSuccess.hide();
        $serverFailure.hide();

        setFormDisabledState(true);

        var ajaxOptions = {
            url: createApiUrl,
            type: 'POST',
            data: $form.serialize(),
            dataType: 'json'
        };

        $.ajax(ajaxOptions)
            .done(submitSuccessHandler)
            .fail(submitErrorHandler)
            .always(submitResponseHandler);
    }

    function submitSuccessHandler(response) {
        $serverSuccess.text(gettext('Category created successfully'));
        $serverSuccess.show();
    }

    function submitErrorHandler(response) {
        $serverFailure.text(gettext('Something went wrong. Maybe the category exists already?'));
        $serverFailure.show();
    }

    function submitResponseHandler(response) {
        setFormDisabledState(false);
    }

    function setFormDisabledState(isDisabled) {
        $submitBtn.attr('disabled', isDisabled);
    }

    return {
        init: init
    }
}();

$(document).ready(function() {
    createCategory.init();
});
