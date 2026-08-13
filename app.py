import streamlit as st
import streamlit.components.v1 as components

# Configure the Streamlit page to take up the full screen
st.set_page_config(layout="wide", page_title="Ariba Naeem - Portfolio")

# Hide Streamlit's default header, footer, and padding for a clean, website-like look
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem; 
                padding-bottom: 0rem; 
                padding-left: 0rem; 
                padding-right: 0rem;
                max-width: 100%;
            }
            /* Adjust iframe to ensure no scrollbars appear around the main container */
            iframe {
                border: none;
                width: 100%;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Your complete HTML, CSS, and JS code embedded as a string
portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ariba Naeem - Bioinformatician & Computational Biologist</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #0A0E27;
            --secondary: #1A1F3A;
            --accent: #00D4FF;
            --accent-dark: #0099CC;
            --light-bg: #F0F4F9;
            --card-bg: #FFFFFF;
            --text-dark: #0A0E27;
            --text-light: #5A6A7A;
            --text-lighter: #8A99A8;
            --border: #D4DFE8;
            --success: #00D084;
            --gold: #FFB800;
            --gradient-1: linear-gradient(135deg, #00D4FF 0%, #0099CC 100%);
            --gradient-2: linear-gradient(135deg, #0A0E27 0%, #1A1F3A 100%);
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Outfit', sans-serif;
            line-height: 1.6;
            color: var(--text-dark);
            background: #FFFFFF;
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero {
            background: var(--gradient-2);
            color: white;
            padding: 80px 20px 120px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.12) 0%, transparent 70%);
            border-radius: 50%;
            top: -300px;
            right: -300px;
        }

        .hero::after {
            content: '';
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.08) 0%, transparent 70%);
            border-radius: 50%;
            bottom: -250px;
            left: -200px;
        }

        .hero-content {
            max-width: 900px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
            animation: fadeInUp 1s ease-out;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .hero-image-section {
            display: flex;
            justify-content: center;
            align-items: center;
            order: -1;
        }

        .profile-picture-container {
            position: relative;
            width: 280px;
            height: 280px;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.25);
            border: 3px solid rgba(255, 255, 255, 0.1);
            animation: profileFloat 3s ease-in-out infinite;
        }

        .profile-picture-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.2) 0%, rgba(0, 208, 132, 0.2) 100%);
            z-index: 2;
        }

        .profile-placeholder {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #1A2F4A 0%, #0F1E35 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: rgba(255, 255, 255, 0.2);
        }

        .profile-picture-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .profile-ring {
            position: absolute;
            width: 300px;
            height: 300px;
            border: 2px solid rgba(0, 212, 255, 0.3);
            border-radius: 20px;
            top: -10px;
            left: -10px;
            animation: ringRotate 8s linear infinite;
        }

        @keyframes profileFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        @keyframes ringRotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .hero-text-section {
            text-align: left;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 15px;
            letter-spacing: -1.5px;
            line-height: 1.15;
            background: linear-gradient(135deg, #FFFFFF 0%, #C0E7FF 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero .title {
            font-size: 1.3rem;
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 25px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .hero p {
            font-size: 1.05rem;
            color: #B8D0E0;
            margin-bottom: 35px;
            line-height: 1.85;
        }

        .hero-meta {
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            margin-top: 30px;
            font-size: 0.9rem;
        }

        .meta-item {
            padding: 10px 18px;
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(0, 212, 255, 0.25);
            border-radius: 8px;
            backdrop-filter: blur(20px);
            font-weight: 500;
        }

        .achievement-badge {
            display: inline-block;
            background: linear-gradient(135deg, var(--gold) 0%, #FFD700 100%);
            color: #0A0E27;
            padding: 12px 28px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.95rem;
            margin-top: 25px;
            letter-spacing: 0.5px;
            box-shadow: 0 8px 20px rgba(255, 184, 0, 0.3);
            text-transform: uppercase;
        }

        /* Navigation */
        nav {
            position: sticky;
            top: 0;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            padding: 16px 20px;
            border-bottom: 1px solid var(--border);
            z-index: 1000;
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--primary);
            letter-spacing: 0.5px;
        }

        .nav-links {
            display: flex;
            gap: 35px;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-light);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
            font-size: 0.9rem;
            letter-spacing: 0.3px;
        }

        .nav-links a:hover {
            color: var(--accent);
        }

        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }
            .hero h1 {
                font-size: 2.8rem;
            }
        }

        /* Sections */
        section {
            padding: 90px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.2rem;
            font-weight: 800;
            color: var(--primary);
            margin-bottom: 60px;
            position: relative;
            display: inline-block;
            letter-spacing: -0.8px;
        }

        .section-title::before {
            content: '';
            position: absolute;
            left: 0;
            top: -20px;
            width: 40px;
            height: 4px;
            background: var(--gold);
            border-radius: 2px;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -15px;
            left: 0;
            width: 60px;
            height: 3px;
            background: var(--gradient-1);
            border-radius: 2px;
        }

        /* About Section */
        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 60px;
            align-items: center;
        }

        .about-text h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            color: var(--primary);
            margin-bottom: 20px;
            letter-spacing: -0.5px;
        }

        .about-text p {
            color: var(--text-light);
            margin-bottom: 20px;
            line-height: 1.9;
            font-size: 1rem;
        }

        .about-highlights {
            display: grid;
            gap: 18px;
        }

        .highlight-item {
            padding: 20px;
            background: var(--light-bg);
            border-left: 3px solid var(--accent);
            border-radius: 6px;
            transition: all 0.3s ease;
        }

        .highlight-item:hover {
            background: #F1F5F9;
            box-shadow: 0 4px 12px rgba(14, 165, 233, 0.08);
        }

        .highlight-item strong {
            color: var(--primary);
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
        }

        @media (max-width: 768px) {
            .about-content {
                grid-template-columns: 1fr;
            }
        }

        /* Skills Section */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 28px;
        }

        .skill-category {
            padding: 40px;
            background: var(--card-bg);
            border-radius: 12px;
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            border: 1px solid var(--border);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
            position: relative;
            overflow: hidden;
        }

        .skill-category::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: var(--gradient-1);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.5s cubic-bezier(0.23, 1, 0.320, 1);
        }

        .skill-category:hover::before {
            transform: scaleX(1);
        }

        .skill-category:hover {
            border-color: var(--accent);
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0, 212, 255, 0.15);
        }

        .skill-category h4 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.15rem;
            color: var(--primary);
            margin-bottom: 20px;
            font-weight: 600;
            letter-spacing: 0.3px;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 9px;
        }

        .skill-tag {
            background: var(--light-bg);
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 0.85rem;
            border: 1px solid var(--border);
            color: var(--text-dark);
            transition: all 0.3s ease;
            cursor: pointer;
            font-weight: 500;
        }

        .skill-tag:hover {
            background: var(--accent);
            color: white;
            border-color: var(--accent);
            transform: translateY(-2px);
        }

        /* Experience Section */
        .experience-container {
            display: grid;
            gap: 30px;
        }

        .experience-item {
            padding: 40px;
            background: var(--card-bg);
            border-radius: 12px;
            border-left: 4px solid var(--accent);
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            border: 1px solid var(--border);
            border-left: 4px solid var(--accent);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
            position: relative;
        }

        .experience-item:hover {
            box-shadow: 0 16px 40px rgba(0, 212, 255, 0.15);
            transform: translateX(6px);
            border-color: var(--accent);
        }

        .exp-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            gap: 20px;
            margin-bottom: 18px;
        }

        .exp-header h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            color: var(--primary);
            flex: 1;
            letter-spacing: -0.3px;
        }

        .exp-meta {
            font-size: 0.85rem;
            color: var(--text-lighter);
            font-weight: 500;
            white-space: nowrap;
        }

        .exp-description {
            color: var(--text-light);
            margin-bottom: 16px;
            line-height: 1.8;
            font-weight: 500;
        }

        .exp-points {
            list-style: none;
            padding-left: 0;
        }

        .exp-points li {
            color: var(--text-light);
            padding-left: 22px;
            position: relative;
            margin-bottom: 12px;
            line-height: 1.7;
        }

        .exp-points li::before {
            content: '•';
            position: absolute;
            left: 0;
            color: var(--accent);
            font-weight: bold;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
            gap: 28px;
        }

        .project-card {
            background: var(--card-bg);
            padding: 40px;
            border-radius: 12px;
            border-top: 3px solid var(--accent);
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            border: 1px solid var(--border);
            border-top: 3px solid var(--accent);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }

        .project-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 16px 40px rgba(0, 212, 255, 0.15);
        }

        .project-number {
            display: inline-flex;
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dark) 100%);
            color: white;
            width: 40px;
            height: 40px;
            border-radius: 8px;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-family: 'Outfit', sans-serif;
            margin-bottom: 18px;
            font-size: 1rem;
        }

        .project-card h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.2rem;
            color: var(--primary);
            margin-bottom: 14px;
            letter-spacing: -0.3px;
        }

        .project-card p {
            color: var(--text-light);
            font-size: 0.95rem;
            line-height: 1.8;
        }

        /* Education Section */
        .education-container {
            display: grid;
            gap: 25px;
        }

        .education-item {
            padding: 40px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            position: relative;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        }

        .education-item:hover {
            border-color: var(--accent);
            box-shadow: 0 16px 40px rgba(0, 212, 255, 0.15);
            transform: translateY(-6px);
        }

        .education-item::before {
            content: '';
            position: absolute;
            right: 25px;
            top: 25px;
            width: 4px;
            height: 4px;
            background: var(--accent);
            border-radius: 50%;
        }

        .edu-degree {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 10px;
            letter-spacing: -0.3px;
        }

        .edu-school {
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 6px;
            font-size: 1rem;
        }

        .edu-date {
            color: var(--text-lighter);
            font-size: 0.9rem;
            margin-bottom: 12px;
            font-weight: 500;
        }

        .edu-cgpa {
            display: inline-block;
            background: linear-gradient(135deg, var(--accent) 0%, var(--success) 100%);
            color: white;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.3px;
        }

        /* Awards Section */
        .awards-list {
            display: grid;
            gap: 22px;
        }

        .award-item {
            padding: 32px;
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.05) 0%, rgba(0, 208, 132, 0.05) 100%);
            border-left: 3px solid var(--accent);
            border-radius: 10px;
            display: flex;
            gap: 22px;
            align-items: flex-start;
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            border: 1px solid var(--border);
            border-left: 3px solid var(--accent);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
        }

        .award-item:hover {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1) 0%, rgba(0, 208, 132, 0.1) 100%);
            transform: translateX(6px);
            box-shadow: 0 8px 24px rgba(0, 212, 255, 0.1);
        }

        .award-icon {
            font-size: 1.5rem;
            opacity: 0.7;
        }

        .award-text {
            flex: 1;
        }

        .award-text h4 {
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 6px;
            font-size: 1.1rem;
        }

        .award-text p {
            color: var(--text-light);
            font-size: 0.95rem;
            line-height: 1.6;
        }

        /* Contact Section */
        .contact-section {
            background: var(--gradient-2);
            color: white;
            text-align: center;
            padding: 120px 20px;
            position: relative;
            overflow: hidden;
        }

        .contact-section::before {
            content: '';
            position: absolute;
            width: 800px;
            height: 800px;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.12) 0%, transparent 70%);
            border-radius: 50%;
            bottom: -300px;
            right: -200px;
        }

        .contact-section::after {
            content: '';
            position: absolute;
            width: 600px;
            height: 600px;
            background: radial-gradient(circle, rgba(0, 212, 255, 0.08) 0%, transparent 70%);
            border-radius: 50%;
            top: -200px;
            left: -150px;
        }

        .contact-section .section-title {
            color: white;
            margin-bottom: 20px;
        }

        .contact-section .section-title::before {
            background: var(--gold);
        }

        .contact-section .section-title::after {
            background: var(--gradient-1);
        }

        .contact-section > p {
            font-size: 1.15rem;
            color: #B8D0E0;
            margin-bottom: 60px;
            letter-spacing: 0.5px;
        }

        .contact-links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 28px;
            margin: 0 auto;
            max-width: 1000px;
            position: relative;
            z-index: 1;
        }

        .contact-link {
            padding: 36px 28px;
            background: rgba(255, 255, 255, 0.07);
            border: 1px solid rgba(0, 212, 255, 0.25);
            border-radius: 12px;
            backdrop-filter: blur(20px);
            transition: all 0.5s cubic-bezier(0.23, 1, 0.320, 1);
            text-decoration: none;
            color: white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .contact-link:hover {
            background: rgba(0, 212, 255, 0.15);
            border-color: var(--accent);
            transform: translateY(-8px);
            box-shadow: 0 16px 40px rgba(0, 212, 255, 0.2);
        }

        .contact-link-icon {
            font-size: 2.2rem;
            margin-bottom: 12px;
            opacity: 0.9;
        }

        .contact-link-text {
            font-weight: 600;
            font-size: 1rem;
            letter-spacing: 0.3px;
        }

        .contact-link-value {
            font-size: 0.9rem;
            color: #CBD5E1;
            margin-top: 6px;
            font-weight: 400;
        }

        /* Footer */
        footer {
            background: var(--primary);
            color: #94A3B8;
            text-align: center;
            padding: 35px 20px;
            font-size: 0.9rem;
            letter-spacing: 0.3px;
            border-top: 1px solid rgba(14, 165, 233, 0.1);
        }

        /* Back to Top */
        .back-to-top {
            position: fixed;
            bottom: 35px;
            right: 35px;
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, var(--accent) 0%, var(--accent-dark) 100%);
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            transition: all 0.3s ease;
            z-index: 999;
            box-shadow: 0 8px 20px rgba(14, 165, 233, 0.3);
        }

        .back-to-top:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 28px rgba(14, 165, 233, 0.4);
        }

        .back-to-top.show {
            display: flex;
        }

        /* Responsive */
        @media (max-width: 1024px) {
            .hero h1 {
                font-size: 3.2rem;
            }

            section {
                padding: 70px 20px;
            }
        }

        @media (max-width: 768px) {
            section {
                padding: 60px 20px;
            }

            .section-title {
                font-size: 2.2rem;
            }

            .hero {
                padding: 70px 20px;
            }

            .hero-content {
                grid-template-columns: 1fr;
                gap: 40px;
            }

            .hero-image-section {
                order: -1;
            }

            .hero h1 {
                font-size: 2.5rem;
            }

            .hero .title {
                font-size: 1.2rem;
            }

            .hero p {
                font-size: 1rem;
            }

            .profile-picture-container {
                width: 240px;
                height: 240px;
            }

            .profile-ring {
                width: 260px;
                height: 260px;
            }

            .exp-header {
                flex-direction: column;
            }

            .exp-meta {
                white-space: normal;
                margin-top: 10px;
            }

            .about-text h3 {
                font-size: 1.5rem;
            }

            .skill-category {
                padding: 25px;
            }

            .contact-links {
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                gap: 20px;
            }

            .contact-link {
                padding: 25px;
            }
        }

        @media (max-width: 480px) {
            .hero h1 {
                font-size: 2rem;
            }

            .section-title {
                font-size: 1.8rem;
            }

            .nav-logo {
                font-size: 1.1rem;
            }

            section {
                padding: 50px 15px;
            }

            .hero-meta {
                gap: 12px;
                font-size: 0.9rem;
            }

            .meta-item {
                padding: 8px 12px;
            }

            .profile-picture-container {
                width: 200px;
                height: 200px;
            }

            .profile-ring {
                width: 220px;
                height: 220px;
            }

            .skills-grid {
                grid-template-columns: 1fr;
            }

            .contact-links {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <div class="nav-logo">AN</div>
            <ul class="nav-links">
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-content">
            <div class="hero-image-section">
                <div class="profile-ring"></div>
                <div class="profile-picture-container">
                    <img src="https://github.com/Areeba79/portfolio/blob/main/IMG_20250724_145901.jpg?raw=true" alt="Ariba Naeem Profile Picture">
                </div>
            </div>
            <div class="hero-text-section">
                <h1>Ariba Naeem</h1>
                <p class="title">Bioinformatician | Computational Biologist</p>
                <p>Bridging computational science and molecular biology to solve complex genomic challenges through NGS analysis, machine learning, and bioinformatics workflow development.</p>
                <div class="achievement-badge">AIR 1 - CUET-PG 2024 (Nanosciences)</div>
                <div class="hero-meta">
                    <div class="meta-item">New Delhi, India</div>
                    <div class="meta-item">M.Sc Completed - JNU</div>
                    <div class="meta-item">Python • R • Bioinformatics</div>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2 class="section-title">About</h2>
        <div class="about-content">
            <div class="about-text">
                <h3>Computational Expert in Genomics</h3>
                <p>I'm a bioinformatician with a passion for transforming raw genomic data into meaningful biological insights. My journey spans NGS data analysis, genome assembly, protein language models, and machine learning applications in genomics.</p>
                <p>With a strong foundation in Python, R, and Linux, I've built reproducible bioinformatics pipelines and worked with industry-standard tools to process and interpret large-scale genomic datasets. My research focuses on protein language models and their biological validation.</p>
            </div>
            <div class="about-highlights">
                <div class="highlight-item">
                    <strong>Research Focus:</strong> Protein Language Models, NGS Analysis, Genomics, Immunoinformatics
                </div>
                <div class="highlight-item">
                    <strong>Current Role:</strong> Bioinformatician & Computational Biologist
                </div>
                <div class="highlight-item">
                    <strong>Specialization:</strong> Bioinformatics with Deep Learning & AI applications
                </div>
                <div class="highlight-item">
                    <strong>Location:</strong> New Delhi, India | Currently: Hybrid (Remote + Lab work)
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills">
        <h2 class="section-title">Technical Skills</h2>
        <div class="skills-grid">
            <div class="skill-category">
                <h4>Programming & Data Science</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">R</span>
                    <span class="skill-tag">Linux/Bash</span>
                    <span class="skill-tag">SQL</span>
                    <span class="skill-tag">Pandas</span>
                    <span class="skill-tag">NumPy</span>
                    <span class="skill-tag">SciPy</span>
                    <span class="skill-tag">Scikit-learn</span>
                </div>
            </div>

            <div class="skill-category">
                <h4>NGS & Genomics Tools</h4>
                <div class="skill-tags">
                    <span class="skill-tag">FastQC</span>
                    <span class="skill-tag">Trimmomatic</span>
                    <span class="skill-tag">SPAdes</span>
                    <span class="skill-tag">QUAST</span>
                    <span class="skill-tag">Prokka</span>
                    <span class="skill-tag">BLAST</span>
                    <span class="skill-tag">SAMtools</span>
                    <span class="skill-tag">Nextflow</span>
                    <span class="skill-tag">Snakemake</span>
                </div>
            </div>

            <div class="skill-category">
                <h4>Bioinformatics Analysis</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Sequence Alignment</span>
                    <span class="skill-tag">Phylogenetics</span>
                    <span class="skill-tag">RNA-seq</span>
                    <span class="skill-tag">ProtBERT</span>
                    <span class="skill-tag">ESM-2</span>
                    <span class="skill-tag">Comparative Genomics</span>
                </div>
            </div>

            <div class="skill-category">
                <h4>AI & Machine Learning</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Transformers</span>
                    <span class="skill-tag">PyTorch</span>
                    <span class="skill-tag">Deep Learning</span>
                    <span class="skill-tag">NLP</span>
                    <span class="skill-tag">t-SNE</span>
                    <span class="skill-tag">UMAP</span>
                </div>
            </div>

            <div class="skill-category">
                <h4>Computational Biology</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Molecular Modeling</span>
                    <span class="skill-tag">GROMACS</span>
                    <span class="skill-tag">Molecular Dynamics</span>
                    <span class="skill-tag">PyMOL</span>
                    <span class="skill-tag">Drug Discovery</span>
                </div>
            </div>

            <div class="skill-category">
                <h4>Tools & Platforms</h4>
                <div class="skill-tags">
                    <span class="skill-tag">Git/GitHub</span>
                    <span class="skill-tag">Docker</span>
                    <span class="skill-tag">HPC Clusters</span>
                    <span class="skill-tag">GPU Computing</span>
                    <span class="skill-tag">Jupyter</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience">
        <h2 class="section-title">Research Experience</h2>
        <div class="experience-container">
            <div class="experience-item">
                <div class="exp-header">
                    <h4>Research Intern - ITAN Lab</h4>
                    <span class="exp-meta">Mount Sinai, NY | 2024</span>
                </div>
                <p class="exp-description"><strong>Prof. Yuval Itan, Icahn School of Medicine at Mount Sinai</strong></p>
                <ul class="exp-points">
                    <li>Built fine-tuning pipelines for domain-specific language models (PubMedBERT) to classify disease-associated variants from biomedical literature</li>
                    <li>Integrated LLM capabilities with machine learning for variant effect prediction</li>
                    <li>Developed innovative approaches at the intersection of NLP and genomics</li>
                </ul>
            </div>

            <div class="experience-item">
                <div class="exp-header">
                    <h4>Master's Dissertation</h4>
                    <span class="exp-meta">Jawaharlal Nehru University | 2024-2026</span>
                </div>
                <p class="exp-description"><strong>Biological validation study of Protein Language Models (ProtBERT, ESM-2, ProtT5)</strong></p>
                <ul class="exp-points">
                    <li>Comprehensive evaluation of protein foundation models to investigate their ability to capture biologically meaningful information</li>
                    <li>Developed scalable Python-based pipeline for large-scale protein sequence analysis</li>
                    <li>Designed deep learning models to understand relationships between various protein representations</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects">
        <h2 class="section-title">Key Projects</h2>
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-number">1</div>
                <h4>E. coli Genome Assembly & Annotation</h4>
                <p>Complete NGS workflow for genome analysis. Processed SRA data through quality control, trimming, assembly, and annotation. Generated 85 contigs, 4.55 Mb genome size with 4,251 CDS genes using FastQC, Trimmomatic, SPAdes, and Prokka.</p>
            </div>

            <div class="project-card">
                <div class="project-number">2</div>
                <h4>HLA Polymorphism & Peptide Binding</h4>
                <p>Computational immunoinformatics analysis of ~9,000 HLA-A alleles from IPD-IMGT/HLA database. Performed MSA on 300 alleles, identified 60% polymorphic amino-acid positions in antigen-binding regions using Clustal Omega and phylogenetic analysis.</p>
            </div>

            <div class="project-card">
                <div class="project-number">3</div>
                <h4>RNA-seq & Transcriptome Assembly</h4>
                <p>Comprehensive RNA-seq analysis of E. coli under different conditions. Implemented reference-based and de novo assembly approaches. Performed differential gene expression analysis and miRNA identification in Drosophila.</p>
            </div>

            <div class="project-card">
                <div class="project-number">4</div>
                <h4>Molecular Dynamics Simulations</h4>
                <p>Full molecular dynamics simulations of Trp-cage miniprotein using GROMACS to analyze folding pathways and structural stability. Investigated protein dynamics and free energy landscapes.</p>
            </div>

            <div class="project-card">
                <div class="project-number">5</div>
                <h4>Computational Drug Discovery</h4>
                <p>Virtual screening with AutoDock to identify potential acetylcholinesterase (AChE) inhibitors. Structure-based drug design and molecular docking studies for therapeutic candidate identification.</p>
            </div>

            <div class="project-card">
                <div class="project-number">6</div>
                <h4>Genomic Pattern Identification</h4>
                <p>Unsupervised K-Means clustering analysis to identify genomic patterns in species' nucleotide sequences. Machine learning approach to understand evolutionary relationships and sequence homology.</p>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education">
        <h2 class="section-title">Education</h2>
        <div class="education-container">
            <div class="education-item">
                <div class="edu-degree">M.Sc, Computational and Integrative Sciences</div>
                <div class="edu-school">Jawaharlal Nehru University, New Delhi</div>
                <div class="edu-date">2024 – 2026</div>
                <div class="edu-cgpa">CGPA: 8.00</div>
                <p style="margin-top: 12px; color: var(--text-light); font-size: 0.95rem;">Specialization: Bioinformatics | Focus: Protein Language Models & Machine Learning</p>
            </div>

            <div class="education-item">
                <div class="edu-degree">B.Sc (Hons), Zoology</div>
                <div class="edu-school">Deshbandhu College, University of Delhi</div>
                <div class="edu-date">2021 – 2024</div>
                <div class="edu-cgpa">CGPA: 7.58</div>
                <p style="margin-top: 12px; color: var(--text-light); font-size: 0.95rem;">Foundation in molecular biology and experimental techniques</p>
            </div>
        </div>
    </section>

    <!-- Awards Section -->
    <section id="awards">
        <h2 class="section-title">Honors & Awards</h2>
        <div class="awards-list">
            <div class="award-item">
                <div class="award-icon">★</div>
                <div class="award-text">
                    <h4>All India Rank 1 (AIR 1)</h4>
                    <p>CUET-PG 2024 – Nanosciences. Top performer in National Entrance Examination</p>
                </div>
            </div>
            <div class="award-item">
                <div class="award-icon">◆</div>
                <div class="award-text">
                    <h4>Organizer – National Symposium</h4>
                    <p>National Symposium on Start-ups in Biological Sciences, 2024</p>
                </div>
            </div>
            <div class="award-item">
                <div class="award-icon">◇</div>
                <div class="award-text">
                    <h4>Workshop Lead – Google Earth Engine</h4>
                    <p>GEE-Quiz Competition & Workshop on Google Earth Engine, 2022 • Organized & Led hands-on training</p>
                </div>
            </div>
            <div class="award-item">
                <div class="award-icon">■</div>
                <div class="award-text">
                    <h4>Student Coordinator – ICNPHH</h4>
                    <p>International Conference on Natural Products and Human Health, 2022 • University of Delhi</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact-section">
        <h2 class="section-title">Get In Touch</h2>
        <p>Let's connect and collaborate on exciting bioinformatics projects</p>
        <div class="contact-links">
            <a href="mailto:areebasaifi6844@gmail.com" class="contact-link">
                <div class="contact-link-icon">✉</div>
                <div class="contact-link-text">Email</div>
                <div class="contact-link-value">areebasaifi6844@gmail.com</div>
            </a>
            <a href="tel:+918799707921" class="contact-link">
                <div class="contact-link-icon">☎</div>
                <div class="contact-link-text">Phone</div>
                <div class="contact-link-value">+91-8799707921</div>
            </a>
            <a href="https://www.linkedin.com/in/ariba-naeem-69a100204/" target="_blank" class="contact-link">
                <div class="contact-link-icon">in</div>
                <div class="contact-link-text">LinkedIn</div>
                <div class="contact-link-value">Connect with me</div>
            </a>
            <a href="https://github.com/Areeba79" target="_blank" class="contact-link">
                <div class="contact-link-icon">&lt;/&gt;</div>
                <div class="contact-link-text">GitHub</div>
                <div class="contact-link-value">View my code</div>
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Ariba Naeem. All rights reserved.</p>
    </footer>

    <!-- Back to Top Button -->
    <button class="back-to-top" onclick="scrollToTop()">↑</button>

    <script>
        // Back to Top Button
        window.addEventListener('scroll', function() {
            const backToTopBtn = document.querySelector('.back-to-top');
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Smooth scroll for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>
</body>
</html>
"""

# Render the HTML using Streamlit Components
# Height is set high enough (5000) to ensure your whole portfolio is visible without a double scrollbar.
components.html(portfolio_html, height=5000, scrolling=True)
