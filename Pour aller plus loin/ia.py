def ia(board, signe):
    
    positions_vides = [i for i in range(9) if board[i] == 0]

    for position in positions_vides:
        # Copie du tableau pour simuler le coup
        board_copy = board.copy()
        board_copy[position] = signe

        # Vérification du gain potentiel après le coup
        if est_gagnant(board_copy, signe):
            return position

    # Si aucune victoire potentielle, choisir une position au hasard
    import random
    return random.choice(positions_vides)

def est_gagnant(board, signe):
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if (board[i*3] == board[i*3+1] == board[i*3+2] == signe or
            board[i] == board[i+3] == board[i+6] == signe):
            return True

    if board[0] == board[4] == board[8] == signe or board[2] == board[4] == board[6] == signe:
        return True

    return False