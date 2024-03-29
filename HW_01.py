class TicTacGame:

    def __init__(self, board):
        self.board = board

    def draw_board(self):
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")

    def take_input(self, player_token):
        valid = False
        while not valid:
            player_answer = int(input(("Куда поставим " + player_token + "? ")))
            if player_answer >= 1 and player_answer <= 9:
                if str(self.board[player_answer - 1]) not in "XO":
                    self.board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клеточка уже занята")
            else:
                print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

    def main(self):
        counter = 0
        win = False
        while not win:
            self.draw_board()
            if counter % 2 == 0:
                self.take_input("X")
            else:
                self.take_input("O")
            counter += 1
            if counter > 4:
                tmp = self.check_winner()
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break

        self.draw_board()

    def check_winner(self):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]]:
                return self.board[each[0]]
        return False



tictac = TicTacGame([i for i in range(1, 10)])

tictac.main()
