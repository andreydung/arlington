var Arlington = window.Arlington || {};

Arlington = (function ($) {

    'use strict';

    return {

        fitVidsJs: function () {
            $('body').fitVids();
        },

        init: function () {
            this.fitVidsJs();
        }
    };

}(window.jQuery));

jQuery(function () {
    'use strict';
    Arlington.init();
});