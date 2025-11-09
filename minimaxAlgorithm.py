
# 創建遊戲設定物件
class GameSettings:
    def __init__(self, board_size=3, win_length=3):
        self.board_size = board_size  # 棋盤大小
        self.win_length = win_length    # 連線長度

        self.AWARDS = {
            'WIN': 1,
            'DRAW': 0,
            'LOSS': -1
        } # 得分
        self.players = ['X', 'O']      # 玩家符號


class TicTacToe(GameSettings):
    def __init__(self) -> None:
        super().__init__()
        self.board = []

    def _vaildInput(self, input):
        pass

    def _moveComputer(self):
        pass
    
    def _movePlayer(self):
        pass

    def _is_wins(self):
        pass

    def _is_draw(self):
        pass

    def _is_loss(self):
        pass

    def checkState(self):
        """
        檢查遊戲狀態，首先盤面已經滿了並且以下情況之一成立:
        1. 玩家獲勝回傳 'WIN'
        2. 平手回傳 'DRAW'
        3. 電腦獲勝回傳 'LOSS'
        4. 遊戲繼續回傳 None
        """

        if self._is_wins():
            return 'WIN'
        
        if self._is_draw():
            return 'DRAW'
        
        if self._is_loss():
            return 'LOSS'

    def run (self):

        print("開始遊戲")
        while True:
            self._moveComputer() 
            self._movePlayer()

    def printBoard(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * (self.board_size * 4 - 3))



def runner(board_size=3, win_length=3):
    settings = GameSettings(board_size, win_length)
    print(f"Game Settings: Board Size = {settings.board_size}, Win Length = {settings.win_length}, Players = {settings.players}")

    # 執行遊戲



if __name__ == "__main__":
    runner()