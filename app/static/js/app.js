// KinoSayt umumiy skriptlar
// Har bir sahifada mavjud bo'lgan kichik yordamchi funksiyalar shu yerga qo'shiladi.

document.addEventListener('DOMContentLoaded', () => {
    // Rasm yuklanmasa, standart rasmga almashtirish
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', () => {
            img.src = 'https://via.placeholder.com/400x600/16171c/9a9ba3?text=Poster+yo%27q';
        }, { once: true });
    });
});
