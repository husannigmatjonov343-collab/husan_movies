(function () {
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');
    if (!slides.length) return;

    let current = 0;
    let timer;

    function show(index) {
        slides.forEach(s => s.classList.remove('active'));
        dots.forEach(d => d.classList.remove('active'));
        slides[index].classList.add('active');
        if (dots[index]) dots[index].classList.add('active');
        current = index;
    }

    function next() {
        show((current + 1) % slides.length);
    }

    function startAuto() {
        timer = setInterval(next, 6000);
    }

    dots.forEach(dot => {
        dot.addEventListener('click', () => {
            clearInterval(timer);
            show(parseInt(dot.dataset.index, 10));
            startAuto();
        });
    });

    startAuto();
})();
