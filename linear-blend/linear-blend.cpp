//
// Created by Rahul Ghangas on 4/9/19.
// For help, refer to
// http://cimg.eu/reference/structcimg__library_1_1CImgDisplay.html#ae4b8135f23d41f2077ff1d63deb452ea
// https://stackoverflow.com/questions/20375140/c11-threads-sleep-for-a-remaining-time
//  

#include <iostream>
#include <string>

#include <CImg.h>

#include <thread>
#include <chrono>

namespace cimg = cimg_library;

// Number of frames per seconds
#define PARTS_PER_SEC 50

void blend_and_show(cimg::CImg<unsigned char> &img1, cimg::CImg<unsigned char> &img2, int time);

int main(){
    // Read Image1, Image2 and duration
    std::cout << "Enter the path for first image" << std::endl;
    std::string img1_path;
    std::cin >> img1_path;

    std::cout << "\nEnter the path for Second image" << std::endl;
    std::string img2_path;
    std::cin >> img2_path;

    cimg::CImg<unsigned char> img1(img1_path.c_str()), img2(img2_path.c_str());

    unsigned int time;
    std::cout << "\n Enter time(in seconds) to blend over: ";
    std::cin >> time;
    
    blend_and_show(img1, img2, time);

    return 0;
}

void blend_and_show(cimg::CImg<unsigned char> &img1, cimg::CImg<unsigned char> &img2, int time){

    // Defined
    typedef std::chrono::duration<int, std::ratio<1, PARTS_PER_SEC>> frame_duration;

    // New display and corresponding image
    cimg::CImg<unsigned char> blend(img1.width(), img1.height(), 1, 3, 0);
    cimg::CImgDisplay display(img1, "Blended Image");

    auto start_time = std::chrono::steady_clock::now();

    float alpha;

    while (true){
        for (int i = 1; i <= PARTS_PER_SEC * time; i++){
            // Iteratively increasing end_time to simulate frame-rate
            auto end_time = start_time + frame_duration(i);

            // Cross-dissolve parameter
            alpha = (float)i / (PARTS_PER_SEC * time);

            // CImg macro for for-loops
            cimg_forXYC(blend,x,y,c) {blend(x,y,c) = ((1-alpha) * img1(x,y,c)) + (alpha * img2(x,y,c));}
            
            // Sleep until next frame
            std::this_thread::sleep_until(end_time);

            // Convert image "blend" to the internal display buffer
            display.render(blend);
            // Paint internal display buffer on associated window
            display.paint();

            if(display.is_closed()){
                goto exit;
            }
        }

    }

    exit:;
}
