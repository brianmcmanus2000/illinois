#include <iostream>
#include <set>

void print_set(std::set<int> set){
    std::set<int>::iterator i;
    for(i = set.begin(); i != set.end(); i++){
        std::cout<<*i;
    }
    std::cout << std::endl;
}

int main(){
    std::set<int> test;
    test.insert(2);
    test.insert(2);
    print_set(test);
    return 0;
}