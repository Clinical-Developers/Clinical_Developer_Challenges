// Example program - By Jeremy Thornton - still needs a bit of debugging but it's getting there
#include <iostream>
#include <algorithm>
#include <vector>

int main() {

    std::vector<int> data {1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6};
    
    std::remove_if(data.begin(), data.end(), [](const int& n){ return ((n < 1) | (n > 10)); });
    
    std::cout << "sanitized:";
    for (auto& datum : data) {
        std::cout << ' ' << datum;
    }
    std::cout << std::endl;
    
    std::cout << std::accumulate(data.begin(), data.end(), 0);

}
