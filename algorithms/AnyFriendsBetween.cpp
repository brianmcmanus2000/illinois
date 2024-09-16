#include <iostream>
#include <vector>
#include <string>
#include <iterator>
using std::string;
using std::vector;

bool AnyF(string t, vector<bool> S){
    for(int i = 0; i<S.size(); i++){
        if(S[i]){
            return true;
        }
    }
    return false;
}

int count_edges_from_node(string t, vector<bool> S){
    if(S.size() == 0) return 0;
    if(S.size() == 1){
        if(AnyF(t,S)) return 1;
        else return 0;
    }
    else{
        if(AnyF(t,S)==false){
            return 0;
        }
        else{
            std::size_t const half_size = S.size() / 2;
            vector<bool> split_lo(S.begin(), S.begin() + half_size);
            vector<bool> split_hi(S.begin() + half_size, S.end());
            return count_edges_from_node(t,split_lo)+count_edges_from_node(t,split_hi);
        }
    }
}

int main(){
    vector<bool> S1 = {true,false,true,false,false,false,false,false,false,true}; //3 trues
    vector<bool> S2 = {true,false,true,false,false,false,false,false,false,true,true,false}; //4 trues
    vector<bool> S3 = {false,false,true,false,false,false,false,false,false,false}; // 1 true
    vector<bool> S4 = {false,false,false,false,false,false,false,false,false,false}; // 0 true
    string t = "test";
    std::cout << "number of edges for S1 = " << count_edges_from_node(t,S1) << std::endl;
    std::cout << "number of edges for S2 = " << count_edges_from_node(t,S2) << std::endl;
    std::cout << "number of edges for S3 = " << count_edges_from_node(t,S3) << std::endl;
    std::cout << "number of edges for S4 = " << count_edges_from_node(t,S4) << std::endl;
    return 0;
}