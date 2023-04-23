class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):
        # no es necesario ya que lo el interprete lo puede inferir
        return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

coords3 = coords

print(coords == coords2)
print(coords, coords2)
print(coords == coords3)
print(coords != coords2)
