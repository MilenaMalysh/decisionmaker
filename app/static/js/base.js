/**
 * Created by Milena on 10.11.2017.
 */

$(".ranged-value").on("keyup", function () {
    var isAllowed = /^\+?(0|[1-9]\d*)$/.test(this.value);
    if (isAllowed) {
        if (parseInt(this.value) < 1) {
            this.value = 1;
        } else if (parseInt(this.value) > 10) {
            this.value = 10;
        }
    }else{
        this.value = '';
    }
    this.dispatchEvent(new Event('change', { 'bubbles': true }))
});

$(".ranged-value").keydown(function (e) {
    if (e.which == 188 || e.which == 190) {
        e.preventDefault();
    }
});
