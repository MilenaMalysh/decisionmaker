
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
            
            titles = _.every(this.alternatives.title, function (title) {
                            return title != '';
                        });
            names = _.every(this.criteria.name, function (name) {
                            return name != '';
                        });
            descriptions = _.every(this.criteria.description, function (description) {
                            return description != '';
                        });
            weights = _.every(this.criteria.weight, function (weight) {
                            return weight != 0;
                        });
            questionDefined = function(){
                return this.question != '';
            };
            //console.log(this.alternatives.title);
            //console.log(this.question);
            //console.log(titles);
            //console.log(names);
            //console.log(descriptions);
            //console.log(weights);
            console.log(questionDefined());
            console.log(this.question);
            console.log((this.question != ''));
            result = (titles && names && descriptions && weights && questionDefined());
            console.log(result);
            return result;
            //return questionDefined();
        },
        submit(){
            //alert('test alert');
            if(!(this.validate())){
                alert('Please fill in all the fields or delete unwanted alternatives and criteria.');
            } else{
                alert('Data submitted');//submit data
            }
        },
        addAlternative(){
            this.alternatives.push({title: ''});
            //this.submit();
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