
var setup = new Vue({
    console.log("Test log");
    el: '#setup',
    data: {
        options: [];
        criteria: [];
        question: "";
    },
    delimiters: ["[[", "]]"],
    methods: {
        addOption: ()=> {
            options.push('');
        },
        addCriterion: ()=> {
            criteria.push({name: '', description: '', weight: 1});
        },
        removeOption: (id)=> {
            var index = this.options.indexOf(id);
            options.splice(index, 1);
        }
        removeCriterion: (id)=> {
            var index = this.criteria.indexOf(id);
            criteria.splice(index, 1);
        }
    }
});