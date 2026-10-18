class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        i = 0
        j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            list1 = firstList[i]
            list2 = secondList[j]
            if list1[1] < list2[0]:
                i += 1
                continue
            if list1[0] > list2[1]:
                j += 1
                continue
            res.append([max(list1[0], list2[0]), min(list1[1], list2[1])])
            if list1[1] < list2[1]:
                i += 1
            elif list2[1] < list1[1]:
                j += 1
            else:
                i += 1
                j += 1
        return res