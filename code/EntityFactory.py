from code.Background import Background
from code.Const import WIN_WIDTH,GROUND_Y, PLAYER_HEIGHT, CACTUS_HEIGHT
from code.Obstacle import Obstacle
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(5):  # quantidade bg image
                    list_bg.append(Background( f'Level1Bg{i}',  (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg


            case 'Player1':
                return Player('Player1', ( 30, GROUND_Y - PLAYER_HEIGHT )) #criar PLAYER_START_X na const.py

            case 'Cactus':
                return Obstacle('Cactus', (WIN_WIDTH + 20, GROUND_Y - CACTUS_HEIGHT)) #poderia ser feito o mesmo
