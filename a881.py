'''
第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。

每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。

返回载到每一个人所需的最小船数。(保证每个人都能被船载)。
'''
class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i < j:
            if (people[i] + people[j]) <= limit:
                i += 1
                j -= 1
                count += 1
            else:
                j -= 1
                count += 1

        if i == j:
            count += 1
        
        return count