# -*- coding: utf-8 -*-
import os
import json

# Define the common navigation, styling references and structures
HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{meta_desc}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://hermeshealthcare.in/{dir}/index.html">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://hermeshealthcare.in/{dir}/index.html">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:image" content="../images/logo.png">

    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:url" content="https://hermeshealthcare.in/{dir}/index.html">
    <meta property="twitter:title" content="{title}">
    <meta property="twitter:description" content="{meta_desc}">
    <meta property="twitter:image" content="../images/logo.png">

    <!-- Fonts & Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../styles.css">

    <!-- JSON-LD Schemas -->
    <script type="application/ld+json">
    {schema_json}
    </script>
</head>
<body>
"""

HEADER_TEMPLATE = """
    <!-- Header Navigation -->
    <header class="main-header" id="header">
        <div class="header-container">
            <a href="../index.html#home" class="logo-link">
                <img src="../images/logo.png" alt="Hermes Health Care Logo" class="clinic-logo">
            </a>
            <nav class="nav-menu" id="nav-menu" aria-label="Main Navigation">
                <ul>
                    <li><a href="../index.html#home" class="nav-link">Home</a></li>
                    <li><a href="../index.html#services" class="nav-link">Services</a></li>
                    <li><a href="../physiotherapy/index.html" class="nav-link">Physiotherapy</a></li>
                    <li><a href="#doctors" class="nav-link">Doctors</a></li>
                    <li><a href="../index.html#about" class="nav-link">About Us</a></li>
                    <li><a href="../index.html#contact" class="nav-link">Contact</a></li>
                </ul>
            </nav>
            <div class="header-cta">
                <a href="tel:+916360855615" class="btn-phone-header" aria-label="Call clinic at 06360855615">
                    <i class="fa-solid fa-phone"></i>
                    <span>06360855615</span>
                </a>
                <button class="mobile-menu-toggle" id="mobile-menu-toggle" aria-label="Toggle navigation menu">
                    <span class="bar"></span>
                    <span class="bar"></span>
                    <span class="bar"></span>
                </button>
            </div>
        </div>
    </header>

    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <ol itemscope itemtype="https://schema.org/BreadcrumbList">
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="../index.html#home">
                    <span itemprop="name">Home</span>
                </a>
                <meta itemprop="position" content="1" />
            </li>
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <a itemprop="item" href="../index.html#services">
                    <span itemprop="name">Services</span>
                </a>
                <meta itemprop="position" content="2" />
            </li>
            <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                <span itemprop="name">{breadcrumb_name}</span>
                <meta itemprop="position" content="3" />
            </li>
        </ol>
    </nav>
"""

FOOTER_TEMPLATE = """
    <!-- Footer -->
    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-info-col">
                <div class="footer-logo-wrapper">
                    <img src="../images/logo.png" alt="Hermes Health Care Logo" class="footer-logo">
                </div>
                <p class="footer-about-text">Hermes Health Care is a premier multi-speciality medical clinic and day care surgery centre in Ullal, Bengaluru, delivering compassionate and evidence-based patient-first care.</p>
            </div>
            <div class="footer-links-col">
                <h4 class="footer-col-title">Our Departments</h4>
                <ul class="footer-links">
                    <li><a href="../general-medicine/index.html">General Medicine</a></li>
                    <li><a href="../orthopaedics/index.html">Orthopaedic Care</a></li>
                    <li><a href="../diabetes/index.html">Diabetes Centre</a></li>
                    <li><a href="../physiotherapy/index.html">Physiotherapy Unit</a></li>
                    <li><a href="../diagnostics/index.html">Lab & Diagnostics</a></li>
                    <li><a href="../daycare-nursing/index.html">Day Care & Surgery</a></li>
                    <li><a href="../gynecology/index.html">Gynecology & Fertility</a></li>
                    <li><a href="../gastroenterology/index.html">Gastroenterology</a></li>
                    <li><a href="../ophthalmology/index.html">Ophthalmology</a></li>
                </ul>
            </div>
            <div class="footer-contact-col">
                <h4 class="footer-col-title">Contact Info</h4>
                <p><i class="fa-solid fa-location-dot"></i> Ullal, Sir M Vishveswaraya Layout, Jnana Ganga Nagar, Bengaluru, KA 560110</p>
                <p><i class="fa-solid fa-phone"></i> <a href="tel:+916360855615">063608 55615</a></p>
                <p><i class="fa-brands fa-whatsapp"></i> <a href="https://wa.me/916360855615">+91 63608 55615</a></p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Hermes Health Care. Multi-Speciality Clinic & Day Care Centre. All rights reserved.</p>
        </div>
    </footer>

    <!-- Bottom Sticky Bar -->
    <div class="bottom-sticky-bar">
        <a href="tel:+916360855615" class="sticky-item sticky-call">
            <div class="sticky-icon"><i class="fa-solid fa-phone"></i></div>
            <div class="sticky-text">
                <span class="sticky-title">Call Clinic</span>
                <span class="sticky-subtitle">06360855615</span>
            </div>
        </a>
        <a href="https://wa.me/916360855615?text=Hello%20Hermes%20Health%20Care,%20I%20would%20like%20to%20book%20an%20appointment." target="_blank" rel="noopener noreferrer" class="sticky-item sticky-whatsapp">
            <div class="sticky-icon"><i class="fa-brands fa-whatsapp"></i></div>
            <div class="sticky-text">
                <span class="sticky-title">WhatsApp Chat</span>
                <span class="sticky-subtitle">Book Appointment</span>
            </div>
        </a>
        <a href="../index.html#contact" class="sticky-item sticky-directions">
            <div class="sticky-icon"><i class="fa-solid fa-location-dot"></i></div>
            <div class="sticky-text">
                <span class="sticky-title">Clinic Details</span>
                <span class="sticky-subtitle">Back to Main Site</span>
            </div>
        </a>
        <div class="sticky-item sticky-hours">
            <div class="sticky-icon"><i class="fa-solid fa-clock"></i></div>
            <div class="sticky-text">
                <span class="sticky-title">Open Daily</span>
                <span class="sticky-subtitle">9:00 AM – 9:30 PM</span>
            </div>
        </div>
    </div>

    <script src="../scripts.js"></script>
</body>
</html>
"""

# Let's run a test file creation script that has the complete content for the pages
# Because of output size limits, we'll write the script to write pages dynamically
# by generating rich, descriptive medical texts per section.
# We will use high-quality template values.
