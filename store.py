from fasthtml.common import *
from monsterui.all import *

# Headers avec le thème bleu et la police Montserrat
hdrs = (
    Theme.blue.headers(),
    Link(href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap", rel="stylesheet"),
    Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css")  # FontAwesome pour les icônes
)

app, rt = fast_app(hdrs=hdrs)


@rt
def index():
    animate_css = Link(rel="stylesheet",
                       href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css")

    favicon = Link(rel="icon", href="/favicon.ico", type="image/x-icon")

    custom_css = """
        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        @keyframes blink {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .animate-on-scroll {
            opacity: 0;
            visibility: hidden;
        }

        .animate__animated {
            opacity: 1;
            visibility: visible;
        }

        html {
            overflow-x: hidden;
            margin: 0;
            padding: 0;
        }

        body {
            overflow-x: hidden;
            background-color: #0f172a !important;
            color: #f8fafc !important;
            font-family: 'Montserrat', sans-serif;
            background-image: 
                linear-gradient(rgba(148, 163, 184, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(148, 163, 184, 0.1) 1px, transparent 1px) !important;
            background-size: 100% 24px, 24px 100% !important;
            background-position: 0 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            padding-top: 64px;
            margin-bottom: 0 !important;
        }

        .splash-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #0f172a;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            transition: opacity 0.5s ease-out;
        }

        .splash-logo {
            width: 180px;
            height: auto;
            margin-bottom: 2rem;
            animation: pulse 2s infinite;
        }

        .splash-greeting {
            font-size: 2rem;
            color: white;
            font-weight: bold;
            height: 3rem;
            text-align: center;
        }

        .splash-loading {
            margin-top: 2rem;
            width: 100px;
            height: 3px;
            background-color: rgba(59, 130, 246, 0.2);
            border-radius: 3px;
            overflow: hidden;
            position: relative;
        }

        .loading-progress {
            position: absolute;
            top: 0;
            left: 0;
            height: 100%;
            width: 0;
            background-color: #3b82f6;
            transition: width 1.5s ease-in-out;
        }

        .fixed-navbar {
            position: fixed !important;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 1000;
            transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out;
            padding: 0 1.5rem;
        }

        .fixed-navbar a:hover {
            transform: scale(1.05);
            transition: transform 0.2s ease-in-out;
        }

        .nav-scrolled {
            background-color: rgba(15, 23, 42, 0.95) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        .nav-logo {
            height: 40px;
            width: auto;
        }

        .hamburger-button {
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 40px;
            height: 40px;
            padding: 5px;
            border-radius: 5px;
            border: none;
            background-color: transparent;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        @media (max-width: 767px) {
            .hamburger-button {
                display: flex;
            }
        }

        .hamburger-button:hover {
            background-color: rgba(59, 130, 246, 0.2);
        }

        .hamburger-line {
            width: 24px;
            height: 2px;
            background-color: white;
            margin: 3px 0;
            transition: all 0.3s ease;
        }

        .hero-bg {
            position: relative;
            min-height: 100vh;
            width: 100vw;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            margin-top: 0 !important;
            padding-top: 0 !important;
            overflow: hidden;
        }

        .hero-bg::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('image/background.png');
            background-size: cover;
            background-position: top center;
            background-repeat: no-repeat;
            z-index: 0;
            filter: saturate(0.8) brightness(0.9);
            background-color: rgba(15, 23, 42, 0.7);
            background-blend-mode: overlay;
        }

        @media (max-width: 768px) {
            .hero-bg::before {
                background-position: top center;
            }
        }

        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: flex-end;
            width: 100%;
            box-sizing: border-box;
        }

        .hero-bg .vertical-logo {
            position: absolute;
            top: 1rem;
            left: 0.5rem;
            writing-mode: vertical-rl;
            -webkit-writing-mode: vertical-rl;
            text-orientation: mixed;
            white-space: nowrap;
            z-index: 10;
            font-size: 2.5rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1;
            display: block;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        @media (max-width: 767px) {
            .hero-bg .vertical-logo {
                font-size: 1.25rem;
                left: 0.6rem;
                top: 1rem;
                writing-mode: vertical-rl;
                -webkit-writing-mode: vertical-rl;
                text-orientation: mixed;
            }
        }

        .hero-title {
            position: relative;
            text-align: right;
            z-index: 10;
            margin-right: 2rem;
        }

        .contact-button {
            position: absolute;
            bottom: 2rem;
            right: 2rem;
            z-index: 10;
            animation: float 3s ease-in-out infinite, blink 3s infinite;
            background: linear-gradient(135deg, #facc15, #f59e0b);
            transition: background 0.3s ease;
        }

        .contact-button:hover {
            background: linear-gradient(135deg, #fde047, #fb923c);
        }

        .whatsapp-button {
            position: absolute;
            bottom: 6rem; /* Positionné au-dessus du bouton Call */
            right: 2rem;
            z-index: 10;
            animation: float 3s ease-in-out infinite;
            background: linear-gradient(135deg, #25D366, #128C7E);
            transition: background 0.3s ease;
        }

        .whatsapp-button:hover {
            background: linear-gradient(135deg, #2ecc71, #1abc9c);
        }

        .services-section {
            position: absolute;
            bottom: 2rem;
            left: 2rem;
            z-index: 10;
            background-color: rgba(30, 41, 59, 1);
            padding: 1rem;
            border-radius: 0.5rem;
        }

        @media (max-width: 767px) {
            .hero-title {
                margin-right: 1rem;
                font-size: 2rem;
            }
            .contact-button {
                bottom: 1rem;
                right: 1rem;
            }
            .whatsapp-button {
                bottom: 4rem; /* Ajusté pour mobile */
                right: 1rem;
            }
            .services-section {
                bottom: 1rem;
                left: 1rem;
                padding: 0.5rem;
            }
        }

        .full-bleed-section {
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            overflow: hidden;
        }

        .footer-container {
            width: 100%;
            overflow: hidden;
            position: relative;
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }

        .footer-marquee-container {
            width: 100%;
            overflow: hidden;
            text-align: center;
            position: relative;
            display: flex;
            justify-content: center;
            margin-bottom: 0 !important;
            padding-bottom: 0 !important;
        }

        .footer-marquee-wrapper {
            display: inline-flex;
            position: relative;
            white-space: nowrap;
            width: auto;
        }

        .animate-marquee {
            display: inline-block;
            animation: marquee 10s linear infinite;
            white-space: nowrap;
            width: max-content;
        }

        .footer-marquee-text {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
        }

        @media (max-width: 768px) {
            .footer-marquee-text {
                font-size: 3rem !important;
            }
        }

        @media (min-width: 769px) and (max-width: 1024px) {
            .footer-marquee-text {
                font-size: 6rem !important;
            }
        }

        .project-card {
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            overflow: hidden;
            background: rgba(30, 41, 59, 0.9);
        }

        .project-card:hover {
            transform: translateY(-5px);
        }

        .project-card img {
            transition: transform 0.5s ease;
        }

        .project-card:hover img {
            transform: scale(1.03);
        }

        .project-tech-badge {
            display: inline-block;
            background-color: rgba(59, 130, 246, 0.2);
            color: #93c5fd;
            border-radius: 9999px;
            padding: 0.25rem 0.75rem;
            font-size: 0.75rem;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .contact-section {
            position: relative;
        }

        .contact-section::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 300px;
            background-image: url('./image/logo.png');
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.5;
            z-index: 0;
        }

        .contact-content {
            position: relative;
            z-index: 1;
        }

        .dark.bg-slate-900 {
            background-color: transparent !important;
        }

        .skills img {
            position: relative;
        }

        .skills img:hover::after {
            content: attr(title);
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            z-index: 10;
        }

        .language-selector {
            padding: 0.5rem;
            background-color: rgba(59, 130, 246, 0.2);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9rem;
            width: 100%;
            margin: 0.5rem 0;
        }

        .language-selector:hover {
            background-color: rgba(59, 130, 246, 0.4);
        }

        @media (max-width: 767px) {
            .language-selector {
                width: auto;
                margin: 0.5rem 1rem;
            }
        }

        .contact-button i, .whatsapp-button i {
            margin-right: 8px;
        }
    """

    custom_style = Style(custom_css + """
        </style>
        <meta name="description" content="Portfolio de Chilavert N'dah, développeur logiciel spécialisé en full-stack et open-source">
        <meta name="keywords" content="Chilavert N'dah, portfolio, développeur, full-stack, open-source, logiciel">
        <meta name="author" content="Chilavert N'dah">
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const splashScreen = document.getElementById('splash-screen');
                const loadingBar = document.getElementById('loading-progress');
                const splashGreeting = document.getElementById('splash-greeting');
                const mainContent = document.getElementById('main-content');

                if (!splashScreen || !loadingBar || !splashGreeting || !mainContent) {
                    console.error('Splash screen elements missing');
                    return;
                }

                splashScreen.style.opacity = '1';
                mainContent.style.opacity = '0';

                const greetings = [
                    "Hello", "Bonjour", "Hola", "Ciao", "Olá", 
                    "Привет", "こんにちは", "你好", "안녕하세요", 
                    "مرحبا", "नमस्ते", "Hallo", "Γειά σου", "Salve"
                ];

                let currentGreetingIndex = 0;

                function cycleGreetings() {
                    splashGreeting.textContent = greetings[currentGreetingIndex];
                    currentGreetingIndex = (currentGreetingIndex + 1) % greetings.length;
                }

                let greetingInterval = setInterval(cycleGreetings, 600);
                cycleGreetings();

                setTimeout(() => {
                    loadingBar.style.width = '100%';
                }, 100);

                setTimeout(() => {
                    splashScreen.style.opacity = '0';
                    mainContent.style.opacity = '1';
                    clearInterval(greetingInterval);
                    setTimeout(() => {
                        splashScreen.style.display = 'none';
                    }, 500);
                }, 3000);

                const navbar = document.querySelector('.fixed-navbar');
                let lastScrollY = window.scrollY;

                navbar && window.addEventListener('scroll', function() {
                    const currentScrollY = window.scrollY;
                    if (currentScrollY > lastScrollY && currentScrollY > 100) {
                        navbar.style.transform = 'translateY(-100%)';
                    } else if (currentScrollY < lastScrollY || currentScrollY <= 100) {
                        navbar.style.transform = 'translateY(0)';
                        navbar.classList.toggle('nav-scrolled', currentScrollY > 50);
                    }
                    lastScrollY = currentScrollY;
                });

                const mobileMenuButton = document.getElementById('mobile-menu-button');
                const mobileMenu = document.getElementById('mobile-menu');

                mobileMenuButton && mobileMenuButton.addEventListener('click', function() {
                    mobileMenu.classList.toggle('hidden');
                });

                const mobileMenuLinks = mobileMenu.querySelectorAll('a');
                mobileMenuLinks.forEach(link => {
                    link.addEventListener('click', function() {
                        mobileMenu.classList.add('hidden');
                    });
                });

                function createScrollAnimations() {
                    const animatedElements = document.querySelectorAll('.animate-on-scroll');

                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                const animation = entry.target.getAttribute('data-animation');
                                entry.target.classList.add('animate__animated', `animate__${animation}`);
                                observer.unobserve(entry.target);
                            }
                        });
                    }, {
                        threshold: 0.1
                    });

                    animatedElements.forEach(element => {
                        observer.observe(element);
                    });
                }

                createScrollAnimations();

                // Gestion de la traduction
                const translations = {
                    en: {
                        "Work": "Work",
                        "About": "About",
                        "GitHub": "GitHub",
                        "Think different": "Think different",
                        "Chilavert N'dah": "Chilavert N'dah",
                        "Software Developer": "Software Developer",
                        "Call": "Call",
                        "Text": "Text",
                        "Services": "Services",
                        "Web Site": "Web Site",
                        "Web App": "Web App",
                        "Mobile App": "Mobile App",
                        "Projects": "Projects",
                        "MC Agence Website": "MC Agence Website",
                        "A responsive website design for a marketing agency built with Webflow. Features modern UI/UX design principles, smooth animations, and a client-focused approach.": "A responsive website design for a marketing agency built with Webflow. Features modern UI/UX design principles, smooth animations, and a client-focused approach.",
                        "Visit Website": "Visit Website",
                        "MonsterUI Library Contribution": "MonsterUI Library Contribution",
                        "Contributed to the open-source MonsterUI library, which provides UI components for Python web applications. My pull request #30 added new features and improvements to the library.": "Contributed to the open-source MonsterUI library, which provides UI components for Python web applications. My pull request #30 added new features and improvements to the library.",
                        "View PR on GitHub": "View PR on GitHub",
                        "About Me": "About Me",
                        "I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. Outside of coding, I enjoy playing basketball, listening to music, and traveling. Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅": "I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. Outside of coding, I enjoy playing basketball, listening to music, and traveling. Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅",
                        "Resume": "Resume",
                        "Things I Can Do Without Googling... Mostly": "Things I Can Do Without Googling... Mostly",
                        "GitHub Stats & Contributions": "GitHub Stats & Contributions",
                        "Let's Connect": "Let's Connect",
                        "Feel free to reach out to me via email.": "Feel free to reach out to me via email.",
                        "Send Email": "Send Email",
                        "© 2025 Chilavert N'dah": "© 2025 Chilavert N'dah"
                    },
                    fr: {
                        "Work": "Travaux",
                        "About": "À propos",
                        "GitHub": "GitHub",
                        "Think different": "Pensez différemment",
                        "Chilavert N'dah": "Chilavert N'dah",
                        "Software Developer": "Développeur Logiciel",
                        "Call": "Appeler",
                        "Text": "Texte",
                        "Services": "Services",
                        "Web Site": "Site Web",
                        "Web App": "Application Web",
                        "Mobile App": "Application Mobile",
                        "Projects": "Projets",
                        "MC Agence Website": "Site Web MC Agence",
                        "A responsive website design for a marketing agency built with Webflow. Features modern UI/UX design principles, smooth animations, and a client-focused approach.": "Un design de site web responsive pour une agence de marketing construit avec Webflow. Inclut des principes de design UI/UX modernes, des animations fluides et une approche centrée sur le client.",
                        "Visit Website": "Visiter le site",
                        "MonsterUI Library Contribution": "Contribution à la bibliothèque MonsterUI",
                        "Contributed to the open-source MonsterUI library, which provides UI components for Python web applications. My pull request #30 added new features and improvements to the library.": "J'ai contribué à la bibliothèque open-source MonsterUI, qui fournit des composants UI pour les applications web Python. Ma pull request #30 a ajouté de nouvelles fonctionnalités et améliorations à la bibliothèque.",
                        "View PR on GitHub": "Voir la PR sur GitHub",
                        "About Me": "À propos de moi",
                        "I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. Outside of coding, I enjoy playing basketball, listening to music, and traveling. Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅": "Je suis diplômé en informatique de l'UCAO à Cotonou. Actuellement, je travaille comme développeur logiciel freelance et contribue activement à divers projets open-source pour améliorer mes compétences en développement full-stack et technologies cloud. En dehors du codage, j'aime jouer au basketball, écouter de la musique et voyager. Anecdote amusante : j'ai passé 3 heures à déboguer pour réaliser que j'avais oublié de sauvegarder le fichier. 😅",
                        "Resume": "CV",
                        "Things I Can Do Without Googling... Mostly": "Choses que je peux faire sans Googler... en grande partie",
                        "GitHub Stats & Contributions": "Statistiques et contributions GitHub",
                        "Let's Connect": "Connectons-nous",
                        "Feel free to reach out to me via email.": "N'hésitez pas à me contacter par email.",
                        "Send Email": "Envoyer un email",
                        "© 2025 Chilavert N'dah": "© 2025 Chilavert N'dah"
                    }
                };

                let currentLang = 'en';

                function updateLanguage(lang) {
                    currentLang = lang;
                    document.querySelectorAll('[data-translate]').forEach(element => {
                        const key = element.getAttribute('data-translate');
                        if (translations[lang][key]) {
                            element.textContent = translations[lang][key];
                        }
                    });
                }

                const langSelector = document.getElementById('language-selector');
                const mobileLangSelector = document.getElementById('mobile-language-selector');

                langSelector.addEventListener('change', function() {
                    updateLanguage(this.value);
                    mobileLangSelector.value = this.value; // Synchroniser avec le mobile
                });

                mobileLangSelector.addEventListener('change', function() {
                    updateLanguage(this.value);
                    langSelector.value = this.value; // Synchroniser avec le desktop
                });

                // Initialisation en anglais
                updateLanguage('en');
            });
        </script>
        <style>
    """)

    splash_screen = Div(
        Img(src="./image/logo.png", cls="splash-logo", alt="Logo", loading="lazy"),
        Div(id="splash-greeting", cls="splash-greeting"),
        Div(Div(id="loading-progress", cls="loading-progress"), cls="splash-loading"),
        id="splash-screen",
        cls="splash-screen"
    )

    nav = Div(
        Container(
            DivFullySpaced(
                A(
                    Img(src="./image/logo.png", cls="nav-logo", alt="Logo", loading="lazy"),
                    href="#",
                    cls="flex items-center"
                ),
                Div(
                    DivHStacked(
                        A("Work", href="#work", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20", **{"data-translate": "Work"}),
                        A("About", href="#about", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20", **{"data-translate": "About"}),
                        A("GitHub", href="https://github.com/99ch", target="_blank", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20", **{"data-translate": "GitHub"}),
                        Select(
                            Option("English", value="en"),
                            Option("Français", value="fr"),
                            id="language-selector",
                            cls="language-selector"
                        ),
                        cls="gap-2 items-center"
                    ),
                    cls="hidden md:flex"
                ),
                Button(
                    Div(
                        Span(cls="hamburger-line"),
                        Span(cls="hamburger-line"),
                        Span(cls="hamburger-line"),
                        cls="flex flex-col justify-center items-center"
                    ),
                    cls="hamburger-button focus:outline-none",
                    id="mobile-menu-button",
                    **{"aria-label": "Toggle mobile menu"}
                ),
                cls="py-4 flex items-center justify-between"
            ),
            cls="max-w-7xl mx-auto px-4"
        ),
        Div(
            Div(
                A("Work", href="#work", cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3 border-b border-blue-500/20", **{"data-translate": "Work"}),
                A("About", href="#about", cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3 border-b border-blue-500/20", **{"data-translate": "About"}),
                A("GitHub", href="https://github.com/99ch", target="_blank", cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3 border-b border-blue-500/20", **{"data-translate": "GitHub"}),
                Select(
                    Option("English", value="en"),
                    Option("Français", value="fr"),
                    id="mobile-language-selector",
                    cls="language-selector"
                ),
                cls="py-2"
            ),
            cls="hidden bg-slate-900 md:hidden",
            id="mobile-menu"
        ),
        cls="fixed-navbar"
    )

    hero = Section(
        Span("Think different", cls="vertical-logo animate-on-scroll", **{"data-translate": "Think different", "data-animation": "fadeInLeft"}),
        Div(
            Div(
                H1("Chilavert N'dah", cls="text-5xl font-bold text-white animate-on-scroll", **{"data-translate": "Chilavert N'dah", "data-animation": "fadeInDown"}),
                P("Software Developer", cls="text-xl text-blue-100 animate-on-scroll", **{"data-translate": "Software Developer", "data-animation": "fadeInUp"}),
                cls="hero-title"
            ),
            A(
                I(cls="fas fa-phone"),  # Icône téléphone
                Span("Call", **{"data-translate": "Call"}),
                href="tel:+2290144432820",
                cls="contact-button bg-yellow-400 text-black px-6 py-3 rounded-lg hover:bg-yellow-500 transition-colors animate-on-scroll",
                **{"data-animation": "fadeIn"}
            ),
            A(
                I(cls="fab fa-whatsapp"),  # Icône WhatsApp
                Span("Text", **{"data-translate": "Text"}),
                href="https://wa.me/+2290144432820",
                cls="whatsapp-button text-white px-6 py-3 rounded-lg hover:bg-green-600 transition-colors animate-on-scroll",
                target="_blank",
                **{"data-animation": "fadeIn"}
            ),
            Div(
                H3("Services", cls="text-white text-lg mb-2 animate-on-scroll", **{"data-translate": "Services", "data-animation": "fadeInLeft"}),
                Ul(
                    Li("Web Site", cls="text-white hover:text-blue-300 transition-colors animate-on-scroll", **{"data-translate": "Web Site", "data-animation": "fadeInLeft"}),
                    Li("Web Application", cls="text-white hover:text-blue-300 transition-colors animate-on-scroll", **{"data-translate": "Web Application", "data-animation": "fadeInLeft"}),
                    Li("Mobile Application", cls="text-white hover:text-blue-300 transition-colors animate-on-scroll", **{"data-translate": "Mobile Application", "data-animation": "fadeInLeft"}),
                    cls="list-none"
                ),
                cls="services-section"
            ),
            cls="hero-content"
        ),
        cls="hero-bg",
        container=False
    )

    projects = Section(
        Container(
            DivCentered(
                H2("Projects", cls="text-4xl font-semibold mb-12 animate-on-scroll text-slate-100", **{"data-translate": "Projects", "data-animation": "fadeIn"}),
                Grid(
                    Card(
                        Div(
                            Img(src="./image/mc-agence.png", cls="w-full h-auto transition-transform", loading="lazy"),
                            cls="overflow-hidden"
                        ),
                        CardBody(
                            H3("MC Agence Website", cls="text-2xl font-medium mb-2 text-slate-100", **{"data-translate": "MC Agence Website"}),
                            P("A responsive website design for a marketing agency built with Webflow. Features modern UI/UX design principles, smooth animations, and a client-focused approach.", cls="text-slate-400 text-sm mb-4", **{"data-translate": "A responsive website design for a marketing agency built with Webflow. Features modern UI/UX design principles, smooth animations, and a client-focused approach."}),
                            Div(
                                Span("Webflow", cls="project-tech-badge"),
                                Span("Responsive Design", cls="project-tech-badge"),
                                Span("UI/UX", cls="project-tech-badge"),
                                cls="flex flex-wrap mt-2"
                            ),
                            A("Visit Website", href="https://mc-agence.webflow.io", cls="inline-block bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg mt-4 transition-colors", target="_blank", **{"data-translate": "Visit Website"}),
                            cls="flex flex-col"
                        ),
                        cls="project-card hover:shadow-2xl animate-on-scroll bg-slate-800/50 backdrop-blur-sm border-0",
                        **{"data-animation": "fadeInLeft"}
                    ),
                    Card(
                        Div(
                            Img(src="./image/monsterui.png", cls="w-full h-auto transition-transform", loading="lazy"),
                            cls="overflow-hidden"
                        ),
                        CardBody(
                            H3("MonsterUI Library Contribution", cls="text-2xl font-medium mb-2 text-slate-100", **{"data-translate": "MonsterUI Library Contribution"}),
                            P("Contributed to the open-source MonsterUI library, which provides UI components for Python web applications. My pull request #30 added new features and improvements to the library.", cls="text-slate-400 text-sm mb-4", **{"data-translate": "Contributed to the open-source MonsterUI library, which provides UI components for Python web applications. My pull request #30 added new features and improvements to the library."}),
                            Div(
                                Span("Python", cls="project-tech-badge"),
                                Span("Open Source", cls="project-tech-badge"),
                                Span("UI Components", cls="project-tech-badge"),
                                cls="flex flex-wrap mt-2"
                            ),
                            A("View PR on GitHub", href="https://github.com/AnswerDotAI/MonsterUI/pull/30", cls="inline-block bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg mt-4 transition-colors", target="_blank", **{"data-translate": "View PR on GitHub"}),
                            cls="flex flex-col"
                        ),
                        cls="project-card hover:shadow-2xl animate-on-scroll bg-slate-800/50 backdrop-blur-sm border-0",
                        **{"data-animation": "fadeInRight"}
                    ),
                    cls="grid grid-cols-1 md:grid-cols-2 gap-8"
                ),
                cls="py-32",
                id="work"
            )
        )
    )

    about = Section(
        Container(
            DivCentered(
                H2("About Me", cls="text-4xl font-semibold mb-12 animate-on-scroll text-slate-100", **{"data-translate": "About Me", "data-animation": "fadeIn"}),
                Grid(
                    Div(
                        Img(src="image/full_profil.png", cls="w-full h-auto rounded-2xl shadow-2xl border-4 border-slate-700/20 animate-on-scroll", style="max-width: 500px;", loading="lazy", **{"data-animation": "fadeInLeft"}),
                        cls="flex items-center justify-center"
                    ),
                    Div(
                        P("""
                            I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and 
                            actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. 
                            Outside of coding, I enjoy playing basketball, listening to music, and traveling. 
                            Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅
                        """, cls="text-xl max-w-2xl leading-relaxed text-slate-300 animate-on-scroll mb-12", **{"data-translate": "I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. Outside of coding, I enjoy playing basketball, listening to music, and traveling. Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅", "data-animation": "fadeInRight"}),
                        DivHStacked(
                            A("Resume", href="https://drive.google.com/drive/folders/1lI8KVnN6aZ6uaj7JpwG91GhEB3we0iIX?usp=drive_link", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate-on-scroll", target="_blank", **{"data-translate": "Resume", "data-animation": "fadeInLeft"}),
                        ),
                        cls="flex flex-col items-start"
                    ),
                    cls="grid grid-cols-1 md:grid-cols-2 gap-12 items-center"
                ),
                cls="py-32",
                id="about"
            )
        )
    )

    skills = Section(
        Container(
            DivCentered(
                H2("Things I Can Do Without Googling... Mostly", cls="text-4xl font-semibold mb-12 animate-on-scroll", **{"data-translate": "Things I Can Do Without Googling... Mostly", "data-animation": "fadeIn"}),
                Div(
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Python", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Django", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="C++", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="HTML", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="CSS", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Bootstrap", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="JavaScript", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/firebase/firebase.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Firebase", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/dart/dart.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Dart", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flutter/flutter.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Flutter", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/latex/latex.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="LaTeX", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="Git", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/tensorflow/tensorflow.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="TensorFlow", loading="lazy", **{"data-animation": "fadeIn"}),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate-on-scroll", title="VS Code", loading="lazy", **{"data-animation": "fadeIn"}),
                    cls="flex flex-wrap justify-center gap-4 skills"
                ),
                cls="py-32",
                id="skills"
            )
        )
    )

    github_stats = Section(
        Container(
            DivCentered(
                H2("GitHub Stats & Contributions", cls="text-4xl font-semibold mb-12 animate-on-scroll text-slate-100", **{"data-translate": "GitHub Stats & Contributions", "data-animation": "fadeIn"}),
                Div(
                    Img(src="https://github-readme-streak-stats.herokuapp.com?user=99ch&theme=github-dark-blue&hide_border=True&background=0f172a", cls="w-full mb-8 rounded-lg animate-on-scroll", loading="lazy", **{"data-animation": "fadeInDown"}),
                    Grid(
                        Img(src="https://github-readme-stats.vercel.app/api/top-langs/?username=99ch&layout=compact&theme=github_dark&hide_border=True&langs_count=10&bg_color=0f172a&height=300", cls="rounded-lg animate-on-scroll", loading="lazy", **{"data-animation": "fadeInRight"}),
                        Div(
                            Img(src="https://github-readme-stats.vercel.app/api?username=99ch&show_icons=true&theme=github_dark&hide_border=True&bg_color=0f172a&height=300", cls="w-full h-full rounded-lg animate-on-scroll object-contain", loading="lazy", **{"data-animation": "fadeInRight"}),
                            cls="h-full"
                        ),
                        cls="grid grid-cols-1 md:grid-cols-2 gap-8 items-stretch h-full"
                    ),
                    cls="github-triangle-layout flex flex-col gap-12 h-full"
                ),
                cls="py-32",
                id="github"
            )
        )
    )

    contact = Section(
        Container(
            DivCentered(
                H2("Let's Connect", cls="text-4xl font-semibold mb-12 animate-on-scroll", **{"data-translate": "Let's Connect", "data-animation": "fadeIn"}),
                P("Feel free to reach out to me via email.", cls="text-xl text-center mb-8 animate-on-scroll", **{"data-translate": "Feel free to reach out to me via email.", "data-animation": "fadeInUp"}),
                A("Send Email", href="mailto:chilavertndah99@gmail.com", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate-on-scroll", **{"data-translate": "Send Email", "data-animation": "fadeIn"}),
                cls="py-32 contact-content",
                id="contact"
            )
        ),
        cls="contact-section"
    )

    footer = Section(
        Div(
            Div(
                DivCentered(
                    Divider(cls="mb-12 border-blue-500/20"),
                    DivHStacked(
                        A(Img(src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg", cls="h-8 w-8 animate__animated animate__bounce", loading="lazy"), href="https://www.linkedin.com/in/chilavert-n-dah-ab5779272/"),
                        cls="gap-4 mb-6 justify-center"
                    ),
                    Div(
                        Div(
                            P("© 2025 Chilavert N'dah", cls="footer-marquee-text text-9xl font-bold whitespace-nowrap inline-block animate-marquee", **{"data-translate": "© 2025 Chilavert N'dah"}),
                            P("© 2025 Chilavert N'dah", cls="footer-marquee-text text-9xl font-bold whitespace-nowrap inline-block animate-marquee", **{"data-translate": "© 2025 Chilavert N'dah"}),
                            cls="footer-marquee-wrapper"
                        ),
                        cls="footer-marquee-container w-screen"
                    ),
                    cls="py-0"
                ),
                cls="w-full"
            ),
            cls="footer-container w-full"
        ),
        cls="py-0 full-bleed-section",
        container=False
    )

    main_content = Div(
        splash_screen,
        Div(
            nav,
            hero,
            projects,
            about,
            skills,
            github_stats,
            contact,
            footer,
            cls="dark bg-slate-900 text-slate-100",
            id="main-content",
            style="opacity: 0; transition: opacity 1s ease-in-out;"
        )
    )

    return Titled(
        "",  # Titre optimisé pour SEO
        animate_css,
        favicon,
        custom_style,
        main_content
    )


if __name__ == "__main__":
    from starlette.testclient import TestClient
    client = TestClient(app)
    response = client.get('/')
    with open('index.html', 'w') as f:
        f.write(response.text)