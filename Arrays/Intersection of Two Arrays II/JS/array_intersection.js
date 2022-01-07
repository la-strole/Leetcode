var intersect = function(nums1, nums2) {

  nums1.sort(function(a,b){return a - b});
  nums2.sort(function(a,b){return a - b});

  var result = [];
  let i = 0;
  let j = 0;

  while ((i < nums1.length) && (j < nums2.length)){
    if (nums1[i] == nums2[j]){
      result.push(nums1[i]);
      i++;
      j++;
    }
    else if (nums1[i] < nums2[j]){
      i++;
    }
    else if (nums1[i] > nums2[j]){
      j++;
    }
  }

  return result;

};

nums1 = [1, 2, 3 ,4];
nums2 = [1, 2];
console.log(`result is ${intersect(nums1, nums2)}`);
