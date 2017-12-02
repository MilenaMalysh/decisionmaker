
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
                            return title !== '';
                        });
            names = _.every(this.criteria.name, function (name) {
                            return name !== '';
                        });
            descriptions = _.every(this.criteria.description, function (description) {
                            return description !== '';
                        });
            weights = _.every(this.criteria.weight, function (weight) {
                            return weight !== 0;
                        });
            questionDefined = function(){
                this.question !== '';
            };
            return titles && names && descriptions && weights && questionDefined;
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