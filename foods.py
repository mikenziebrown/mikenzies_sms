import random

all_foods = ['ð', 'ð','ð','ð','ð','ð','ð','ð','ð','ðŦ','ð',
             'ð','ð','ðĨ­','ð','ðĨĨ','ðĨ','ð','ð','ðĨ','ðĨĶ','ðĨŽ',
             'ðĨ','ðķïļ','ðŦ','ð―','ðĨ', 'ðŦ','ð§','ð§','ðĨ','ð ','ðĨ',
             'ðĨŊ','ð','ðĨ','ðĨĻ','ð§','ðĨ','ðģ','ð§','ðĨ','ð§','ðĨ',
             'ðĨĐ','ð','ð­','ðĶī','ð','ð','ð','ð','ðŦ','ðĨŠ','ðĨ',
             'ðĨ','ðŦ','ðŊ','ðŪ','ð§','ðĨ','ðŦ','ðĨŦ','ðŦ','ð','ðą',
             'ðĢ','ð','ðē','ð','ðĨ','ðĶŠ','ðĪ','ð','ð','ð','ðĨ',
             'ðĨ ','ðĨŪ','ðĒ','ðĄ','ð§','ðĻ','ðĶ','ðĨ§','ð­','ðŪ','ð',
             'ð°','ð§','ðŽ','ðŦ','ðŋ','ðĐ','ðŠ','ðŊ','ðŦ','ðĨ','ð°']



class foods:
    choices = {}
    food_hunger = []

    def __init__(self):
        self.choices = random.choices(all_foods, k=3)
        for food in self.choices:
            self.food_hunger.append(random.randint(1, 10))

    def show_choices(self):
        for count,choice in enumerate(self.choices):
            print(f"{choice} --- {self.food_hunger[count]}")

    def give_food_choices(self):
        food_options = []
        for count,choice in enumerate(self.choices):
            food_option = food(choice, self.food_hunger[count])
            print(food_option.emoji, food_option.hunger, end=' ')
            food_options.append(food_option)
        return food_options
        

        
class food:
    emoji = ''
    hunger = 0

    def __init__(self, emoji, hunger):
        self.emoji = emoji
        self.hunger = hunger


test = foods()
test.give_food_choices()

