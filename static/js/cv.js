
// Light and dark theme
const themeButton = document.getElementById('theme-button');
const darkTheme = 'dark-theme';
const iconTheme = 'bi-sun-fill';
const selectedTheme = localStorage.getItem('selected-theme');
const selectedIcon = localStorage.getItem('selected-icon');
const getCurrentTheme = () => document.body.classList.contains(darkTheme) ? 'dark' : 'light';
const getCurrentIcon = () => themeButton.classList.contains(iconTheme) ? 'bi-moon-fill' : 'bi-sun-fill';

if (selectedTheme){
   document.body.classList[selectedTheme === 'dark' ? 'add' : 'remove'](darkTheme);
   themeButton.classList[selectedIcon === 'bi-moon-fill' ? 'add' : 'remove'](iconTheme);
}

themeButton.addEventListener("click", (e) => {
   document.body.classList.toggle(darkTheme);
   themeButton.classList.toggle(iconTheme);

   localStorage.setItem('selected-theme', getCurrentTheme());
   localStorage.setItem('selected-icon', getCurrentIcon());
});
// ****************************


// Print to pdf
const areaCv = document.getElementById('area-cv');
const downloadButton = document.getElementById('print2pdf');
let options = {
  margin:       0,
  filename:     'Zoltan_Domonkos_Cv.pdf',
  image:        { type: 'jpeg', quality: 0.98 },
  html2canvas:  { scale: 2 },
  jsPDF:        { format: 'a4', orientation: 'portrait' }
};

downloadButton.addEventListener("click", (e) => {
   html2pdf().set(options).from(areaCv).save();
});
// ****************************