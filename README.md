# practice_-_demo

<div align="center">
  <img src="path/to/slide1.jpg" alt="Slide 1" id="slide-image">
</div>

<div align="center">
  <button onclick="previousSlide()">Previous</button>
  <button onclick="nextSlide()">Next</button>
</div>

<script>
  var slideIndex = 0;
  var slideImages = [
    'path/to/slide1.jpg',
    'path/to/slide2.jpg',
    'path/to/slide3.jpg',
    // Add more slide image paths as needed
  ];
  
  function previousSlide() {
    if (slideIndex === 0) {
      slideIndex = slideImages.length - 1;
    } else {
      slideIndex--;
    }
    document.getElementById('slide-image').src = slideImages[slideIndex];
  }
  
  function nextSlide() {
    if (slideIndex === slideImages.length - 1) {
      slideIndex = 0;
    } else {
      slideIndex++;
    }
    document.getElementById('slide-image').src = slideImages[slideIndex];
  }
</script>
