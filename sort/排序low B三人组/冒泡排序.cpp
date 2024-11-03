#include <stdio.h>
void bubble(int nums[], int len);
int main(void){
	int nums[10] = {1,6,2,8,7,6,9,4,3,5};
	bubble(nums, 10);
	for(int i = 0 ; i < 10 ; i ++){
		printf("%d ", nums[i]);
	}
	return 0;
}
void bubble(int nums[], int len){
	for(int i = 0 ; i < len - 1 ; i ++){
		for(int j = 0 ; j < len - i - 1 ; j ++){
			if(nums[j] > nums[j+1]){
				int temp = nums[j];
				nums[j] = nums[j+1];
				nums[j+1] = temp;
			}
		}
	}
}
