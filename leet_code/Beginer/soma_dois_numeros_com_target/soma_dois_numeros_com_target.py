import time


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.target = target
        dict_result = {}
        list_indexes = []

        for index, num in enumerate(nums):
            complemento = self.target - num
            if complemento not in dict_result.keys():
                dict_result[num] = index
            else:
                list_indexes.append(dict_result[complemento])
                list_indexes.append(index)
        if len(list_indexes) == 0:
            raise Exception("Não há solução para o target")

        return list_indexes
