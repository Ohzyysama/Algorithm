#include <stdio.h>
int partition(int nums[], int left, int right);
void quickSort(int nums[], int left, int right);

int main(void){
	int nums[10] = {5, 2, 6, 1, 3, 8, 9, 4, 0, 7};
	quickSort(nums, 0, 9);
	for(int i = 0 ; i < 10 ; i ++){
		printf("%d ", nums[i]);
	}
	return 0;
}

int partition(int nums[], int left, int right){
	int temp = nums[left];
	while(left < right){
		while(left < right && nums[right] > temp){
			right --;
		}
		nums[left] = nums[right];
		while(left < right && nums[left] < temp){
			left ++;
		}
		nums[right] = nums[left];
	}
	nums[left] = temp;
	return left;
}

void quickSort(int nums[], int left, int right){
	if(left < right){
		int mid = partition(nums, left, right);
		quickSort(nums, left, mid - 1);
		quickSort(nums, mid + 1, right);
	}
}
