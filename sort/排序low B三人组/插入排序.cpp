#include <stdio.h>
void insertSort(int nums[], int len);
int main(void){
	int nums[10] = {4, 6, 1, 2, 0, 9, 5, 8, 3, 7};
	insertSort(nums, 10);
	for(int i = 0 ; i < 10 ; i ++){
		printf("%d ", nums[i]);
	}
	return 0;
}

void insertSort(int nums[], int len){
	for(int i = 1 ; i < len ; i ++){
		int j = i - 1;
		int temp = nums[i];
		while(j >= 0 && nums[j] > temp){
			nums[j+1] = nums[j];
			j --;
		}
		nums[j+1] = temp;
	}
}
