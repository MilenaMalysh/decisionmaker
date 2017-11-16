/**
 * Created by Milena on 10.11.2017.
 */
console.log($(".importance-value"));
$(".ranged-value").on("input", function () {
    var isAllowed = /^\+?(0|[1-9]\d*)$/.test(this.value);
    if (isAllowed) {
        if (parseInt(this.value) < 0) {
            this.value = 1;
        } else if (parseInt(this.value) > 10) {
            this.value = 10;
        }
    }else{
        this.value = '';
    }
});

$(".ranged-value").keydown(function (e) {
    if (e.which > 90 || (e.which < 48 && e.which < 65)) {
        e.preventDefault();
    }
});
