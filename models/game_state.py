# define models
# import dataclass

class RoundResult:
    """
    Stores the outcome of a single completed round.
    title: str
    true_statement: str
    false_statement: str
    player_correct: bool
    """
    pass

class GameState:
    # define all data describing an active game session.
    total_rounds: int
    score: int = 0
    current_round: int = 1
    is_complete: bool = False
    pass

    # results: list[RoundResult] = field(default_factory=list)

    def record_result(self, result: RoundResult) -> None:
        """
        Appends a completed round's result and advances the game state.
        """
        pass

    def rounds_played(self) -> int:
        """Returns how many rounds have been completed."""
        return len(self.results)