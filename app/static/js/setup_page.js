
var setup = new Vue({
    el: '#setup',
    data: {
        alternatives: [],
        criteria: [],
        question: ""
    },
    delimiters: ["[[", "]]"],
    methods: {
        validate(){
            console.log('aaaa');
            titles = _.every(alternatives.title, function (title) {
                            return title !== '';
                        });
            names = _.every(criteria.name, function (name) {
                            return name !== '';
                        });
            descriptions = _.every(criteria.description, function (description) {
                            return description !== '';
                        });
            weights = _.every(criteria.weight, function (weight) {
                            return weight !== 0;
                        });
            questionDefined = function(){
                this.question !== '';
            };
            return titles && names && descriptions && weights && questionDefined;
        },
        submit(){
            alert('test alert');
            if(!validate()){
                alert('Please fill in all the fields or delete unwanted alternatives and criteria.');
            } else{
                //submit data
            }
        },
        addAlternative(){
            this.alternatives.push({title: ''});
            submit();
        },
        addCriterion(){
            this.criteria.push({name: '', description: '', weight: 0});
        },
        removeAlternative(index){
            this.alternatives.splice(index, 1);
            console.log(this);
        },
        removeCriterion(id){
            var index = this.criteria.indexOf(id);
            this.criteria.splice(index, 1);
        }
    }
});