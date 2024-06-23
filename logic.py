from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability1 = self.get_ability1()
        self.ability2 = self.get_ability2()
        self.hp = randint(50, 100)
        self.power = randint(15, 45)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])

    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    def get_ability1(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['abilities'][0]['ability']['name'])
    def get_ability2(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            #Я пытался создать репозеторий
            data = response.json()
            return (data['abilities'][1]['ability']['name'])
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        enemy.hp -= self.power
        if enemy.hp == 0:
            return f"{self.pokemon_trainer} победил {enemy.pokemon_traner}"
        else:
            return f"Сражение произошло над {self.pokemon_trainer} и {enemy.pokemon_trainer}"
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, здоровье: {self.hp}, сила: {self.power}"
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_ability(self):
        return f"Способности вашего покемона: {self.ability1} и {self.ability2}"
class Wizard(Pokemon):
    pass
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\
    Боец применил супер-атаку силой:{super_power} "
    



