class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)
        self._generate_sequences(tiles, "", used, sequences)
        return len(sequences) - 1

    def _generate_sequences(self, tiles: str, current: str, used: list, sequences: set) -> None:
        sequences.add(current)
        for pos, ch in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self._generate_sequences(tiles, current+ch, used, sequences)
                used[pos] = False