import json

from src.utils import paths

DATA_PATH = paths.ASSETS_DIR / "champion_ratings.json"

class Champ:
    _champs = None  # Cached

    def __init__(self, cid, data):
        self.cid = cid
        self.name = data["name"]
        self.primary = data["Primary"]
        self.secondary = data["Secondary"]
        self.ratings = data["Ratings"]
        self.attacks = data["Basic Attacks"]
        self.style = data["Style"]
        self.ability = data["Abilities"]
        self.type = data["Damage Type"]
        self.diff = data["Difficulty"]
        
        # Deferred fields
        self.raw_gain = None
        self.raw_wr = None
        self.norm_gain = None
        self.norm_wr = None
        self.flags = []
        self.score = None

    def __repr__(self):
        return f"Champ({self.cid}, {self.name})"

    @classmethod
    def load_champs(cls):
        """Loads champions from JSON and caches them."""
        if cls._champs is None:
            with open(DATA_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
            cls._champs = {cid: cls(cid, cdata) for cid, cdata in data.items()}
        return cls._champs

    @classmethod
    def get(cls, cid):
        """Retrieve a champion by ID."""
        champs = cls.load_champs()
        return champs.get(cid, None)

    def debug(self):
        """Prints all champion attributes for debugging."""
        info = f"""
        Champ ID: {self.cid}
        Name: {self.name}
        Primary: {self.primary}
        Secondary: {self.secondary}
        Ratings: {self.ratings}
        Basic Attacks: {self.attacks}
        Style: {self.style}
        Abilities: {self.ability}
        Damage Type: {self.type}
        Difficulty: {self.diff}
        Raw Gain: {self.raw_gain}
        Raw WR: {self.raw_wr}
        Norm Gain: {self.norm_gain}
        Norm WR: {self.norm_wr}
        Flags: {self.flags}
        Score: {self.score}
        """
        print(info)

if __name__ == "__main__":
    champs = Champ.load_champs()

    test_id = "266"
    champ = Champ.get(test_id) # aatrox
    if champ:
        champ.debug()
    else:
        print("Champion not found.")
