var setup = new Vue({
    el: '#setup',
    data: {
        alternatives: [],
        currentAlternative: {title: ''},
        criteria: [],
        currentCriterion: {name: '', description: '', weight: ""},
        users: [],
        currentUser: {title: ''},
        question: ""
    },
    delimiters: ["[[", "]]"],
    methods: {
        validate() {
            return ((this.alternatives.length >= 1) && (this.criteria.length >= 1) && (this.users.length >= 1) && this.question);
        },
        submit() {
            if (!(this.validate())) {
                alert('Please fill survey title and add at least one option, criterion, user.');
            } else {
                //submit data
                $.ajax({
                    type: "POST",
                    url: '/decision/create',
                    data: JSON.stringify({
                        decision: this.question,
                        options: this.alternatives,
                        criteria: this.criteria,
                        users: this.users
                    }),
                    dataType: "json",
                    success: function (data, textStatus) {
                        if (data.redirect) {
                            window.location.href = data.redirect;
                        }
                        else {
                            alert("malformed response: "+ textStatus)
                        }
                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                        alert("error " + textStatus)
                    }
                });
            }
        },
        addAlternative() {
            if (this.currentAlternative.title) {
                this.alternatives.push(this.currentAlternative);
                this.currentAlternative = {title: ''};
            }
        },
        addUser() {
            if (this.currentUser.email) {
                this.users.push(this.currentUser);
                this.currentUser = {email: ''};
            }
        },
        addCriterion() {
            if (this.currentCriterion.title && this.currentCriterion.description && this.currentCriterion.weight) {
                this.criteria.push(this.currentCriterion);
                this.currentCriterion = {name: '', description: '', weight: ""};
            }
        },
        removeAlternative(index) {
            this.alternatives.splice(index, 1);
        },
        removeCriterion(index) {
            this.criteria.splice(index, 1);
        },
        removeUser(index) {
            this.users.splice(index, 1);
        }
    }
});