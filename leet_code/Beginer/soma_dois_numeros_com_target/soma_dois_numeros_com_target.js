/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    let map_indexes = {};
    for (let i = 0; i < nums.length; i++) {
        let complemento = target - nums[i];
        if (complemento in map_indexes) {

            return [map_indexes[complemento], i];
        }

        map_indexes[nums[i]] = i;
    }

    map_indexes = null;
    if (map_indexes == null) {
        throw new Error("Não há solução para o target");
    }
    return [];
};

