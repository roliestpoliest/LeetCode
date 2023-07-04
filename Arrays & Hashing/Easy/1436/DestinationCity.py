class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities = set()

        for p in paths:
            cities.add(p[0]) 
            cities.add(p[1])
        for p in paths:
            if p[0] in cities:
                cities.remove(p[0])
        return cities.pop()