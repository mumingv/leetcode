var twoSum = function(nums, target) {
	var twoSum = [];
	for (var i = 0; i < nums.length - 1 ; i++) {
		for (var j = i + 1; j < nums.length; j++) {
			if (nums[i] + nums[j] == target) {
				twoSum[0] = i;
				twoSum[1] = j;
			}
		}
	}
	return twoSum;    
};

var nums = [2, 7, 11, 15];
var target = 22;
ret = twoSum(nums, target);
console.log(ret);

