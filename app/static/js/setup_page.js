
var setup = new Vue({
    el: '#setup',
    data: {
        alternatives: [],
        criteria: [],
        question: ""
    },
    delimiters: ["[[", "]]"],
    methods: {
        addAlternative: ()=> {
            alternatives.push('');
        },
        addCriterion: ()=> {
            criteria.push({name: '', description: '', weight: 1});
        },
        removeAlternative: (id)=> {
            var index = this.alternatives.indexOf(id);
            alternatives.splice(index, 1);
        },
        removeCriterion: (id)=> {
            var index = this.criteria.indexOf(id);
            criteria.splice(index, 1);
        }
    }
});