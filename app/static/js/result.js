// /**
//  * Created by Milena on 10.12.2017.
//  */
// const interval = 5000;  // 1000 = 1 second, 3000 = 3 seconds
// function doAjax() {
//     $.ajax({
//         type: 'GET',
//         url: '/decision/' + decision_id + /result/,
//         data: [],
//         success: function (data) {
//             group_result = app.$data.group_result = data.group_result;
//             normal_result = app.$data.normal_result = data.normal_result;
//             $(function () {
//                 $(".preload").fadeOut(1000, function () {
//                     $("#survey-result-container").fadeIn(1000);
//                 });
//                 clearInterval(timeout)
//             });
//         }
//     });
// }
//
// var timeout;
// if (group_result == null) {
//     timeout = setInterval(doAjax, interval);
// } else {
//     $(".preload").hide();
//     $("#survey-result-container").show();
// }
//
//
// const app = new Vue({
//     el: '#app',
//     data: {
//         group_result: group_result,
//         normal_result: normal_result
//     },
//     delimiters: ["[[", "]]"],
//     methods: {
//         validate() {
//             console.log(this.answers);
//             return _.every(this.answers, function (answer) {
//                 return answer.weight && _.every(answer.options, function (option) {
//                     return option.score;
//                 });
//             });
//         },
//     }
// });