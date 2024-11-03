#include <stdio.h>
void sift(int nums[], int high, int low);
void topk(int nums[], int len, int k);
int main(void){
	int nums[9] = {4, 1, 3, 7, 9, 8, 6, 5, 2};
	topk(nums, 9, 4);
	return 0;
}
//思想：堆排序的应用
void sift(int nums[], int high, int low){
	int i = low;
	int j = 2 * i + 1;
	int temp = nums[low];
	while(j <= high){
		if((j+1 <= high) && (nums[j] > nums[j+1])){
			j = j + 1;
		}
		if(nums[j] < temp){
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

void topk(int nums[], int len, int k){
	int heap[k] = {0};
	for(int i = 0 ; i < k ; i ++){
		heap[i] = nums[i];
	}
	//建堆
	for(int i = (k-2)/2 ; i >= 0 ; i --){
		sift(heap, k-1, i);
	}
	//处理剩下的数
	for(int i = k ; i < len ; i ++){
		if(nums[i] > heap[0]){
			int temp = nums[i];
			nums[i] = heap[0];
			heap[0] = temp;
		}
		sift(heap, k-1, 0);
	}
	//取数
	for(int i = k-1 ; i >= 0 ; i --){
		int tmp = heap[0];
		heap[0] = heap[i];
		heap[i] = tmp;
		sift(heap, i-1, 0);
	}
	//打印结果
	for(int i = 0 ; i < k ; i ++){
		printf("%d ", heap[i]);
	}
}
