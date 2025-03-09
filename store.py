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

        .animate-marquee {
            display: inline-block;
            animation: marquee 10s linear infinite;
            white-space: nowrap;
            width: max-content;
        }

        /* Appliquer le motif de cahier au body entier */
        body {
            background-color: #0f172a !important;
            color: #f8fafc !important;
            background-image: 
                linear-gradient(rgba(148, 163, 184, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(148, 163, 184, 0.1) 1px, transparent 1px) !important;
            background-size: 100% 24px, 24px 100% !important;
            background-position: 0 0 !important;
        }

        /* S'assurer que les éléments sur le fond sont toujours visibles */
        .dark.bg-slate-900 {
            background-color: transparent !important; /* Rendre transparent pour voir le fond */
        }

        /* Pour la NavBar, ajouter un fond semi-transparent pour que les lignes soient visibles */
        .backdrop-blur-lg.bg-blue-600\/90 {
            background-color: rgba(30, 64, 175, 0.85) !important; /* Un peu plus transparent */
        }

        .dark .text-blue-100 {
            color: #e0f2fe !important;
        }

        .github-triangle-layout {
            position: relative;
            margin-top: 4rem;
        }

        .github-triangle-layout::after {
            content: '';
            position: absolute;
            top: -30px;
            left: 50%;
            transform: translateX(-50%);
            border-left: 20px solid transparent;
            border-right: 20px solid transparent;
            border-bottom: 30px solid #1e293b;
        }

        /* Supprime les bordures des composants Card */
        .card {
            border: none !important;
            box-shadow: none !important;
        }

        /* Supprime les bordures des images */
        img {
            border: none !important;
            outline: none !important;
        }
    """
    custom_style = Style(custom_css)

    # Navigation
    # Navigation (Updated Design)
    nav = NavBar(
        Container(
            DivFullySpaced(

                DivHStacked(
                    A("Work", href="#work",
                      cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                    A("About", href="#about",
                      cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                    A("Contact", href="#contact",
                      cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                    cls="gap-2"
                ),
                cls="py-4 flex items-center justify-between"
            ),
            cls="backdrop-blur-lg bg-blue-600/90 sticky top-0 border-b border-blue-500/20"
        )
    )

    # Hero Section (With Profile Picture and Animated Title)
    hero = Section(
        DivCentered(
            # Add a clickable profile picture
            Img(src="./image/logo.png",
                cls="h-32 w-32 rounded-full cursor-pointer profile-pic animate__animated animate__bounce"),
            H1("Hello, I'm Chilavert N'dah",
               cls="text-6xl font-bold mb-6 text-center text-white animate__animated animate__fadeInDown"),
            P("Software Developer ", cls="text-xl text-blue-100 mb-8 animate__animated animate__fadeInUp"),
            Button("View My Work",
                   cls="text-lg bg-white text-blue-600 hover:bg-blue-50 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeIn",
                   href="#work"),
            cls="min-h-screen flex items-center justify-center py-20 "
        )
    )

    # Projects Section (With Animated Cards)
    projects = Section(
        Container(
            DivCentered(
                H2("Projects", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn text-slate-100"),
                Grid(
                    Card(
                        PicSumImg(800, 600, blur=1, grayscale=True),
                        CardBody(
                            H3("Vision Pro Experience", cls="text-2xl font-medium mb-2 text-slate-100"),
                            P("Spatial computing interface...",
                              cls="text-slate-400 text-sm")
                        ),
                        cls="hover:scale-[1.01] transition-transform hover:shadow-2xl animate__animated animate__fadeInLeft bg-slate-800/50 backdrop-blur-sm border-0"
                        # ← border-0 ici
                    ),
                    Card(
                        PicSumImg(800, 600, blur=1),
                        CardBody(
                            H3("iOS App Redesign", cls="text-2xl font-medium mb-2 text-slate-100"),
                            P("Mobile interface overhaul...",
                              cls="text-slate-400 text-sm")
                        ),
                        cls="hover:scale-[1.01] transition-transform hover:shadow-2xl animate__animated animate__fadeInRight bg-slate-800/50 backdrop-blur-sm border-0"
                        # ← border-0 ici
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
                                   cls="text-lg bg-slate-700 text-slate-100 hover:bg-slate-600 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeInLeft"),
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
                H2("Things I Can Do Without Googling... Mostly", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                Div(
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/django/django.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/cpp/cpp.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/bootstrap/bootstrap.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/javascript/javascript.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/firebase/firebase.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/dart/dart.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flutter/flutter.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/latex/latex.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/tensorflow/tensorflow.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
                    Img(src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/visual-studio-code/visual-studio-code.png", cls="h-16 w-16 mx-2 hover:scale-110 transition-transform animate__animated animate__fadeIn"),
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
            P("Feel free to reach out to me via email.", cls="text-xl text-center mb-8 animate__animated animate__fadeInUp"),
            A("Send Email", href="mailto:chilavertndah99@gmail.com", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeIn"),
            cls="py-32",
            id="contact"
        )
    )
)

    # Footer (With Continuous Marquee Animation)
    footer = Section(
        Container(
            DivCentered(
                Divider(cls="mb-12"),
                DivHStacked(
                    A(Img(src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg", cls="h-8 w-8 animate__animated animate__bounce"), href="https://www.linkedin.com/in/chilavert-n-dah-ab5779272/"),
                    cls="gap-4 mb-6"
                ),
                # Marquee Container
                Div(
                    # Original Text
                    P(
                        "© 2025 Chilavert N'dah",
                        cls="text-9xl font-bold whitespace-nowrap inline-block animate-marquee",
                    ),
                    # Duplicate Text
                    P(
                        "© 2025 Chilavert N'dah",
                        cls="text-9xl font-bold whitespace-nowrap inline-block animate-marquee",
                    ),
                    cls="whitespace-nowrap overflow-hidden w-full",  # Ensure the container hides overflow
                ),
                cls=" text-center",
            )
        )
    )

    return Titled(
        animate_css,
        custom_style,
        nav,
        Div(  # Ajouter un conteneur global avec classes Tailwind
            hero,
            projects,
            about,
            skills,
            github_stats,
            contact,
            footer,
            cls="dark bg-slate-900 text-slate-100"  # Couleurs forcées
        )
    )

serve()