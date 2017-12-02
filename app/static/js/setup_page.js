
var setup = new Vue({
    el: '#setup',
    data: {
        alternatives: [],
        criteria: [],
        question: ""
    },
    delimiters: ["[[", "]]"],
    methods: {
        addAlternative(){
            this.alternatives.push({});
        },
        addCriterion(){
            this.criteria.push({name: '', description: '', weight: 1});
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