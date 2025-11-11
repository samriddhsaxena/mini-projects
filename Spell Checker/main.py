from spellchecker import SpellChecker as Speller

class SpellChecker:
    def __init__(self):
        self.spell = Speller()

    def correct_text(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            correction = self.spell.correction(word)
            corrected_words.append(correction if correction is not None else word)
        return " ".join(corrected_words)

    def run(self):
        print("--------Spell Checker-----")

        while True:
            text = input("Enter text: ")
            if text.lower() == "exit":
                print("Goodbye!")
                break

            corrected_text = self.correct_text(text)
            print("Corrected text:", corrected_text)

if __name__ == "__main__":
    spell_checker = SpellChecker()
    spell_checker.run()