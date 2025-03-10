from fasthtml.common import *
from monsterui.all import *

# Use blue theme for a professional look
hdrs = (
    Theme.blue.headers()
)

app, rt = fast_app(hdrs=hdrs)


@rt
def index():
    # CSS animations
    animate_css = Link(rel="stylesheet",
                       href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css")

    # Custom CSS
    custom_css = """
        @keyframes marquee {
            0% { transform: translateX(0%); }
            100% { transform: translateX(-50%); }
        }

        html {
            overflow-x: hidden;
        }

        .animate-marquee {
            display: inline-block;
            animation: marquee 10s linear infinite;
            white-space: nowrap;
            width: max-content;
        }

        /* Effet de papier ligné */
        body {
            overflow-x: hidden; /* Added to prevent horizontal scroll */
            background-color: #0f172a !important;
            color: #f8fafc !important;
            background-image: 
                linear-gradient(rgba(148, 163, 184, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(148, 163, 184, 0.1) 1px, transparent 1px) !important;
            background-size: 100% 24px, 24px 100% !important;
            background-position: 0 0 !important;
        }

        /* Hero Section */
        .hero-bg {
            position: relative;
            min-height: 100vh;
            margin-top: -64px;
            padding-top: 64px;
            width: 100vw;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
        }

        .hero-bg::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                url('image/background.png');
            background-size: cover;
            background-position: center top;
            background-repeat: no-repeat;
            z-index: 0;
            filter: saturate(0.8) brightness(0.9);
            /* Add a dark blue overlay */
            background-color: rgba(15, 23, 42, 0.7);
            background-blend-mode: overlay;
        }

        @media (max-width: 768px) {
            .hero-bg::before {
                background-position: center top 20%; /* Ajustement mobile */
            }
        }


        .hero-content {
            position: relative;
            z-index: 1;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Transparence pour voir les rayures */
        .dark.bg-slate-900 {
            background-color: transparent !important;
        }

        /* Navbar */
        .fixed-navbar {
            position: fixed !important;
            top: 0;
            left: 0;
            right: 0;
            width: 100%;
            z-index: 1000;
            transition: transform 0.3s ease-in-out, background-color 0.3s ease-in-out;

        }

        .nav-scrolled {
            background-color: rgba(15, 23, 42, 0.95) !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        body {
            padding-top: 64px;
        }

        @media (max-width: 768px) {
            .hero-bg::before {
                background-position: 60% center;
            }

            .hero-content h1 {
                font-size: 2.5rem !important;
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

        /* Fix footer overflow */
        .footer-container {
            width: 100%;
            overflow: hidden;
            position: relative;
        }

        /* Fix marquee container */
        .footer-marquee-container {
            width: 100%;
            overflow: hidden;
            text-align: center;
            position: relative;
            display: flex;
            justify-content: center;
        }

        /* Fixed marquee wrapper */
        .footer-marquee-wrapper {
            display: inline-flex;
            position: relative;
            white-space: nowrap;
            width: auto;
        }

        /* Responsive text sizes for footer */
        @media (max-width: 768px) {
            .footer-marquee-text {
                font-size: 4rem !important; /* Smaller text on mobile */
            }
        }

        @media (min-width: 769px) and (max-width: 1024px) {
            .footer-marquee-text {
                font-size: 6rem !important; /* Medium text on tablet */
            }
        }
    """

    custom_style = Style(custom_css + """
        </style>
        <script>
            document.addEventListener('DOMContentLoaded', function() {
                const navbar = document.querySelector('.fixed-navbar');
                let lastScrollY = window.scrollY;

                navbar && window.addEventListener('scroll', function() {
                    const currentScrollY = window.scrollY;

                    if (currentScrollY > lastScrollY && currentScrollY > 100) {
                        navbar.style.transform = 'translateY(-100%)';
                    } else {
                        navbar.style.transform = 'translateY(0)';
                        navbar.classList.toggle('nav-scrolled', currentScrollY > 50);
                    }
                    lastScrollY = currentScrollY;
                });

                // Mobile menu toggle
                const mobileMenuButton = document.getElementById('mobile-menu-button');
                const mobileMenu = document.getElementById('mobile-menu');

                mobileMenuButton && mobileMenuButton.addEventListener('click', function() {
                    mobileMenu.classList.toggle('hidden');
                });

                // Close mobile menu when clicking on a link
                const mobileMenuLinks = mobileMenu.querySelectorAll('a');
                mobileMenuLinks.forEach(link => {
                    link.addEventListener('click', function() {
                        mobileMenu.classList.add('hidden');
                    });
                });
            });
        </script>
        <style>
        """)

    # Navigation
    nav = Div(
        Container(
            DivFullySpaced(
                # Logo/Brand on the left
                A("CN", href="#", cls="text-xl font-bold text-white"),

                # Desktop menu (hidden on mobile)
                Div(
                    DivHStacked(
                        A("Work", href="#work",
                          cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                        A("About", href="#about",
                          cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                        A("Contact", href="#contact",
                          cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                        cls="gap-2"
                    ),
                    cls="hidden md:flex"  # Hide on mobile, show on medium screens and up
                ),

                # Hamburger menu button (visible only on mobile)
                Button(
                    Span(cls="block h-0.5 w-6 bg-white mb-1"),
                    Span(cls="block h-0.5 w-6 bg-white mb-1"),
                    Span(cls="block h-0.5 w-6 bg-white"),
                    cls="md:hidden focus:outline-none",
                    id="mobile-menu-button"
                ),

                cls="py-4 flex items-center justify-between"
            ),
            cls="max-w-7xl mx-auto px-4"  # Removed border-b class here
        ),

        # Mobile menu (initially hidden)
        Div(
            Div(
                A("Work", href="#work",
                  cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3 border-b border-blue-500/20"),
                A("About", href="#about",
                  cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3 border-b border-blue-500/20"),
                A("Contact", href="#contact",
                  cls="block text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-3"),
                cls="py-2"
            ),
            cls="hidden bg-slate-900 md:hidden",
            id="mobile-menu"
        ),

        cls="fixed-navbar"
    )

    # Hero Section
    hero = Section(
        DivCentered(
            H1("Hello, I'm Chilavert N'dah",
               cls="text-6xl font-bold mb-6 text-center text-white animate__animated animate__fadeInDown"),
            P("Software Developer ", cls="text-xl text-blue-100 mb-8 animate__animated animate__fadeInUp"),

            cls="min-h-screen flex items-center justify-center py-20 hero-content"
        ),
        cls="hero-bg",
        container=False
    )

    about = Section(
        Container(
            DivCentered(
                H2("About Me", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn text-slate-100"),
                Grid(
                    # Colonne photo
                    Div(
                        Img(src="image/full_profil.png",  # ← Votre photo
                            cls="w-full h-auto rounded-2xl shadow-2xl border-4 border-slate-700/20 animate__animated animate__fadeInLeft",
                            style="max-width: 500px;"),
                        cls="flex items-center justify-center"
                    ),

                    # Colonne texte
                    Div(
                        P("""
                            I'm a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and 
                            actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. 
                            Outside of coding, I enjoy playing basketball, listening to music, and traveling. 
                            Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅
                        """,
                          cls="text-xl max-w-2xl leading-relaxed text-slate-300 animate__animated animate__fadeInRight mb-12"),
                        # ← Ajout de mb-12 pour la marge

                        DivHStacked(
                            Button("Resume", href="...",
                                   cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeInLeft"),
                        ),
                        cls="flex flex-col items-start"
                    ),

                    cls="grid grid-cols-1 md:grid-cols-2 gap-12 items-center"  # Disposition responsive
                ),
                cls="py-32",
                id="about"
            )
        )
    )

    # Skills Section (With Animated Icons)
    skills = Section(
        Container(
            DivCentered(
                H2("Things I Can Do Without Googling... Mostly",
                   cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                Div(
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/firebase/firebase.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/dart/dart.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flutter/flutter.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/latex/latex.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/tensorflow/tensorflow.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png",
                        cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    cls="flex flex-wrap justify-center gap-4"
                ),
                cls="py-32 ",
                id="skills"
            )
        )
    )

    # GitHub Stats Section (With Animated Stats)
    github_stats = Section(
        Container(
            DivCentered(
                H2("GitHub Stats (Proof I Actually Code)",
                   cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn text-slate-100"),
                Div(
                    # Top stat (centré)
                    Img(src="https://github-readme-streak-stats.herokuapp.com?user=99ch&theme=github-dark-blue&hide_border=True&background=0f172a",
                        cls="w-full mb-8 rounded-lg animate__animated animate__fadeInDown"),

                    # Bottom stats (disposition triangulaire)
                    Grid(
                        Img(src="https://github-readme-stats.vercel.app/api/top-langs/?username=99ch&layout=compact&theme=github_dark&hide_border=True&langs_count=10&bg_color=0f172a&height=300",
                            cls=" rounded-lg animate__animated animate__fadeInRight"),

                        Div(
                            Img(src="https://github-readme-stats.vercel.app/api?username=99ch&show_icons=true&theme=github_dark&hide_border=True&bg_color=0f172a&height=300",
                                cls="w-full h-full rounded-lg animate__animated animate__fadeInRight object-contain"),
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

    # Contact Section (With Animated Form)
    contact = Section(
        Container(
            DivCentered(
                H2("Let's Connect", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                P("Feel free to reach out to me via email.",
                  cls="text-xl text-center mb-8 animate__animated animate__fadeInUp"),
                A("Send Email", href="mailto:chilavertndah99@gmail.com",
                  cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeIn"),
                cls="py-32",
                id="contact"
            )
        )
    )

    # FIXED Footer with marquee animation (preserving all original elements)
    footer = Section(
        Div(
            Div(
                DivCentered(
                    Divider(cls="mb-12 border-blue-500/20"),
                    DivHStacked(
                        A(Img(
                            src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg",
                            cls="h-8 w-8 animate__animated animate__bounce"),
                            href="https://www.linkedin.com/in/chilavert-n-dah-ab5779272/"),
                        cls="gap-4 mb-6 justify-center"
                    ),
                    # Marquee container
                    Div(
                        # Marquee wrapper
                        Div(
                            P("© 2025 Chilavert N'dah",
                              cls="footer-marquee-text text-9xl font-bold whitespace-nowrap inline-block animate-marquee"),
                            P("© 2025 Chilavert N'dah",
                              cls="footer-marquee-text text-9xl font-bold whitespace-nowrap inline-block animate-marquee"),
                            cls="footer-marquee-wrapper"
                        ),
                        cls="footer-marquee-container w-screen"
                    ),
                    cls="py-16"
                ),
                cls="w-full"
            ),
            cls="footer-container w-full"
        ),
        cls="py-0 full-bleed-section",
        container=False
    )

    return Titled(
        animate_css,
        custom_style,
        nav,
        Div(
            hero,
            about,
            skills,
            github_stats,
            contact,
            footer,
            cls="dark bg-slate-900 text-slate-100"
        )
    )


serve()