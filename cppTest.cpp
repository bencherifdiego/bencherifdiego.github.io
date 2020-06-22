#include <fstream>
#include <iostream>

int main()
{
    char data[100];
    std::ofstream outfile;
    outfile.open("console.txt");
    std::cin.getline(data, 100);

    outfile<<data<<std::endl;
}