from fasthtml.common import *
from monsterui.all import *

# Use blue theme for a professional look
hdrs = Theme.blue.headers()

app, rt = fast_app(hdrs=hdrs)

@rt
def index():
    # Include Animate.css
    animate_css = Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css")

    # Custom CSS for Marquee Animation
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
    """
    custom_style = Style(custom_css)

    # Navigation (Updated Design)
    nav = NavBar(
        Container(
            DivFullySpaced(

                DivHStacked(
                    A("Work", href="#work", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                    A("About", href="#about", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
                    A("Contact", href="#contact", cls="text-sm font-medium text-blue-100 hover:text-white transition-colors px-4 py-2 rounded-lg hover:bg-blue-500/20"),
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
                H2("Projects", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                Grid(
                    Card(
                        PicSumImg(800, 600, blur=1, grayscale=True),
                        CardBody(
                            H3("Vision Pro Experience", cls="text-2xl font-medium mb-2"),
                            P("Spatial computing interface (because flat screens are so 2022).", cls=TextPresets.muted_sm.value)
                        ),
                        cls="hover:scale-[1.01] transition-transform hover:shadow-2xl animate__animated animate__fadeInLeft"
                    ),
                    Card(
                        PicSumImg(800, 600, blur=1),
                        CardBody(
                            H3("iOS App Redesign", cls="text-2xl font-medium mb-2"),
                            P("Mobile interface overhaul (because users deserve better than spaghetti code).", cls=TextPresets.muted_sm.value)
                        ),
                        cls="hover:scale-[1.01] transition-transform hover:shadow-2xl animate__animated animate__fadeInRight"
                    ),
                    cls="grid grid-cols-1 md:grid-cols-2 gap-8"
                ),
                cls="py-32",
                id="work"
            )
        )
    )

    # About Me Section (With Animated Text)
    about = Section(
        Container(
            DivCentered(
                H2("About Me", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                P("""
                    I’m a Computer Science graduate from UCAO in Cotonou. Currently, I work as a freelance Software Developer and 
                    actively contribute to various open-source projects to enhance my skills in full-stack development and cloud technologies. 
                    Outside of coding, I enjoy playing basketball, listening to music, and traveling. 
                    Fun fact: I once spent 3 hours debugging only to realize I forgot to save the file. 😅
                """, cls="text-xl text-center max-w-3xl leading-relaxed " + TextPresets.muted_lg.value + " animate__animated animate__fadeInUp"),
                DivHStacked(
                    Button("Resume", href="https://drive.google.com/drive/folders/1lI8KVnN6aZ6uaj7JpwG91GhEB3we0iIX?usp=drive_link", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeInLeft"),
                    Button("LinkedIn", href="https://www.linkedin.com/in/chilavert-n-dah-ab5779272/", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeInUp"),
                    Button("YouTube", href="https://www.youtube.com/channel/UC6dVeSK8zBQGaaRE7DXA2ow", cls="text-lg bg-blue-600 text-white hover:bg-blue-700 px-6 py-3 rounded-lg transition-colors animate__animated animate__fadeInRight"),
                    cls="gap-4 mt-8"
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
                H2("GitHub Stats (Proof I Actually Code)", cls="text-4xl font-semibold mb-12 animate__animated animate__fadeIn"),
                Div(
                    Img(src="https://github-readme-streak-stats.herokuapp.com?user=99ch&theme=github-dark-blue", cls="w-full mb-8 rounded-lg animate__animated animate__fadeInLeft"),
                    Img(src="https://github-readme-stats.vercel.app/api?username=99ch&show_icons=true&theme=github_dark&hide_border=True", cls="w-full mb-8 rounded-lg animate__animated animate__fadeInRight"),
                    Img(src="https://github-readme-stats.vercel.app/api/top-langs/?username=99ch&layout=compact&theme=github_dark&hide_border=True&langs_count=10", cls="w-full rounded-lg animate__animated animate__fadeInUp"),
                    cls="grid grid-cols-1 md:grid-cols-2 gap-8"
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
        custom_style,  # Include custom CSS
        nav,
        hero,
        projects,
        about,
        skills,
        github_stats,
        contact,
        footer,
    )

serve()
