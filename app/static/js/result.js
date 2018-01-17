/**
 * Created by Milena on 10.12.2017.
 */
const interval = 5000;  // 1000 = 1 second, 3000 = 3 seconds
function doAjax() {
    $.ajax({
        type: 'GET',
        url: '/decision/' + decision_id + '/result/',
        data: [],
        success: function (data) {
            var group_result = app.$data.group_result = data.group_result;
            var normal_result = app.$data.normal_result = data.normal_result;
            $(function () {
                $(".preload").fadeOut(1000, function () {
                    if (normal_result == group_result) {
                        $("#final-result").fadeIn(1000);
                    } else {
                        $("#survey-result-container").fadeIn(1000);
                    }
                });
                clearInterval(timeout)
            });
        }
    });
}


const app = new Vue({
    el: '#app',
    data: {
        group_result: group_result,
        normal_result: normal_result
    },
    delimiters: ["[[", "]]"],
    methods: {
        validate() {
            console.log(this.answers);
            return _.every(this.answers, function (answer) {
                return answer.weight && _.every(answer.options, function (option) {
                        return option.score;
                    });
            });
        },
        acceptNormal(){
            $.ajax({
                type: 'GET',
                url: '/invitation/' + invitation_id + '/accepting?result='+1,
                data: [],
                success: function (data, textStatus) {
                    if (data.redirect) {
                            window.location.href = data.redirect;
                        }
                        else {
                            alert("malformed response: " + textStatus)
                        }
                    },
                error: function (jqXHR, textStatus) {
                    alert("error " + textStatus)
                }
            });
        },
        acceptGroup(){
            $.ajax({
                type: 'GET',
                url: '/invitation/' + invitation_id + '/accepting?result='+0,
                data: [],
                success: function (data, textStatus) {
                    if (data.redirect) {
                            window.location.href = data.redirect;
                        }
                        else {
                            alert("malformed response: " + textStatus)
                        }
                    },
                error: function (jqXHR, textStatus) {
                    alert("error " + textStatus)
                }
            });
        },
    }
});

var timeout;
if (group_result == null) {
    timeout = setInterval(doAjax, interval);
} else {
    $(".preload").hide();
    if (app.$data.normal_result == app.$data.group_result) {
        $("#final-result").show();
    } else {
        $("#survey-result-container").show();
    }
}