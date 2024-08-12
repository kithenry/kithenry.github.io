document.addEventListener("DOMContentLoaded", function () {
    fetch('/assets/snippets/header.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('header').innerHTML = data;
        });

    fetch('/assets/snippets/footer.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('footer').innerHTML = data;
        });
});