from random import randint
import time


class FrenchAssignment:
    def __init__(self, user):
        self.user = user
        self.score = 0
    def trivia(self):
        questions = [{'question': 'Qui a chanté Sur Va Yeke?', 'awnser': 'Black M'},
                     {'question': 'Qui a chanté Outété?', 'awnser': 'KeenV'},
                     {'question': 'Combien de temps dure Outété? (en format minute:seconde)', 'awnser': '4:29'},
                     {'question': 'Combien de temps dure Rifia? (en format minute:seconde)', 'awnser': '3:02'},
                     {'question': 'Qui a gagné le premier tour?', 'awnser': 'Outete'},
                     {'question': 'Qui a gagné la deuxième ronde?', 'awnser': 'Danser avec toi'},
                     {'question': 'Qui a gagné la troisième ronde?', 'awnser': 'Case Depart'},
                     {'question': 'Qui a gagné la quatrième ronde?', 'awnser': 'Demain ca ira'}]
        print('BIENVENUE AU JEU-QUESTIONNAIRE!')
        time.sleep(1)
        print('Quand il y a une question comme celle-ci: Combien de temps dure ____, le temps est pris de la vidéo youtube.')
        time.sleep(1)
        print('Tous les awnsers sont sans accent.')
        time.sleep(1)
        print('Bienvenue {}!'.format(self.user))
        print('Le jeu commencera dans deux secondes.')
        time.sleep(2)
        while len(questions) > 1:
            q, questions = self.choose_random(questions, 1)
            if not q:
                break
            print(q[0]['question'])
            awn = input('')
            awn = awn.lower()
            if awn == q[0]['awnser'].lower():
                print('Bon travail, vous avez raison!')
                self.score += 1
                print('Votre note actuelle est {}'.format(self.score))
            else:
                print('incorrect!')
                print('Votre note actuelle est {}'.format(self.score))
                print('Le bon awnser est {}'.format(q[0]['question']))
        print('Le jeu-questionnaire est terminé!')
        print('Vous avez {} points!'.format(self.score))
    
    def choose_random(self, l, amount):
        if len(l) < amount:
            print('choose_random has encountered an error')
            return False, False
        li = l
        r = []
        for i in range(amount):
            index = randint(0, len(li) - 1)
            r.append(li[index])
            del li[index]
        return r, li
    
    def 


assign = FrenchAssignment(input('Nom d’utilisateur:\n'))
assign.trivia()
