#include <stdio.h>
void selectSort(int nums[], int len);
int main(void){
	int nums[10] = {1, 5, 3, 2, 6, 8, 7, 9, 4, 0};
	selectSort(nums, 10);
	for(int i = 0 ; i < 10 ; i ++){
		printf("%d ", nums[i]);
	}
	
	return 0;
}

void selectSort(int nums[], int len){
	for(int i = 0 ; i < len - 1 ; i ++){
		int min = nums[i];
		int min_index = i;
		for(int j = i + 1 ; j < len ; j ++){
			if(min > nums[j]){
				min = nums[j];
				min_index = j;
			}
		}
		int temp = nums[i];
		nums[i] = nums[min_index];
		nums[min_index] = temp;
	}
}
