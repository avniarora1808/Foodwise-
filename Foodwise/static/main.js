class Typewriter{
    constructor(txtElement, words, wait = 3000) {
        this.txtElement = txtElement;
        this.words = words;
        this.txt = '';
        this.wordIndex = 0;
        this.wait = parseInt(wait, 10);
        this.type();
        this.isDeleting = false;
    }

    type() {
    // Current index of word
    const current = this. wordIndex % this.words.length;
    // Get full text of current word
    const fullTxt = this.words [current];

    // Check if deleting
    if(this.isDeleting) {
    //remove char
    this.txt = fullTxt.substring(0, this.txt.length - 1);
    }else {
        //Add char
        this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    // Insert txt into element

    if (this.txt == ""){
        this.txtElement.innerHTML = `<span class="txt"> <pre> </pre> </span>`;
    }
    else {
        this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;
    }
    

    // Type Speed
    let typeSpeed = 300;

    if(this.isDeleting) {
    typeSpeed = typeSpeed/= 2; 
    }

    // If word is complete
    if(!this.isDeleting&& this.txt === fullTxt) {
        // Make a pause at end
        typeSpeed = this.wait;
        // Set delete to true
        this.isDeleting = true;
    } else if(this.isDeleting && this.txt ===''){
        this.isDeleting = false;
        // Move to the next word
        this.wordIndex++;
        // Pause before start typing
        typeSpeed = 500;
    }

        setTimeout(() => this.type(), typeSpeed)
    }
}


// Init On DOM Load
document.addEventListener('DOMContentLoaded', init);

// Init App
function init() {
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    //Init Typewriter
    new Typewriter(txtElement, words, wait);

}

function myFunction() {
    var x = document.getElementById("myNavbar");
    if (x.className === "navbar") {
        x.className += " responsive";
    } else {
        x.className = "navbar";
    }
}


var slideIndex = 0;
showSlides();

// Next/previous controls
function plusSlides(n) {
    showpSlides(slideIndex += n);
}
function subSlides(n) {
    showsSlides(slideIndex -= n);
}
 
// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}


function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
    }   
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 5000); // Change image every 3 seconds
}

