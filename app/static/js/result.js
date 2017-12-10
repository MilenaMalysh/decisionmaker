/**
 * Created by Milena on 10.12.2017.
 */


var interval = 3000;  // 1000 = 1 second, 3000 = 3 seconds
function doAjax() {
    $.ajax({
        type: 'get',
        url: '/wait-for-answer/',
        data: []
    }).done(function (data) {
        {
            if (data.everybodyVoted) {
                $(function () {
                    $(".preload").fadeOut(2000, function () {
                        $("#survey-result-container").fadeIn(1000);
                    });
                });
            }
        }
    });
}
setTimeout(doAjax, interval);