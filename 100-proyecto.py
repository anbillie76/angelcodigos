import flet as ft;

def main(page: ft.Page):

    # Window Config    
    page.window_title_bar_hidden = True;
    page.window_title_bar_buttons_hidden = True;
    page.padding = 0;
    page.theme = ft.Theme(
        color_scheme_seed= ft.colors.GREEN
    )  

    # Page AppBar
    page.appbar = ft.AppBar(
        title=ft.WindowDragArea(ft.Text("BANCO")),
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        actions=[
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
        ]
    )  
    # Function to show the Home page
    def show_home():
        page.clean()
        page.add(
            ft.Column([
                ft.Text("hola"),
                # Aquí puedes agregar más contenido para la página de Inicio
            ])
        )

    # Function to show the About page
    def show_about():
        page.clean()
        page.add(
            ft.Column([
                ft.Text("Información sobre el Banco"),
                # Aquí puedes agregar más contenido para la página de Acerca de
            ])
        )

    # Page Add2
    page.add(
        ft.Row(
            [
                ft.Container(
                    expand=1,
                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                    content= ft.Column(
                        [
                            ft.TextButton(
                                text="Home",
                                icon=ft.icons.HOME,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    },   
                                ),
                                on_click= lambda _: show_home()
                            ),
                            ft.TextButton(
                                text="Settings", 
                                icon=ft.icons.SETTINGS,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    },
                                ),
                                on_click= lambda _: show_home()
                            ),
                            ft.TextButton(
                                text="ACERCA DE",
                                icon=ft.icons.QUESTION_MARK,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                            ft.TextButton(
                                text="Ubicación",
                                icon=ft.icons.LOCATION_CITY,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "": ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                            ft.TextButton(
                                text="Dinero electronico",
                                icon=ft.icons.MONEY,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                            ft.TextButton(
                                text="Preguntas frecuentes",
                                icon=ft.icons.QUESTION_ANSWER,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                            ft.TextButton(
                                text="Quejas y sugerencias",
                                icon=ft.icons.BUSINESS_CENTER,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                            ft.TextButton(
                                text="Ayudanos a mejorar la App",
                                icon=ft.icons.LIST_OUTLINED,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                             ft.TextButton(
                                text="Compartir la App",
                                icon=ft.icons.DATA_EXPLORATION_SHARP,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            ),
                             ft.TextButton(
                                text="PRIVACIDAD",
                                icon=ft.icons.LOCK,
                                width=600,
                                style=ft.ButtonStyle(
                                    shape={
                                        "":ft.RoundedRectangleBorder(radius=3)
                                    }
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    margin=0
                ),
                ft.Container(
                    expand=4,
                    content=ft.Column(
                        [
                            ft.Text(
                                value="𝔹𝔸ℕℂ𝕆 𝔼ℂ𝕆𝔽ℝ𝕀𝔼ℕ𝔻𝕃𝕐",
                                size=70,
                                color=ft.colors.PRIMARY,
                                weight="bold"
                            ),
                            ft.Text(
                                value="▀▄▀ 𝒮𝑒 𝓊𝓃𝑜 𝒸𝑜𝓃 𝓉𝓊 𝒹𝒾𝓃𝑒𝓇𝑜 ▄▀▄",
                                size=30,
                            ),  
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    margin=0
                )
            ],
            expand=3,
        )
    )
# Ejecutar la aplicacion
ft.app(target=main);