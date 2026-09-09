from kivy.clock import Clock
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import dp

Window.clearcolor = (0.035, 0.045, 0.09, 1)


QUESTIONS = {

    "SCIENCE": [

    ("Which planet is known as the Red Planet?",
     ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),

    ("What is H2O?",
     ["Oxygen", "Water", "Hydrogen", "Salt"], "Water"),

    ("Which gas do humans need for breathing?",
     ["Oxygen", "Hydrogen", "Helium", "Nitrogen"], "Oxygen"),

    ("What is the SI unit of force?",
     ["Joule", "Newton", "Watt", "Pascal"], "Newton"),

    ("Which organ pumps blood?",
     ["Lungs", "Brain", "Heart", "Kidney"], "Heart"),

    ("What is the boiling point of water?",
     ["50°C", "100°C", "150°C", "200°C"], "100°C"),

    ("Which is the nearest star to Earth?",
     ["Moon", "Sun", "Mars", "Venus"], "Sun"),

    ("What is the SI unit of energy?",
     ["Newton", "Joule", "Watt", "Pascal"], "Joule"),

    ("Which part of a plant absorbs water?",
     ["Leaf", "Flower", "Root", "Stem"], "Root"),

    ("What is the chemical symbol for oxygen?",
     ["O", "Ox", "C", "N"], "O"),

    ("Which vitamin is produced in sunlight?",
     ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"], "Vitamin D"),

    ("Which organ helps us to breathe?",
     ["Heart", "Lungs", "Kidney", "Stomach"], "Lungs"),

    ("What is the smallest unit of life?",
     ["Atom", "Cell", "Tissue", "Organ"], "Cell"),

    ("Which force pulls objects toward Earth?",
     ["Magnetic force", "Friction", "Gravity", "Electric force"], "Gravity"),

    ("How many planets are in our Solar System?",
     ["7", "8", "9", "10"], "8"),

    ("Which gas do plants absorb during photosynthesis?",
     ["Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen"], "Carbon Dioxide"),

    ("What is the SI unit of temperature?",
     ["Celsius", "Kelvin", "Fahrenheit", "Joule"], "Kelvin"),

    ("Which is the largest organ in the human body?",
     ["Heart", "Brain", "Skin", "Liver"], "Skin"),

    ("What is the center of an atom called?",
     ["Electron", "Nucleus", "Proton", "Shell"], "Nucleus"),

    ("Which blood cells fight infections?",
     ["Red blood cells", "White blood cells",
      "Platelets", "Plasma"], "White blood cells")
],

    "MATHS": [

    ("What is 12 × 8?",
     ["86", "96", "106", "116"], "96"),

    ("What is the square of 15?",
     ["125", "200", "225", "250"], "225"),

    ("What is 144 ÷ 12?",
     ["10", "11", "12", "14"], "12"),

    ("What is the value of 2³?",
     ["4", "6", "8", "9"], "8"),

    ("What is 25% of 200?",
     ["25", "40", "50", "75"], "50"),

    ("What is the HCF of 12 and 18?",
     ["3", "6", "9", "12"], "6"),

    ("What is the LCM of 4 and 6?",
     ["10", "12", "18", "24"], "12"),

    ("What is √144?",
     ["10", "11", "12", "14"], "12"),

    ("What is 7²?",
     ["14", "21", "49", "56"], "49"),

    ("What is 15 + 27?",
     ["32", "42", "52", "62"], "42"),

    ("What is 100 − 37?",
     ["53", "63", "73", "83"], "63"),

    ("What is 9 × 9?",
     ["72", "81", "91", "99"], "81"),

    ("What is 81 ÷ 9?",
     ["7", "8", "9", "10"], "9"),

    ("If x + 5 = 12, what is x?",
     ["5", "6", "7", "8"], "7"),

    ("What is the value of 5³?",
     ["25", "75", "125", "150"], "125"),

    ("What is 50% of 80?",
     ["20", "30", "40", "50"], "40"),

    ("How many degrees are in a right angle?",
     ["45°", "90°", "180°", "360°"], "90°"),

    ("What is the perimeter of a square with side 5 cm?",
     ["10 cm", "15 cm", "20 cm", "25 cm"], "20 cm"),

    ("What is the area of a rectangle of length 10 cm and breadth 5 cm?",
     ["15 cm²", "30 cm²", "50 cm²", "100 cm²"], "50 cm²"),

    ("What is the next number: 2, 4, 6, 8, ?",
     ["9", "10", "11", "12"], "10")
],

    "COMPUTER": [

    ("What does CPU stand for?",
     ["Central Processing Unit",
      "Computer Personal Unit",
      "Central Program Utility",
      "Computer Processing User"],
     "Central Processing Unit"),

    ("What does RAM stand for?",
     ["Random Access Memory",
      "Read Access Memory",
      "Rapid Action Machine",
      "Random Application Module"],
     "Random Access Memory"),

    ("Which device is used to type text?",
     ["Monitor", "Keyboard", "Speaker", "Printer"],
     "Keyboard"),

    ("What is the brain of a computer?",
     ["Mouse", "CPU", "Monitor", "Keyboard"],
     "CPU"),

    ("Which language is used to create web pages?",
     ["HTML", "Python", "C++", "Java"],
     "HTML"),

    ("What does ROM stand for?",
     ["Read Only Memory",
      "Random Only Memory",
      "Read Open Memory",
      "Run Only Memory"],
     "Read Only Memory"),

    ("Which device displays information?",
     ["Keyboard", "Monitor", "Mouse", "Scanner"],
     "Monitor"),

    ("Which device is used to print documents?",
     ["Scanner", "Printer", "Monitor", "Keyboard"],
     "Printer"),

    ("Which one is an operating system?",
     ["Windows", "Google", "YouTube", "HTML"],
     "Windows"),

    ("Which company developed Android?",
     ["Microsoft", "Google", "Apple", "IBM"],
     "Google"),

    ("What is the full form of USB?",
     ["Universal Serial Bus",
      "United System Bus",
      "Universal System Board",
      "User Serial Board"],
     "Universal Serial Bus"),

    ("Which device is used to move the pointer?",
     ["Keyboard", "Mouse", "Printer", "Speaker"],
     "Mouse"),

    ("Which of these is a programming language?",
     ["Python", "Google", "Windows", "Chrome"],
     "Python"),

    ("What is used to store files permanently?",
     ["RAM", "Hard Disk", "CPU", "Monitor"],
     "Hard Disk"),

    ("Which key is used to delete characters?",
     ["Shift", "Delete", "Caps Lock", "Tab"],
     "Delete"),

    ("What does WWW stand for?",
     ["World Wide Web",
      "World Web Window",
      "Wide World Web",
      "Web World Wide"],
     "World Wide Web"),

    ("Which one is a web browser?",
     ["Chrome", "Windows", "Python", "Android"],
     "Chrome"),

    ("What is the smallest unit of digital data?",
     ["Byte", "Bit", "KB", "MB"],
     "Bit"),

    ("Which device can scan a document?",
     ["Scanner", "Speaker", "Monitor", "Mouse"],
     "Scanner"),

    ("Which shortcut is commonly used to copy text?",
     ["Ctrl + X", "Ctrl + C", "Ctrl + V", "Ctrl + Z"],
     "Ctrl + C")
],

    "GENERAL KNOWLEDGE": [

    ("What is the capital of India?",
     ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
     "New Delhi"),

    ("How many days are there in a leap year?",
     ["365", "366", "364", "360"],
     "366"),

    ("Which is the largest ocean?",
     ["Atlantic", "Indian", "Pacific", "Arctic"],
     "Pacific"),

    ("How many continents are there?",
     ["5", "6", "7", "8"],
     "7"),

    ("Which is the fastest land animal?",
     ["Lion", "Horse", "Cheetah", "Tiger"],
     "Cheetah"),

    ("Which is the national animal of India?",
     ["Lion", "Tiger", "Elephant", "Leopard"],
     "Tiger"),

    ("Which is the national bird of India?",
     ["Eagle", "Peacock", "Parrot", "Sparrow"],
     "Peacock"),

    ("How many states are there in India?",
     ["26", "28", "29", "30"],
     "28"),

    ("Which is the largest continent?",
     ["Africa", "Europe", "Asia", "Australia"],
     "Asia"),

    ("Which planet is closest to the Sun?",
     ["Venus", "Earth", "Mercury", "Mars"],
     "Mercury"),

    ("How many hours are there in one day?",
     ["12", "18", "24", "48"],
     "24"),

    ("Which is the highest mountain in the world?",
     ["K2", "Mount Everest", "Kangchenjunga", "Makalu"],
     "Mount Everest"),

    ("Which country is known as the Land of the Rising Sun?",
     ["China", "Japan", "India", "Thailand"],
     "Japan"),

    ("How many players are there in a cricket team?",
     ["9", "10", "11", "12"],
     "11"),

    ("Which is the largest mammal?",
     ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
     "Blue Whale"),

    ("Which is the currency of Japan?",
     ["Dollar", "Yuan", "Yen", "Won"],
     "Yen"),

    ("Who wrote the Indian national anthem?",
     ["Rabindranath Tagore",
      "Bankim Chandra Chatterjee",
      "Sarojini Naidu",
      "Subhash Chandra Bose"],
     "Rabindranath Tagore"),

    ("Which ocean lies south of India?",
     ["Atlantic Ocean",
      "Indian Ocean",
      "Pacific Ocean",
      "Arctic Ocean"],
     "Indian Ocean"),

    ("How many colors are there in a rainbow?",
     ["5", "6", "7", "8"],
     "7"),

    ("Which is the smallest continent?",
     ["Europe", "Australia", "Asia", "Africa"],
     "Australia")
]
}


class QuizApp(App):

    def build(self):

        self.layout = BoxLayout(
            orientation="vertical",
            padding=[dp(25), dp(35)],
            spacing=dp(18)
        )

        self.home_screen()

        return self.layout

    # ---------- BUTTON ----------

    def make_button(self, text):

        return Button(
            text=text,
            font_size=dp(20),
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(62),
            background_normal="",
            background_color=(0.10, 0.45, 0.85, 1)
        )

    # ---------- HOME ----------

    def home_screen(self):

        self.layout.clear_widgets()

        title = Label(
            text="QUIZ MASTER",
            font_size=dp(42),
            bold=True,
            color=(0.2, 0.75, 1, 1),
            size_hint_y=None,
            height=dp(75)
        )

        subtitle = Label(
            text="TEST • LEARN • IMPROVE",
            font_size=dp(17),
            bold=True,
            color=(0.75, 0.8, 0.9, 1),
            size_hint_y=None,
            height=dp(45)
        )

        start = self.make_button("START QUIZ 🚀")
        start.bind(on_press=self.category_screen)

        self.layout.add_widget(title)
        self.layout.add_widget(subtitle)

        self.layout.add_widget(
            Label(text="", size_hint_y=0.2)
        )

        self.layout.add_widget(start)

    # ---------- CATEGORY ----------

    def category_screen(self, instance):

        self.layout.clear_widgets()

        title = Label(
            text="SELECT CATEGORY",
            font_size=dp(32),
            bold=True,
            color=(0.2, 0.75, 1, 1),
            size_hint_y=None,
            height=dp(70)
        )

        self.layout.add_widget(title)

        categories = [
            ("SCIENCE 🔬", "SCIENCE"),
            ("MATHS 📐", "MATHS"),
            ("COMPUTER 💻", "COMPUTER"),
            ("GENERAL KNOWLEDGE 🌎", "GENERAL KNOWLEDGE")
        ]

        for text, category in categories:

            button = self.make_button(text)

            button.bind(
                on_press=lambda btn, cat=category:
                self.start_category(cat)
            )

            self.layout.add_widget(button)

    # ---------- START CATEGORY ----------

    def start_category(self, category):

        self.category = category
        self.questions = QUESTIONS[category]
        self.question_number = 0
        self.score = 0

        self.show_question()

    # ---------- QUESTION ----------

    def show_question(self):
        self.layout.clear_widgets()

        question, options, answer = self.questions[
            self.question_number
        ]

        progress = Label(
            text=f"{self.category}   •   "
                 f"{self.question_number + 1}/{len(self.questions)}",
            font_size=dp(18),
            bold=True,
            color=(0.2, 0.75, 1, 1),
            size_hint_y=None,
            height=dp(45)
        )

        self.layout.add_widget(progress)

        question_label = Label(
            text=question,
            font_size=dp(24),
            bold=True,
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
            size_hint_y=None,
            height=dp(115)
        )

        question_label.bind(
            size=lambda obj, value:
            setattr(obj, "text_size", value)
        )

        self.layout.add_widget(question_label)

        self.feedback = Label(
            text="",
            font_size=dp(18),
            bold=True,
            size_hint_y=None,
            height=dp(35)
        )

        self.layout.add_widget(self.feedback)

        for option in options:

            button = self.make_button(option)

            button.bind(
                on_press=lambda btn, correct=answer:
                self.check_answer(btn, correct)
            )

            self.layout.add_widget(button)

        self.score_label = Label(
            text=f"Score: {self.score}",
            font_size=dp(18),
            bold=True,
            color=(0.75, 0.8, 0.9, 1)
        )

        self.layout.add_widget(self.score_label)

    # ---------- ANSWER ----------

    def check_answer(self, button, correct_answer):

        if button.text == correct_answer:

            self.score += 1

            button.background_color = (0.1, 0.7, 0.3, 1)

            self.feedback.text = "✓ CORRECT!"
            self.feedback.color = (0.2, 1, 0.4, 1)

        else:

            button.background_color = (0.85, 0.15, 0.2, 1)

            self.feedback.text = "✗ WRONG!"
            self.feedback.color = (1, 0.3, 0.3, 1)

        self.score_label.text = f"Score: {self.score}"

        for widget in self.layout.children:

            if isinstance(widget, Button):
                widget.disabled = True

        next_button = Button(
            text="NEXT →",
            font_size=dp(20),
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=(0.55, 0.25, 0.85, 1)
        )

        next_button.bind(
            on_press=self.next_question
        )

        self.layout.add_widget(next_button)

    # ---------- NEXT ----------

    def next_question(self, instance):

        self.question_number += 1

        if self.question_number < len(self.questions):

            self.show_question()

        else:

            self.result_screen()

    # ---------- RESULT ----------

    def result_screen(self):

        self.layout.clear_widgets()

        title = Label(
            text="🎉 QUIZ COMPLETE!",
            font_size=dp(34),
            bold=True,
            color=(0.2, 0.75, 1, 1)
        )

        result = Label(
            text=f"Your Score\n\n"
                 f"{self.score} / {len(self.questions)}",
            font_size=dp(30),
            bold=True,
            color=(1, 1, 1, 1)
        )

        restart = self.make_button("PLAY AGAIN 🔄")
        restart.bind(on_press=self.home_screen)

        self.layout.add_widget(title)
        self.layout.add_widget(result)
        self.layout.add_widget(restart)


QuizApp().run()