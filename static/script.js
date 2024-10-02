// Parallax...

let text = document.getElementById('text');
let leaf = document.getElementById('leaf');
let hill1 = document.getElementById('hill1');
let hill4 = document.getElementById('hill4');
let hill5 = document.getElementById('hill5');

window.addEventListener('scroll', () => {
    let value = window.scrollY;

    text.style.marginTop = value * 1.2 + 'px';
    leaf.style.top = value * -1.5 + 'px';
    leaf.style.left = value * 1.5 + 'px';
    hill5.style.left = value * 1.5 + 'px';
    hill4.style.left = value * -1.5 + 'px';
    hill1.style.top = value * 0.5 + 'px';
});

// Swiper...

var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
  });



  document.querySelector('.subscribe-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const email = this.querySelector('input[type="email"]').value;
    alert(`Thank you for subscribing with email: ${email}`);
    this.reset();
});

// document.querySelector('.search-bar').addEventListener('keypress', function(e) {
//     if (e.key === 'Enter') {
//         e.preventDefault();
//         const searchTerm = this.value;
//         alert(`Searching for: ${searchTerm}`);
//         this.value = '';
//     }
// });
