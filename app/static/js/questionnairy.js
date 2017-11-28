var app = new Vue({
        el: '#app',
        data: {
            answers: _.map(questions, function (question) {
                return {
                    question_id: question.id, weight: '', options: _.map(options, function (option) {
                        return {option_id: option.id, score: ''}
                    })
                }
            })
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
            findQuestion(id){
                return _.find(questions, function (question) {
                    return question.id == id
                })
            },
            findOption(id){
                return _.find(options, function (option) {
                    return option.id == id
                })
            },
            submitResults() {
                if (this.validate()) {
                    console.log('aaaa');
                    $.ajax({
                        url: '/submit_results/',
                        type: 'post',
                        data: {
                            answers: this.answers
                        }
                    }).done(function (val) {
                        console.log(val);
                    })
                }
            }
        }
    });