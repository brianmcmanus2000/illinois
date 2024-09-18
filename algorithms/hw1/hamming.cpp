#include <string>
#include <iostream>
#include <math.h>

using std::string;
using std::cout;
using std::endl;

void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;
    
    for (i = size-1; i >= 0; i--) {
        for (j = 7; j >= 0; j--) {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
    puts("");
}

int hamming_distance(char* arg1, char* arg2,int offset){
    int hamming_distance = 0;
    int i =0;
    while(true){
        if(arg1[i] == '\0' || arg2[i] == '\0'){
            break;
        }
        if(arg1[i] != arg2[i+offset]){
            hamming_distance++;
        }
        i++;
    }
    return hamming_distance;
}

bool first_smaller(char* arg1, char* arg2){
    int i =0;
    while(true){
        if(arg1[i] == '\0'){
            return true;
        }
        i++;
        if(arg2[i] == '\0'){
            return false;
        }
    }
}

int char_size(char* arg1){
    int i =0;
    while(true){
        if(arg1[i] == '\0'){
            break;
        }
        i++;
    }
    return i;
}

int min_ham_dist(char* arg1, char* arg2){
    //first argument is always assumed to be smaller
    int num_checks = char_size(arg2) - char_size(arg1) + 1;
    //cout << "num checks = " << num_checks << endl;
    int min_dist = pow(2,char_size(arg1));
    for(int i = 0; i<num_checks; i++){
        //cout << "i = " << i << endl;
        int curr_dist = hamming_distance(arg1,arg2,i);
        //cout << "min_dist = " << min_dist << endl;
        //cout << "curr_dis = " << curr_dist << endl;
        if (curr_dist < min_dist){
            min_dist = curr_dist;
        }
    }
    return min_dist;
}

int main(int argc, char* argv[]){
    cout << "fist arg: " << argv[1] << ", second arg: " << argv[2] << endl;
    if(first_smaller(argv[1],argv[2])){
        min_ham_dist(argv[1],argv[2]);
    }
    else{
        min_ham_dist(argv[2],argv[1]);
    }
    cout << "minimum hamming distance is: " << min_ham_dist(argv[1],argv[2]) << endl;
    return 0;
}