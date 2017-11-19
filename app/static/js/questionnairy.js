let answers = _.map(questions, function (question) {
    return {
        question_id: question.id, weight: '', options: _.map(options, function (option) {
            return {option_id: option.id, score: ''}
        })
    }
});

let validate=()=>{
    return true;
};
var app = new Vue({
    el: '#app',
    data: {
        answers: answers
    },
    delimiters: ["[[", "]]"],
    methods: {
        findQuestion: (id)=> {
            return _.find(questions, function (question) {
                return question.id == id
            })
        },
        findOption: (id)=> {
            return _.find(options, function (option) {
                return option.id == id
            })
        },
        submitResults: function () {
            if (validate()) {
                $.ajax({
                    type: "POST",
                    url: '/submit_results',
                    data: this.answers
                });
            }
        }
    }
});