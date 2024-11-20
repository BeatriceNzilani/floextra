   $(document).ready(function() {
    // Function to show text with typing effect
    function showText(textElement) {
        const text = $(textElement).data('text');
        $(textElement).html(''); // Clear previous text
        $(textElement).css('opacity', 1); // Ensure it's visible

        let index = 0;
        const interval = setInterval(() => {
            if (index < text.length) {
                $(textElement).append(text[index]);
                index++;
            } else {
                clearInterval(interval);
            }
        }, 100); // Speed of typing effect
    }

    // On carousel slide transition
    $('.carousel ').on('slide.bs.carousel', function(e) {
        const $currentSlide = $(e.relatedTarget); // Get the next slide

        // Reset typing effect
        $currentSlide.find('.carousel-caption p').each(function() {
            const $textElement = $(this);
            $textElement.css('opacity', 0); // Hide text at start
            $textElement.html(''); // Clear text content
        });

        // Reset scale of image on the current slide
        $('.carousel-item img').css('transform', 'scale(1)');
    });

    // After carousel slide transition
    $('.carousel').on('slid.bs.carousel', function(e) {
        const $currentSlide = $(e.relatedTarget); // Get the next slide

        // Apply typing effect to the new slide
        $currentSlide.find('.carousel-caption p').each(function() {
            const $textElement = $(this);
            showText($textElement);
        });

        // Scale up the image on the active slide
        $currentSlide.find('img').css('transform', 'scale(1.1)');
    });

    // Initialize typing effect and image scale on the first slide
    $('.carousel-item.active .carousel-caption p').each(function() {
        const $textElement = $(this);
        showText($textElement);
    });

    // Scale up the image on the first slide
    $('.carousel-item.active img').css('transform', 'scale(1.1)');
});




   /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }



  window.addEventListener("load", initSwiper);

  document.addEventListener("DOMContentLoaded", function () {
    const lightbox = GLightbox({
        selector: '.glightbox',
    });
});

//portfolio


   document.addEventListener("DOMContentLoaded", function() {
  // Open the lightbox when image or eye icon is clicked
  document.querySelectorAll('.portfolio-lightbox').forEach(function(link) {
    link.addEventListener('click', function(e) {
      e.preventDefault(); // Prevent default link behavior
      const imgSrc = link.getAttribute('href'); // Get the image source
      const lightbox = document.querySelector('.portfolio-lightbox-container');
      const lightboxImg = document.querySelector('.lightbox-img');
      lightboxImg.src = imgSrc; // Set the lightbox image source
      lightbox.style.display = 'flex'; // Show the lightbox
    });
  });

  // Close the lightbox when X is clicked
  document.querySelector('.close-btn').addEventListener('click', function() {
    document.querySelector('.portfolio-lightbox-container').style.display = 'none';
  });
});
