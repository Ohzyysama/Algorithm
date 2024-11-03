#include <stdio.h>
void sift(int nums[], int low, int high);
void heapSort(int nums[], int len);
int main(void){
	int nums[9] = {4, 2, 1, 8, 5, 9, 6, 7, 3};
	heapSort(nums, 9);
	for(int i = 0 ; i < 9 ; i ++){
		printf("%d ", nums[i]);
	}
	return 0;
}

void sift(int nums[], int low, int high){
	int i = low;
	int j = 2 * i + 1;
	int temp = nums[low];
	while (j <= high){
		if(j+1 <= high && nums[j] < nums[j+1]){
			j = j + 1;
		}
		if(temp < nums[j]){
			nums[i] = nums[j];
			i = j;
			j = 2 * i + 1;
		}else{
			nums[i] = temp;
			break;
		}
	}
	nums[i] = temp;
}

void heapSort(int nums[], int len){
	for(int k = (len-2) / 2 ; k >= 0 ; k --){
		sift(nums, k, len-1);
	}
	for(int k = len-1 ; k >= 0 ; k --){
		int temp = nums[k];
		nums[k] = nums[0];
		nums[0] = temp;
		sift(nums, 0, k-1);
	}
}
