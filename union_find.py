
class UnionFind:
    def __init__(self, groups):
        self.leader_to_group = {}
        self.item_to_leader = {}

        for group in groups:
            leader = group[0]
            self.leader_to_group[leader] = []
            for item in group:
                self.leader_to_group[leader].append(item)
                self.item_to_leader[item] = leader

    def find(self, item):
        return self.item_to_leader[item]

    def union(self, item_1, item_2):
        leader_1 = self.item_to_leader[item_1]
        leader_2 = self.item_to_leader[item_2]

        if leader_1 == leader_2:
            return

        leader_of_smaller_group, leader_of_larger_group = (leader_1, leader_2) if len(self.leader_to_group[leader_1]) < len(self.leader_to_group[leader_2]) else (leader_2, leader_1)

        for item in self.leader_to_group[leader_of_smaller_group]:
            self.item_to_leader[item] = leader_of_larger_group

        self.leader_to_group[leader_of_larger_group] += self.leader_to_group[leader_of_smaller_group]
        del self.leader_to_group[leader_of_smaller_group]