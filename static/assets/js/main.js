   //carousel
   
   $(document).ready(function() {
    function showText(textElement) {
        const text = $(textElement).data('text');
        $(textElement).html(''); 
        $(textElement).css('opacity', 1); 

        let index = 0;
        const interval = setInterval(() => {
            if (index < text.length) {
                $(textElement).append(text[index]);
                index++;
            } else {
                clearInterval(interval);
            }
        }, 100); 
    }

    $('.carousel ').on('slide.bs.carousel', function(e) {
        const $currentSlide = $(e.relatedTarget); 

        
        $currentSlide.find('.carousel-caption p').each(function() {
            const $textElement = $(this);
            $textElement.css('opacity', 0); 
            $textElement.html('');
        });

        $('.carousel-item img').css('transform', 'scale(1)');
    });

    $('.carousel').on('slid.bs.carousel', function(e) {
        const $currentSlide = $(e.relatedTarget); 

        $currentSlide.find('.carousel-caption p').each(function() {
            const $textElement = $(this);
            showText($textElement);
        });

        $currentSlide.find('img').css('transform', 'scale(1.1)');
    });

    $('.carousel-item.active .carousel-caption p').each(function() {
        const $textElement = $(this);
        showText($textElement);
    });

    $('.carousel-item.active img').css('transform', 'scale(1.1)');
});




  
  new PureCounter();

  
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


//testimonials
  window.addEventListener("load", initSwiper);

  document.addEventListener("DOMContentLoaded", function () {
    const lightbox = GLightbox({
        selector: '.glightbox',
    });
});



//eye icon

document.addEventListener("DOMContentLoaded", function() {
  const lightboxContainer = document.querySelector('.portfolio-lightbox-container');
  const lightboxImg = document.querySelector('.lightbox-img');
  const closeBtn = document.querySelector('.close-btn');

  if (!lightboxContainer || !lightboxImg || !closeBtn) {
    console.error("Lightbox elements are missing!");
    return;
  }

  
  document.querySelectorAll('.portfolio-lightbox').forEach(function(link) {
    link.addEventListener('click', function(e) {
      e.preventDefault(); 
      const imgSrc = link.getAttribute('href'); 
      if (imgSrc) {
        lightboxImg.src = imgSrc; 
        lightboxContainer.style.display = 'flex'; 
      } else {
        console.error("Image source is missing!");
      }
    });
  });

  closeBtn.addEventListener('click', function() {
    lightboxContainer.style.display = 'none';
    lightboxImg.src = ''; 
  });
});
