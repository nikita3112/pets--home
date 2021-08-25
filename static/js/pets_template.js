const btn = document.querySelectorAll('.card-btn');
const star = document.querySelectorAll('#Capa_1');
const checkbox = document.querySelector('.switch__2');
const swText = document.querySelector('.switch-text');

btn.forEach(bt => {
    bt.addEventListener('click', () => {
        if (bt.children[0].style.fill !== "gold") {
            bt.children[0].style.fill = "gold";
        } else {
            bt.children[0].style.fill = "#9baacf";
        }
    });
});

checkbox.addEventListener('mouseover', () => {
    swText.style.display = "block";
});

checkbox.addEventListener('mouseout', () => {
    swText.style.display = "none";
});