const headings = $('h1');

headings.eq(0).hover(function() {
    headings.eq(0).text("Mouse Currently Over :)");
    changeHeaderColor(headings.eq(0))
}, function() {
    headings.eq(0).text("HOVER OVER ME!");
    headings.eq(0).css("color", "black");
});

headings.eq(1).click(function() {
    headings.eq(1).text("CLICKED :)");
    changeHeaderColor(headings.eq(1))
});

$('input').on('click', function () {
    ($('.boxy')).fadeOut();

    $('input').attr("value", "faded")
});

function getRandomColor() {
    let letters = "0123456789ABCDEF";
    let color = "#";
    while (color.length < 7) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function changeHeaderColor(header) {
    header.css("color", getRandomColor());
}