#include <stdio.h>
int linearSearch(int nums[], int num, int len);
int binarySearch(int nums[], int num, int len);
int main(void){
	int num = 0;
	printf("Please type in the number you want to search:");
	scanf("%d", &num);
	int nums[10] = {1, 2, 4, 19, 34, 324, 1000, 1002, 1005, 2000};
	printf("The result of linear search is %d\n", linearSearch(nums, num, 10));
	printf("The result of binary search is %d\n", binarySearch(nums, num, 10));
	return 0;
}

int linearSearch(int nums[], int num, int len){
	for(int i = 0 ; i < len ; i ++){
		if(nums[i] == num){
			return i;
		}
	}
	return -1;
}

int binarySearch(int nums[], int num, int len){
	int left = 0;
	int right = len - 1;
	while(left <= right){
		int mid = (left + right) / 2;
		if(nums[mid] > num){
			right = mid - 1;
		}else if(nums[mid] < num){
			left = mid + 1;
		}else{
			return mid;
		}
	}
	return -1;
}
