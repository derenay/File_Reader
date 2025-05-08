#include <iostream>
#include <fstream>
#include <filesystem>
#include <thread>
#include <mutex>
#include <vector>
#include <set>
#include <chrono>

using namespace std;

namespace fs = std::filesystem;
std::mutex file_mutex;

std::vector<std::string> directory_reader(const std::string& dir_name){
    std::vector<std::string> file_paths;
    
    if (fs::exists(dir_name)){
        for(const auto& entry : fs::recursive_directory_iterator(dir_name)){
            file_paths.push_back(entry.path());
        }
    }
    return file_paths;
}

void file_writer(const std::string& file_name, const std::vector<std::string> paths){
    if (fs::exists(file_name)){
        std::ofstream config_file(file_name);
        for(const std::string& path_ : paths){
            config_file << path_<<"\n";
        }
    }
}

std::vector<std::string> file_reader(const std::string& file_name){
    std::string line;
    std::vector<string> lines;

    if (fs::exists(file_name)){
        std::ifstream config_file(file_name);
        
        while(std::getline(config_file,line)){
            lines.push_back(line);
        }
    }
    return lines;
}


void watcher(std::vector<std::string>& stored_paths, const std::string file_name){
    while(true){
        std::this_thread::sleep_for(std::chrono::seconds(2));
        std::lock_guard<std::mutex> lock(file_mutex);
        stored_paths = file_reader(file_name);
    }
}

int main(){
    std::string dir_name = "./gelen_fotograflar" ;
    std::string file_name =  "./gelen_fotograflar/config.txt";
    std::vector<std::string> stored_paths;

    thread t2(watcher, ref(stored_paths), file_name);

    while(true){
        std::this_thread::sleep_for(std::chrono::seconds(5));
        std::vector<std::string> file_paths = directory_reader(dir_name);
        {
            std::lock_guard<std::mutex> lock(file_mutex);
            std::set<std::string> current_set(file_paths.begin(),file_paths.end());
            std::set<std::string> stored_set(stored_paths.begin(),stored_paths.end());
        
            if(current_set != stored_set){
                std::cout << "Değişiklik tespit edildi. config.txt güncelleniyor...\n";
                file_writer(file_name, file_paths);
            }
        }
    }

    t2.join();
    return 0;
}


// config_file << entry.path()<<"\n";




