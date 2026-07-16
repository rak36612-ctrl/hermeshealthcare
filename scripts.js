/* ==========================================================================
   Hermes Health Care - Interactivity & UX Logic
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    
    // 0. Entry Preloader Hide Logic
    const preloader = document.getElementById('entry-preloader');
    if (preloader) {
        const isFirstLoad = !sessionStorage.getItem('hermes_visited');
        if (isFirstLoad) {
            sessionStorage.setItem('hermes_visited', 'true');
            const backupTimeout = setTimeout(() => {
                preloader.classList.add('fade-out');
            }, 3000);

            window.addEventListener('load', () => {
                clearTimeout(backupTimeout);
                setTimeout(() => {
                    preloader.classList.add('fade-out');
                }, 1800);
            });
        } else {
            // Already visited in this session, hide instantly
            preloader.style.display = 'none';
        }
    }

    // 1. Mobile Menu Toggle
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    if (mobileMenuToggle && navMenu) {
        mobileMenuToggle.addEventListener('click', () => {
            mobileMenuToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        // Close menu when a link is clicked
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileMenuToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // 2. Header Scroll Effect
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // 3. Navigation Link Active State on Scroll (Intersection Observer)
    const sections = document.querySelectorAll('section');
    
    const observerOptions = {
        root: null,
        rootMargin: '-80px 0px -20% 0px', // Adjusted for header height
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    } else {
                        link.classList.remove('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // 4. Testimonial Carousel Slider (Responsive)
    const track = document.getElementById('testimonials-track');
    const cards = document.querySelectorAll('.testimonial-card');
    const dots = document.querySelectorAll('.carousel-dots .dot');
    const prevBtn = document.getElementById('prev-review-btn');
    const nextBtn = document.getElementById('next-review-btn');
    
    let currentIndex = 0;
    const totalCards = cards.length;

    function getVisibleCardsCount() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 1024) return 2;
        return 3; // Desktop
    }

    function updateCarousel() {
        if (!track || cards.length === 0) return;
        
        const visibleCards = getVisibleCardsCount();
        const maxIndex = totalCards - visibleCards;
        
        // Clamp current index
        if (currentIndex > maxIndex) {
            currentIndex = maxIndex;
        }
        if (currentIndex < 0) {
            currentIndex = 0;
        }

        const isMobile = window.innerWidth <= 768;
        const isTablet = window.innerWidth > 768 && window.innerWidth <= 1024;
        
        let gap = 30; // matches CSS gap
        if (isMobile) {
            gap = 20;
        }
        
        if (visibleCards < totalCards) {
            // Get width of a single card
            const cardWidth = cards[0].offsetWidth;
            const amountToTranslate = currentIndex * (cardWidth + gap);
            track.style.transform = `translateX(-${amountToTranslate}px)`;
        } else {
            // Reset translation on desktop where all cards fit
            track.style.transform = 'translateX(0)';
            currentIndex = 0;
        }

        // Update dot indicators
        dots.forEach((dot, index) => {
            if (index === currentIndex) {
                dot.classList.add('active');
            } else {
                dot.classList.remove('active');
            }
        });
    }

    // Carousel Button Controls
    if (nextBtn && prevBtn) {
        nextBtn.addEventListener('click', () => {
            const visibleCards = getVisibleCardsCount();
            if (currentIndex < totalCards - visibleCards) {
                currentIndex++;
            } else {
                currentIndex = 0; // Loop back
            }
            updateCarousel();
        });

        prevBtn.addEventListener('click', () => {
            const visibleCards = getVisibleCardsCount();
            if (currentIndex > 0) {
                currentIndex--;
            } else {
                currentIndex = totalCards - visibleCards; // Loop to end
            }
            updateCarousel();
        });
    }

    // Carousel Dot Controls
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            const visibleCards = getVisibleCardsCount();
            if (index <= totalCards - visibleCards) {
                currentIndex = index;
                updateCarousel();
            }
        });
    });

    // Handle Window Resize
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            updateCarousel();
        }, 100);
    });

    // Initialize carousel layout
    setTimeout(updateCarousel, 200);

    // 5. Generalized click navigation for all service cards in the grid
    const serviceCards = document.querySelectorAll('.services-grid .service-card');
    serviceCards.forEach(card => {
        card.style.cursor = 'pointer';

        const navigateToPage = () => {
            const anchor = card.querySelector('a');
            if (anchor) {
                const url = anchor.getAttribute('href');
                if (url) {
                    window.location.href = url;
                }
            }
        };

        card.addEventListener('click', (event) => {
            const isClickableChild = event.target.closest('a, button');
            if (!isClickableChild) {
                navigateToPage();
            }
        });

        card.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                navigateToPage();
            }
        });
    });
});

// 6. FAQ Accordion Toggle
document.addEventListener('DOMContentLoaded', () => {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                // Close all other items
                faqItems.forEach(other => other.classList.remove('active'));
                // Toggle the clicked item
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });
});
