#include <iostream>
#include <stdio.h>

int total_value, no_of_cars, total_sum_possible = 0;

int main()
{
	std::cin>>total_value;
	std::cin>>no_of_cars;
	int car_array[no_of_cars+1];
	car_array[0] = 0;
	for(int i = 1; i <= no_of_cars; i++) {
		std::cin>>car_array[i];

	}
	int matrix[no_of_cars + 1][total_value + 1];
        for(int i = 0; i <= no_of_cars; i++){
		for(int j = 0; j <= total_value; j++)
		{
			matrix[i][j] = -1; 
		}
	}
	matrix[0][0] = 1;
	int total_till_now = 0;
	int latest_car = 0;
	for(int i = 1; i <= no_of_cars; i++) {
		total_till_now += car_array[i];
		for(int j = 0; j <= total_value; j++) {
		
			if(matrix[i-1][j] == 1) {
				int right = total_till_now - j;
				if(right > 0 && right <= total_value)
					{
					latest_car = i;
					matrix[i][j] = 1;
					if(car_array[i] + j <= total_value)
						matrix[i][j + car_array[i]] = 1;
					}
			}
		}
			
	}
	std::cout<<latest_car<<"\n";
	for(int i = latest_car; i > 0; i--) {
		int k;
		if( i == latest_car)
		{
			for(k = total_value; k >= 0; k--) {
				if(matrix[latest_car][k] == 1)
					break;
			}
		}		
		if(matrix[i-1][k] == 1)
			std::cout<<"R"<<"\n";
		else {
			k -= car_array[i];
			std::cout<<"L"<<"\n";
		}
			
	}
}