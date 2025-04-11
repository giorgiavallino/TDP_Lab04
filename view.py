import flet as ft

class View(object):

    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

    # Define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # Title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker",
                               size=24,
                               color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(ft.Row(spacing=30,
                                         controls=[self.__theme_switch, self.__title, ],
                                         alignment=ft.MainAxisAlignment.START))
        # Elementi grafici
        self._ddLang = ft.Dropdown(label="Select language",
                                   options=[ft.dropdown.Option("English"),
                                            ft.dropdown.Option("Italian"),
                                            ft.dropdown.Option("Spanish")])
        self._ddMod = ft.Dropdown(label="Select modality",
                                  options=[ft.dropdown.Option("Contains"),
                                           ft.dropdown.Option("Linear"),
                                           ft.dropdown.Option("Dicotomic")])
        self._txtIn = ft.TextField(value="Add your sentence here")
        self._btnSpell = ft.ElevatedButton(text="Spell Check",
                                           on_click=self.__controller.handleBtnSpell)
        self._lv = ft.ListView(expand=True)
        row_01 = ft.Container(content=self.__title,
                              alignment=ft.alignment.center)
        row_02 = ft.Container(content=self._ddLang,
                              alignment=ft.alignment.center)
        row_03 = ft.Row(controls=[self._ddMod, self._txtIn, self._btnSpell],
                        alignment=ft.MainAxisAlignment.CENTER)
        self.page.add(row_01, row_02, row_03, self._lv)
        self.page.update()

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
